const ICON_PATHS = {
  email:
    '<path d="M3 6.75A1.75 1.75 0 0 1 4.75 5h14.5A1.75 1.75 0 0 1 21 6.75v10.5A1.75 1.75 0 0 1 19.25 19H4.75A1.75 1.75 0 0 1 3 17.25Zm1.5.56v9.94c0 .14.11.25.25.25h14.5a.25.25 0 0 0 .25-.25V7.31l-7.04 5.16a.75.75 0 0 1-.88 0Zm14.7-.81H4.8L12 11.78Z" />',
  phone:
    '<path d="M6.62 10.79a15.5 15.5 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.01-.24 11.4 11.4 0 0 0 3.58.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.49a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .57 3.58 1 1 0 0 1-.24 1.01Z" />',
  linkedin:
    '<path d="M6.94 8.5A1.56 1.56 0 1 1 6.94 5.4a1.56 1.56 0 0 1 0 3.1M5.7 9.75h2.5V18H5.7zm4.06 0h2.4v1.13h.04c.33-.63 1.15-1.3 2.37-1.3 2.54 0 3.01 1.67 3.01 3.84V18h-2.5v-4.04c0-.96-.02-2.2-1.34-2.2-1.35 0-1.56 1.06-1.56 2.14V18h-2.5z" />',
  orcid:
    '<path d="M7.35 5.5a1.35 1.35 0 1 1 0 2.7 1.35 1.35 0 0 1 0-2.7M6.3 9.4h2.1v7.6H6.3zm3.65 0h3.06c2.85 0 4.75 1.61 4.75 3.8 0 2.39-1.82 3.8-4.82 3.8H9.95Zm2.1 1.74v4.12h.78c1.69 0 2.76-.77 2.76-2.06 0-1.32-1-2.06-2.71-2.06Z" />',
  gitlab:
    '<path d="m12 18.9 2.94-9.04H9.06Zm0 0-9.12-6.63 2.55-7.85a.46.46 0 0 1 .87 0l2.76 8.48Zm0 0 9.12-6.63-2.55-7.85a.46.46 0 0 0-.87 0l-2.76 8.48Z" />',
};

const ICON_CLASSES = {
  linkedin: "icon-link icon-link-linkedin",
  orcid: "icon-link icon-link-orcid",
  gitlab: "icon-link icon-link-gitlab",
  cern_gitlab: "icon-link icon-link-gitlab icon-link-labeled",
};

export async function loadModule(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Failed to load module: ${path}`);
  }

  return parseModule(await response.text());
}

export function parseModule(raw) {
  const normalized = raw.replace(/\r\n/g, "\n").trim();
  let attributes = {};
  let body = normalized;

  if (normalized.startsWith("---\n")) {
    const end = normalized.indexOf("\n---\n", 4);
    if (end !== -1) {
      attributes = parseFrontMatter(normalized.slice(4, end));
      body = normalized.slice(end + 5).trim();
    }
  }

  return { attributes, body };
}

function parseFrontMatter(raw) {
  const attributes = {};

  raw.split("\n").forEach((line) => {
    const trimmed = line.trim();
    if (!trimmed) {
      return;
    }

    const separator = trimmed.indexOf(":");
    if (separator === -1) {
      return;
    }

    const key = trimmed.slice(0, separator).trim();
    const value = trimmed.slice(separator + 1).trim();
    attributes[key] = parseFrontMatterValue(value);
  });

  return attributes;
}

function parseFrontMatterValue(value) {
  if (value.includes(" | ")) {
    return value.split("|").map((item) => item.trim()).filter(Boolean);
  }

  return value;
}

export function parseBulletItems(markdown) {
  return markdown
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line.startsWith("- "))
    .map((line) => line.slice(2).trim())
    .filter(Boolean);
}

export function splitMarkdownSections(markdown) {
  const sections = {};
  let currentKey = "default";
  const buffer = [];

  const flush = () => {
    const content = buffer.join("\n").trim();
    if (content) {
      sections[currentKey] = content;
    }
    buffer.length = 0;
  };

  markdown.split("\n").forEach((line) => {
    const match = line.match(/^##\s+(.+)$/);
    if (match) {
      flush();
      currentKey = slugify(match[1]);
      return;
    }

    buffer.push(line);
  });

  flush();
  return sections;
}

export function renderMarkdown(markdown) {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const blocks = [];
  let index = 0;

  while (index < lines.length) {
    const line = lines[index].trim();

    if (!line) {
      index += 1;
      continue;
    }

    const headingMatch = line.match(/^(#{1,3})\s+(.+)$/);
    if (headingMatch) {
      const level = headingMatch[1].length;
      blocks.push(`<h${level}>${renderInline(headingMatch[2])}</h${level}>`);
      index += 1;
      continue;
    }

    if (line.startsWith("- ")) {
      const items = [];
      while (index < lines.length && lines[index].trim().startsWith("- ")) {
        items.push(`<li>${renderInline(lines[index].trim().slice(2))}</li>`);
        index += 1;
      }
      blocks.push(`<ul>${items.join("")}</ul>`);
      continue;
    }

    const paragraph = [];
    while (index < lines.length) {
      const current = lines[index].trim();
      if (!current || current.match(/^(#{1,3})\s+/) || current.startsWith("- ")) {
        break;
      }
      paragraph.push(current);
      index += 1;
    }

    blocks.push(`<p>${renderInline(paragraph.join(" "))}</p>`);
  }

  return blocks.join("");
}

function renderInline(text) {
  const escaped = escapeHtml(text);
  return escaped
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
}

function escapeHtml(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

export function renderSkillPills(container, markdown) {
  container.innerHTML = parseBulletItems(markdown)
    .map((item) => `<span class="skill-pill">${escapeHtml(item)}</span>`)
    .join("");
}

export function renderCaseStudy(module, index) {
  const sections = splitMarkdownSections(module.body);
  const introHtml = renderMarkdown(sections.default || "");
  const evidenceHtml = sections.evidence
    ? `
      <div class="case-evidence">
        <p class="case-evidence-title">${escapeHtml(
          module.attributes.evidence_title || "Selected evidence from project work",
        )}</p>
        ${renderMarkdown(sections.evidence).replace("<ul>", '<ul class="case-evidence-list">')}
      </div>
    `
    : "";

  return `
    <article class="case-study" id="work-${index + 1}">
      <div class="case-study-header">
        <p class="case-number">${escapeHtml(module.attributes.number || String(index + 1).padStart(2, "0"))}</p>
        <h3>${escapeHtml(module.attributes.title || `Work ${index + 1}`)}</h3>
      </div>
      <div class="case-tags" aria-label="Skills and tools used">
        ${(module.attributes.tags || [])
          .map((tag) => `<span class="case-tag">${escapeHtml(tag)}</span>`)
          .join("")}
      </div>
      ${introHtml}
      <p class="case-meta"><strong>Methods:</strong> ${escapeHtml(module.attributes.methods || "")}</p>
      <p class="impact-note"><strong>Impact:</strong> ${escapeHtml(module.attributes.impact || "")}</p>
      <p class="impact">Industry relevance: ${escapeHtml(module.attributes.industry || "")}</p>
      ${evidenceHtml}
    </article>
  `;
}

export function renderTopbarLinks(profile) {
  return [
    createIconLink({
      href: `mailto:${profile.email}`,
      ariaLabel: "Email",
      title: "Email",
      icon: "email",
      className: "icon-link",
    }),
    createIconLink({
      href: profile.linkedin,
      ariaLabel: "LinkedIn",
      title: "LinkedIn",
      icon: "linkedin",
      className: ICON_CLASSES.linkedin,
    }),
    createIconLink({
      href: profile.orcid,
      ariaLabel: "ORCID",
      title: "ORCID",
      icon: "orcid",
      className: ICON_CLASSES.orcid,
    }),
    createIconLink({
      href: profile.personal_gitlab,
      ariaLabel: "GitLab",
      title: "GitLab",
      icon: "gitlab",
      className: ICON_CLASSES.gitlab,
    }),
    createIconLink({
      href: profile.cern_gitlab,
      ariaLabel: "CERN GitLab",
      title: "CERN GitLab",
      icon: "gitlab",
      className: ICON_CLASSES.cern_gitlab,
      label: "CERN",
    }),
  ].join("");
}

export function renderResumeContact(profile, phoneLabel) {
  return `
    <a class="contact-link" href="mailto:${escapeAttribute(profile.email)}">
      <span class="contact-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24">${ICON_PATHS.email}</svg>
      </span>
      <span>${escapeHtml(profile.email)}</span>
    </a>
    <div class="contact-link">
      <span class="contact-icon" aria-hidden="true">
        <svg viewBox="0 0 24 24">${ICON_PATHS.phone}</svg>
      </span>
      <button
        class="reveal-button"
        type="button"
        data-reveal="phone"
        data-value="${escapeAttribute(profile.phone)}"
      >${escapeHtml(phoneLabel)}</button>
    </div>
    <div class="resume-icon-links" aria-label="Profile links">
      ${createIconLink({
        href: profile.linkedin,
        ariaLabel: "LinkedIn",
        title: "LinkedIn",
        icon: "linkedin",
        className: ICON_CLASSES.linkedin,
      })}
      ${createIconLink({
        href: profile.orcid,
        ariaLabel: "ORCID",
        title: "ORCID",
        icon: "orcid",
        className: ICON_CLASSES.orcid,
      })}
      ${createIconLink({
        href: profile.personal_gitlab,
        ariaLabel: "Personal GitLab",
        title: "Personal GitLab",
        icon: "gitlab",
        className: ICON_CLASSES.gitlab,
      })}
      ${createIconLink({
        href: profile.cern_gitlab,
        ariaLabel: "CERN GitLab",
        title: "CERN GitLab",
        icon: "gitlab",
        className: ICON_CLASSES.cern_gitlab,
        label: "CERN",
      })}
    </div>
  `;
}

function createIconLink({ href, ariaLabel, title, icon, className, label = "" }) {
  return `
    <a class="${className}" href="${escapeAttribute(href)}" aria-label="${escapeAttribute(
      ariaLabel,
    )}" title="${escapeAttribute(title)}">
      <svg viewBox="0 0 24 24" aria-hidden="true">${ICON_PATHS[icon]}</svg>
      ${label ? `<span class="icon-link-text">${escapeHtml(label)}</span>` : ""}
    </a>
  `;
}

export function escapeAttribute(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/"/g, "&quot;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}
