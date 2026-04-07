#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

ICON_PATHS = {
    "email": 'M3 6.75A1.75 1.75 0 0 1 4.75 5h14.5A1.75 1.75 0 0 1 21 6.75v10.5A1.75 1.75 0 0 1 19.25 19H4.75A1.75 1.75 0 0 1 3 17.25Zm1.5.56v9.94c0 .14.11.25.25.25h14.5a.25.25 0 0 0 .25-.25V7.31l-7.04 5.16a.75.75 0 0 1-.88 0Zm14.7-.81H4.8L12 11.78Z',
    "phone": 'M6.62 10.79a15.5 15.5 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.01-.24 11.4 11.4 0 0 0 3.58.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.49a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .57 3.58 1 1 0 0 1-.24 1.01Z',
    "linkedin": 'M6.94 8.5A1.56 1.56 0 1 1 6.94 5.4a1.56 1.56 0 0 1 0 3.1M5.7 9.75h2.5V18H5.7zm4.06 0h2.4v1.13h.04c.33-.63 1.15-1.3 2.37-1.3 2.54 0 3.01 1.67 3.01 3.84V18h-2.5v-4.04c0-.96-.02-2.2-1.34-2.2-1.35 0-1.56 1.06-1.56 2.14V18h-2.5z',
    "orcid": 'M7.35 5.5a1.35 1.35 0 1 1 0 2.7 1.35 1.35 0 0 1 0-2.7M6.3 9.4h2.1v7.6H6.3zm3.65 0h3.06c2.85 0 4.75 1.61 4.75 3.8 0 2.39-1.82 3.8-4.82 3.8H9.95Zm2.1 1.74v4.12h.78c1.69 0 2.76-.77 2.76-2.06 0-1.32-1-2.06-2.71-2.06Z',
    "gitlab": 'm12 18.9 2.94-9.04H9.06Zm0 0-9.12-6.63 2.55-7.85a.46.46 0 0 1 .87 0l2.76 8.48Zm0 0 9.12-6.63-2.55-7.85a.46.46 0 0 0-.87 0l-2.76 8.48Z',
}


def parse_module(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n").strip()
    attributes = {}
    body = raw

    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end == -1 and raw.endswith("\n---"):
            end = len(raw) - 4
        if end != -1:
            attributes = parse_front_matter(raw[4:end])
            body = raw[end + 5 :].strip() if raw[end : end + 5] == "\n---\n" else ""

    return {"attributes": attributes, "body": body}


def parse_front_matter(raw: str) -> dict:
    attributes = {}
    multi_value_keys = {"tags"}
    for line in raw.split("\n"):
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key in multi_value_keys and " | " in value:
            attributes[key] = [part.strip() for part in value.split("|") if part.strip()]
        else:
            attributes[key] = value
    return attributes


def render_inline(text: str) -> str:
    html = escape(text)
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)
    html = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)
    return html


def render_markdown(markdown: str) -> str:
    lines = markdown.replace("\r\n", "\n").split("\n")
    blocks = []
    index = 0

    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue

        heading_match = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading_match:
            level = len(heading_match.group(1))
            blocks.append(f"<h{level}>{render_inline(heading_match.group(2))}</h{level}>")
            index += 1
            continue

        if line.startswith("- "):
            items = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                items.append(f"<li>{render_inline(lines[index].strip()[2:])}</li>")
                index += 1
            blocks.append(f"<ul>{''.join(items)}</ul>")
            continue

        paragraph = []
        while index < len(lines):
            current = lines[index].strip()
            if not current or re.match(r"^(#{1,3})\s+", current) or current.startswith("- "):
                break
            paragraph.append(current)
            index += 1
        blocks.append(f"<p>{render_inline(' '.join(paragraph))}</p>")

    return "".join(blocks)


def split_sections(markdown: str) -> dict:
    sections = {}
    current = "default"
    buffer = []

    def flush():
        content = "\n".join(buffer).strip()
        if content:
            sections[current] = content
        buffer.clear()

    for line in markdown.split("\n"):
        match = re.match(r"^##\s+(.+)$", line)
        if match:
            flush()
            current = slugify(match.group(1))
            continue
        buffer.append(line)

    flush()
    return sections


def slugify(text: str) -> str:
    return re.sub(r"(^-|-$)", "", re.sub(r"[^a-z0-9]+", "-", text.lower()))


def parse_bullets(markdown: str) -> list[str]:
    return [line.strip()[2:] for line in markdown.split("\n") if line.strip().startswith("- ")]


def icon_link(href: str, aria_label: str, title: str, icon: str, class_name: str, label: str = "") -> str:
    label_html = f'<span class="icon-link-text">{escape(label)}</span>' if label else ""
    return (
        f'<a class="{class_name}" href="{escape(href, quote=True)}" '
        f'aria-label="{escape(aria_label, quote=True)}" title="{escape(title, quote=True)}">'
        f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{ICON_PATHS[icon]}" /></svg>'
        f"{label_html}</a>"
    )


def render_topbar_links(profile: dict) -> str:
    return "".join(
        [
            icon_link(f"mailto:{profile['email']}", "Email", "Email", "email", "icon-link"),
            icon_link(profile["linkedin"], "LinkedIn", "LinkedIn", "linkedin", "icon-link icon-link-linkedin"),
            icon_link(profile["orcid"], "ORCID", "ORCID", "orcid", "icon-link icon-link-orcid"),
            icon_link(profile["personal_gitlab"], "GitLab", "GitLab", "gitlab", "icon-link icon-link-gitlab"),
            icon_link(
                profile["cern_gitlab"],
                "CERN GitLab",
                "CERN GitLab",
                "gitlab",
                "icon-link icon-link-gitlab icon-link-labeled",
                "CERN",
            ),
        ]
    )


def render_resume_contact(profile: dict, phone_label: str) -> str:
    return f"""
<a class="contact-link" href="mailto:{escape(profile['email'], quote=True)}">
  <span class="contact-icon" aria-hidden="true">
    <svg viewBox="0 0 24 24"><path d="{ICON_PATHS['email']}" /></svg>
  </span>
  <span>{escape(profile['email'])}</span>
</a>
<div class="contact-link">
  <span class="contact-icon" aria-hidden="true">
    <svg viewBox="0 0 24 24"><path d="{ICON_PATHS['phone']}" /></svg>
  </span>
  <button class="reveal-button" type="button" data-reveal="phone" data-value="{escape(profile['phone'], quote=True)}">{escape(phone_label)}</button>
</div>
<div class="resume-icon-links" aria-label="Profile links">
  {icon_link(profile["linkedin"], "LinkedIn", "LinkedIn", "linkedin", "icon-link icon-link-linkedin")}
  {icon_link(profile["orcid"], "ORCID", "ORCID", "orcid", "icon-link icon-link-orcid")}
  {icon_link(profile["personal_gitlab"], "Personal GitLab", "Personal GitLab", "gitlab", "icon-link icon-link-gitlab")}
  {icon_link(profile["cern_gitlab"], "CERN GitLab", "CERN GitLab", "gitlab", "icon-link icon-link-gitlab icon-link-labeled", "CERN")}
</div>
""".strip()


def render_case_study(module: dict, index: int) -> str:
    sections = split_sections(module["body"])
    attrs = module["attributes"]
    tags = "".join(f'<span class="case-tag">{escape(tag)}</span>' for tag in attrs.get("tags", []))
    evidence_html = ""
    if "evidence" in sections:
        evidence_html = f"""
<div class="case-evidence">
  <p class="case-evidence-title">{escape(attrs.get("evidence_title", "Selected evidence from project work"))}</p>
  {render_markdown(sections["evidence"]).replace("<ul>", '<ul class="case-evidence-list">', 1)}
</div>
""".strip()

    return f"""
<article class="case-study" id="work-{index + 1}">
  <div class="case-study-header">
    <p class="case-number">{escape(attrs.get("number", str(index + 1).zfill(2)))}</p>
    <h3>{escape(attrs.get("title", f"Work {index + 1}"))}</h3>
  </div>
  <div class="case-tags" aria-label="Skills and tools used">{tags}</div>
  {render_markdown(sections.get("default", ""))}
  <p class="case-meta"><strong>Methods:</strong> {escape(attrs.get("methods", ""))}</p>
  <p class="impact-note"><strong>Impact:</strong> {escape(attrs.get("impact", ""))}</p>
  <p class="impact">Industry relevance: {escape(attrs.get("industry", ""))}</p>
  {evidence_html}
</article>
""".strip()


def build_index(profile: dict) -> str:
    intro = parse_module(CONTENT / "index/intro.md")
    seeking = parse_module(CONTENT / "index/seeking.md")
    skills = parse_module(CONTENT / "index/skills.md")
    overview = parse_module(CONTENT / "index/overview.md")
    positioning = parse_module(CONTENT / "index/positioning.md")
    works = [parse_module(CONTENT / f"index/work-{i}.md") for i in range(1, 6)]

    skill_pills = "".join(f'<span class="skill-pill">{escape(item)}</span>' for item in parse_bullets(skills["body"]))
    work_map = "".join(
        f'<li><a href="#work-{index + 1}">{escape(work["attributes"]["title"])}</a></li>'
        for index, work in enumerate(works)
    )
    work_cards = "\n".join(render_case_study(work, index) for index, work in enumerate(works))

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{escape(profile["name"])} | Selected Work</title>
    <meta
      name="description"
      content="Selected work by {escape(profile['name'])}, focused on data science, probabilistic modelling, signal extraction, bias correction, and machine learning under uncertainty."
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&amp;family=Space+Grotesk:wght@400;500;700&amp;display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="page-shell">
      <nav class="topbar">
        <div class="topbar-identity">
          <a class="brand" href="#top">{escape(profile["name"])}</a>
          <div class="icon-links topbar-links" aria-label="Personal links">
            {render_topbar_links(profile)}
          </div>
        </div>
        <div class="nav-links">
          <a href="#overview">Overview</a>
          <a href="#selected-work">Selected Work</a>
          <a href="#competencies">Skills</a>
          <a href="resume.html" target="_blank" rel="noopener noreferrer">Resume</a>
        </div>
      </nav>

      <header class="hero">
        <div class="hero-layout" id="top">
          <section class="profile-panel">
            <p class="eyebrow">{escape(intro["attributes"].get("eyebrow", "Personal Introduction"))}</p>
            <h1>{escape(intro["attributes"].get("title", ""))}</h1>
            <p class="hero-about">{escape(intro["attributes"].get("about", ""))}</p>
            <div class="hero-copy">{render_markdown(intro["body"])}</div>

            <section class="sidebar-section">
              <p class="sidebar-label">Seeking opportunities as</p>
              <div class="sidebar-copy">{render_markdown(seeking["body"])}</div>
            </section>

            <section class="sidebar-section" id="competencies">
              <p class="sidebar-label">Skills &amp; Tools</p>
              <div class="skill-list">
                {skill_pills}
              </div>
            </section>
          </section>

          <aside class="toc-panel" id="overview" aria-label="Overview and selected work index">
            <p class="eyebrow">{escape(overview["attributes"].get("eyebrow", "Overview"))}</p>
            <h2>{escape(overview["attributes"].get("title", ""))}</h2>
            <div class="toc-copy">{render_markdown(overview["body"])}</div>
            <p class="sidebar-label">{escape(overview["attributes"].get("map_label", "Selected Work Map"))}</p>
            <ol class="toc-list">
              {work_map}
            </ol>
          </aside>
        </div>
      </header>

      <main>
        <section class="section" id="selected-work">
          <div class="section-heading">
            <p class="eyebrow">Selected Work</p>
            <h2>Selected work</h2>
          </div>

          <div class="case-study-grid">
            {work_cards}
          </div>
        </section>

        <section class="section closing">
          <div class="closing-panel">
            <p class="eyebrow">{escape(positioning["attributes"].get("eyebrow", "Positioning"))}</p>
            <h2>{escape(positioning["attributes"].get("title", ""))}</h2>
            {render_markdown(positioning["body"])}
          </div>
        </section>
      </main>
    </div>
  </body>
</html>
"""


def build_resume(profile: dict) -> str:
    shell = {
        lang: parse_module(CONTENT / f"resume/{lang}/shell.md")["attributes"]
        for lang in ("en", "fr")
    }
    sections = {
        lang: {
            name: parse_module(CONTENT / f"resume/{lang}/{name}.md")
            for name in ("summary", "education", "skills", "languages", "highlights", "experience")
        }
        for lang in ("en", "fr")
    }

    resume_content = {}
    for lang in ("en", "fr"):
        resume_content[lang] = {
            "title": shell[lang]["title"],
            "description": shell[lang]["description"],
            "eyebrow": shell[lang]["eyebrow"],
            "back_home": shell[lang]["back_home"],
            "contact_label": shell[lang]["contact_label"],
            "education_label": shell[lang]["education_label"],
            "skills_label": shell[lang]["skills_label"],
            "languages_label": shell[lang]["languages_label"],
            "highlights_label": shell[lang]["highlights_label"],
            "experience_label": shell[lang]["experience_label"],
            "summary_html": render_markdown(sections[lang]["summary"]["body"]),
            "contact_html": render_resume_contact(profile, shell[lang]["phone_label"]),
            "education_html": render_markdown(sections[lang]["education"]["body"]),
            "skills_html": render_markdown(sections[lang]["skills"]["body"]),
            "languages_html": render_markdown(sections[lang]["languages"]["body"]),
            "highlights_html": render_markdown(sections[lang]["highlights"]["body"]),
            "experience_html": render_markdown(sections[lang]["experience"]["body"]),
        }

    payload = json.dumps(resume_content, ensure_ascii=False)
    initial = resume_content["en"]

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{escape(initial["title"])}</title>
    <meta name="description" content="{escape(initial["description"], quote=True)}" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&amp;family=Space+Grotesk:wght@400;500;700&amp;display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body class="resume-page">
    <div class="resume-shell">
      <header class="resume-header">
        <div>
          <p class="eyebrow" id="resume-eyebrow">{escape(initial["eyebrow"])}</p>
          <div class="resume-name-row">
            <h1 id="resume-name">{escape(profile["name"])}</h1>
            <button
              class="name-audio-button"
              type="button"
              aria-label="Play name pronunciation"
              title="Play name pronunciation"
              id="name-audio-button"
            >
              <svg viewBox="0 0 24 24" aria-hidden="true">
                <path d="M4 9.5A1.5 1.5 0 0 1 5.5 8H9l4.18-3.35A1 1 0 0 1 14.8 5.43v13.14a1 1 0 0 1-1.62.78L9 16H5.5A1.5 1.5 0 0 1 4 14.5Zm12.73-2.52a.75.75 0 0 1 1.04.2 8.1 8.1 0 0 1 0 9.64.75.75 0 1 1-1.24-.84 6.6 6.6 0 0 0 0-7.96.75.75 0 0 1 .2-1.04m2.57-2.44a.75.75 0 0 1 1.05.14 12.21 12.21 0 0 1 0 14.64.75.75 0 1 1-1.19-.92 10.71 10.71 0 0 0 0-12.8.75.75 0 0 1 .14-1.06" />
              </svg>
            </button>
            <audio id="name-audio" preload="metadata">
              <source id="name-audio-source" src="{escape(profile['audio'], quote=True)}" type="audio/mpeg" />
            </audio>
          </div>
          <p class="resume-location" id="resume-location">{escape(profile["location"])}</p>
        </div>
        <div class="resume-header-actions">
          <div class="resume-links">
            <a href="index.html" id="back-home-link">{escape(initial["back_home"])}</a>
          </div>
          <div class="resume-flag-switcher" aria-label="Language switcher">
            <button class="lang-flag is-active" type="button" data-lang-btn="en" aria-label="English CV" title="English CV">🇬🇧</button>
            <button class="lang-flag" type="button" data-lang-btn="fr" aria-label="CV en français" title="CV en français">🇫🇷</button>
          </div>
        </div>
      </header>

      <section class="resume-card resume-summary" id="resume-summary">{initial["summary_html"]}</section>

      <div class="resume-grid">
        <aside class="resume-sidebar">
          <section class="resume-card">
            <p class="sidebar-label" id="contact-label">{escape(initial["contact_label"])}</p>
            <div class="contact-list" id="resume-contact">{initial["contact_html"]}</div>
          </section>

          <section class="resume-card">
            <p class="sidebar-label" id="education-label">{escape(initial["education_label"])}</p>
            <div class="resume-markdown resume-sidebar-markdown" id="resume-education">{initial["education_html"]}</div>
          </section>

          <section class="resume-card">
            <p class="sidebar-label" id="skills-label">{escape(initial["skills_label"])}</p>
            <div class="resume-markdown resume-sidebar-markdown" id="resume-skills">{initial["skills_html"]}</div>
          </section>

          <section class="resume-card">
            <p class="sidebar-label" id="languages-label">{escape(initial["languages_label"])}</p>
            <div class="resume-markdown resume-sidebar-markdown" id="resume-languages">{initial["languages_html"]}</div>
          </section>
        </aside>

        <main class="resume-main">
          <section class="resume-card">
            <p class="sidebar-label" id="highlights-label">{escape(initial["highlights_label"])}</p>
            <div class="resume-markdown resume-main-markdown" id="resume-highlights">{initial["highlights_html"]}</div>
          </section>

          <section class="resume-card">
            <p class="sidebar-label" id="experience-label">{escape(initial["experience_label"])}</p>
            <div class="resume-markdown resume-main-markdown" id="resume-experience">{initial["experience_html"]}</div>
          </section>
        </main>
      </div>
    </div>
    <script>
      const resumeContent = {payload};
      const descriptionMeta = document.querySelector('meta[name="description"]');
      const langButtons = document.querySelectorAll("[data-lang-btn]");
      const nameAudioButton = document.getElementById("name-audio-button");
      const nameAudio = document.getElementById("name-audio");

      const dom = {{
        html: document.documentElement,
        eyebrow: document.getElementById("resume-eyebrow"),
        backHomeLink: document.getElementById("back-home-link"),
        contactLabel: document.getElementById("contact-label"),
        educationLabel: document.getElementById("education-label"),
        skillsLabel: document.getElementById("skills-label"),
        languagesLabel: document.getElementById("languages-label"),
        highlightsLabel: document.getElementById("highlights-label"),
        experienceLabel: document.getElementById("experience-label"),
        summary: document.getElementById("resume-summary"),
        contact: document.getElementById("resume-contact"),
        education: document.getElementById("resume-education"),
        skills: document.getElementById("resume-skills"),
        languages: document.getElementById("resume-languages"),
        highlights: document.getElementById("resume-highlights"),
        experience: document.getElementById("resume-experience"),
      }};

      function bindPhoneReveal() {{
        const phoneButton = dom.contact.querySelector("[data-reveal='phone']");
        if (!phoneButton) {{
          return;
        }}

        phoneButton.addEventListener("click", () => {{
          phoneButton.textContent = phoneButton.dataset.value;
          phoneButton.classList.add("is-revealed");
          phoneButton.disabled = true;
        }});
      }}

      function applyResumeLanguage(lang) {{
        const copy = resumeContent[lang];
        dom.html.lang = lang;
        document.title = copy.title;
        if (descriptionMeta) {{
          descriptionMeta.setAttribute("content", copy.description);
        }}

        dom.eyebrow.textContent = copy.eyebrow;
        dom.backHomeLink.textContent = copy.back_home;
        dom.contactLabel.textContent = copy.contact_label;
        dom.educationLabel.textContent = copy.education_label;
        dom.skillsLabel.textContent = copy.skills_label;
        dom.languagesLabel.textContent = copy.languages_label;
        dom.highlightsLabel.textContent = copy.highlights_label;
        dom.experienceLabel.textContent = copy.experience_label;
        dom.summary.innerHTML = copy.summary_html;
        dom.contact.innerHTML = copy.contact_html;
        dom.education.innerHTML = copy.education_html;
        dom.skills.innerHTML = copy.skills_html;
        dom.languages.innerHTML = copy.languages_html;
        dom.highlights.innerHTML = copy.highlights_html;
        dom.experience.innerHTML = copy.experience_html;

        bindPhoneReveal();

        langButtons.forEach((button) => {{
          button.classList.toggle("is-active", button.dataset.langBtn === lang);
        }});

        window.localStorage.setItem("resume-lang", lang);
      }}

      langButtons.forEach((button) => {{
        button.addEventListener("click", () => {{
          applyResumeLanguage(button.dataset.langBtn);
        }});
      }});

      if (nameAudioButton && nameAudio) {{
        const setNameAudioState = (isPlaying) => {{
          nameAudioButton.classList.toggle("is-playing", isPlaying);
        }};

        nameAudio.addEventListener("play", () => setNameAudioState(true));
        nameAudio.addEventListener("pause", () => setNameAudioState(false));
        nameAudio.addEventListener("ended", () => setNameAudioState(false));

        nameAudioButton.addEventListener("click", async () => {{
          if (!nameAudio.paused) {{
            nameAudio.pause();
            nameAudio.currentTime = 0;
            return;
          }}

          nameAudio.currentTime = 0;
          try {{
            await nameAudio.play();
          }} catch (error) {{
            nameAudioButton.disabled = true;
            nameAudioButton.title = "Audio playback is blocked in this browser";
          }}
        }});
      }}

      applyResumeLanguage(window.localStorage.getItem("resume-lang") || "en");
    </script>
  </body>
</html>
"""


def main():
    profile = parse_module(CONTENT / "shared/profile.md")["attributes"]
    (ROOT / "index.html").write_text(build_index(profile), encoding="utf-8")
    (ROOT / "resume.html").write_text(build_resume(profile), encoding="utf-8")


if __name__ == "__main__":
    main()
