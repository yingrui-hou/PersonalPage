#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import dataclass
from html import unescape
from pathlib import Path

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, StyleSheet1, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import (
        KeepTogether,
        Paragraph,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing PDF dependency 'reportlab'. "
        "Run with PYTHONPATH=/tmp/codex-pdf-tools or install reportlab first."
    ) from exc


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESUME_HTML = ROOT / "resume.html"
DEFAULT_INDEX_HTML = ROOT / "index.html"
DEFAULT_PROFILE = ROOT / "content" / "shared" / "profile.md"
DEFAULT_SHORTLIST = SCRIPT_DIR / "jobs_shortlist_simulation_validation_2026-04-20.md"
DEFAULT_OUTPUT = SCRIPT_DIR / "output" / "pdf"

ACCENTS = {
    "A1": {"primary": colors.HexColor("#16324F"), "light": colors.HexColor("#E9F0F6")},
    "A2": {"primary": colors.HexColor("#0F5D5E"), "light": colors.HexColor("#E6F3F1")},
    "A3": {"primary": colors.HexColor("#7A4E2D"), "light": colors.HexColor("#F5ECE4")},
    "A4": {"primary": colors.HexColor("#355E3B"), "light": colors.HexColor("#E8F1EA")},
    "A5": {"primary": colors.HexColor("#3A4A73"), "light": colors.HexColor("#E9ECF5")},
}

STOPWORDS = {
    "a",
    "about",
    "an",
    "and",
    "are",
    "as",
    "at",
    "aux",
    "avec",
    "avant",
    "be",
    "by",
    "dans",
    "data",
    "de",
    "des",
    "du",
    "en",
    "et",
    "for",
    "from",
    "in",
    "la",
    "le",
    "les",
    "my",
    "of",
    "on",
    "pour",
    "sur",
    "systemes",
    "systems",
    "that",
    "the",
    "their",
    "through",
    "to",
    "with",
}

SKILL_KEYWORDS = {
    "Python": ("python", "automation", "scientific software"),
    "C/C++": ("c++", "c/c++", "software", "development"),
    "NumPy": ("python", "analysis"),
    "pandas": ("data", "analysis"),
    "scikit-learn": ("ml", "machine learning", "selection"),
    "statsmodels": ("statistical", "modelling", "inference"),
    "matplotlib / seaborn": ("analysis", "visualisation", "reporting"),
    "ROOT / RooFit": ("root", "fit", "calibration", "analysis"),
    "Geant4": ("simulation", "physical systems", "system response", "model"),
    "CatBoost / Gradient Boosting": ("ml", "gradient boosting", "domain adaptation"),
    "Probabilistic Modelling": ("likelihood", "uncertainty", "inference"),
    "Statistical Inference": ("inference", "parameter estimation", "likelihood"),
    "Maximum Likelihood Estimation": ("likelihood", "parameter estimation", "fit"),
    "Model Validation": ("validation", "v&v", "verification", "ivv", "qa", "quality"),
    "Calibration & Bias Correction": ("calibration", "bias", "correction"),
    "Simulation-to-Data Alignment": ("simulation", "measurement", "alignment", "test", "corrélation"),
    "Signal Processing": ("signal", "pulse", "timing", "time-resolved"),
    "Domain Adaptation": ("dataset shift", "domain adaptation", "reweighting"),
    "Workflow Automation (YAML / Shell / CMake)": ("automation", "workflow", "linux", "shared environments"),
    "Large-Scale Data Analysis": ("large-scale", "shared codebases", "collaboration"),
}

SKILL_GROUP_ORDER = ("Tools", "Methods", "Validation", "ML")

PROJECT_LABELS = {
    "en": {
        "target": "Target Application",
        "intro": "Introduction personnelle",
        "personal": "Personal Info",
        "profile": "Role Narrative",
        "skills": "Core Tools & Methods",
        "evidence": "Current Resume Evidence",
        "fit": "Selected Fit For This Role",
        "experience": "Relevant Experience",
        "projects": "Selected Project",
        "education": "Education",
        "languages": "Languages",
        "city": "City",
        "phone": "Phone",
        "email": "Email",
        "portfolio": "Portfolio",
        "methods": "Methods",
        "impact": "Impact",
        "relevance": "Industry relevance",
        "outcomes": "Selected outcomes",
    },
    "fr": {
        "target": "Candidature ciblée",
        "personal": "Informations personnelles",
        "profile": "Narratif de positionnement",
        "skills": "Outils & méthodes clés",
        "evidence": "Preuves issues du CV actuel",
        "fit": "Arguments clés pour ce poste",
        "experience": "Expérience pertinente",
        "projects": "Projets les plus pertinents",
        "education": "Formation",
        "languages": "Langues",
        "city": "Ville",
        "phone": "Téléphone",
        "email": "Email",
        "portfolio": "Portfolio",
        "methods": "Méthodes",
        "impact": "Impact",
        "relevance": "Pertinence industrielle",
        "outcomes": "Résultats marquants",
    },
}

JOB_EN_OVERRIDES = {
    "A1": {
        "bullets": [
            "Developed reusable Python/C++ workflows for validation, calibration, and analysis of noisy measurement systems in shared technical environments.",
            "Built monitoring and validation workflows to identify reconstruction and calibration discrepancies, then trace anomalies back to detector or software causes.",
            "Identified concrete anomalies that led to corrective actions, including a missing-energy software issue later fixed in reconstruction.",
            "Developed ROOT/C++ calibration and correction workflows to reduce structured bias and compare performance before and after correction across operating conditions.",
            "Worked in large shared codebases with review discipline, result reproducibility, and reinjection of validation outputs into modelling decisions.",
            "Aligned simulation and data through reweighting and control-sample calibration before downstream decisions, avoiding the propagation of software or model bias.",
        ],
        "fit": "software validation, automation, Python, Linux, critical environment, and a direct link to software quality and internal simulation tools.",
    },
    "A2": {
        "fit": "the closest match to your core evidence: calibration, signal processing, experimental data, and scientific software.",
    },
    "A3": {
        "bullets": [
            "Developed and adapted Geant4/C++ code for system-response and simulation studies on physical systems, including model logic, geometry, and analysis outputs.",
            "Developed ROOT/C++ calibration and correction workflows to reduce structured bias and compare performance before and after correction.",
            "Built reusable Python/C++ workflows in shared technical environments, with strong attention to robustness and traceability.",
            "Built validation and monitoring workflows that detect anomalies, trace their causes, and feed corrective actions back to the relevant teams.",
            "Combined test measurements, simulation, and response maps to model the measurement chain and quantify the system impact of observed discrepancies.",
            "Wrote structured decision-facing technical results that connect models, methods, discrepancies, and proposed improvements.",
        ],
        "fit": "simulation-software component development, Python/C, QA, testing and validation, technical reporting, and interaction with product teams.",
    },
    "A4": {
        "bullets": [
            "Combined test-beam data, simulation, and response maps to model the measurement chain and quantify the effect of non-uniformities on resolution.",
            "Developed and adapted Geant4/C++ code for system-response studies, directly linking model assumptions to measured results.",
            "Built time-resolved signal-analysis workflows that recovered component fractions and improved energy resolution by about a factor of 2.",
            "Developed calibration and correction workflows to stabilize model behaviour across operating conditions.",
            "Produced analysis outputs usable by technical experts by connecting simulation, test results, and diagnostics instead of stopping at curve comparisons.",
            "Built validation workflows that distinguish discrepancies coming from the detector, the model, or the software.",
        ],
        "fit": "modelling, experimental validation, and reliable analysis built from both simulations and instrumented tests.",
    },
    "A5": {
        "bullets": [
            "Developed reusable C++/Python workflows for modelling, validation, and inference on noisy systems without direct ground truth.",
            "Developed and adapted Geant4/C++ simulation code for system-response studies, with analysis outputs usable for technical assessment.",
            "Combined test measurements, simulation, and response maps to quantify the impact of physical non-idealities on system performance.",
            "Developed calibration and correction workflows to compare performance before and after adjustment and make models more reliable.",
            "Built validation and monitoring workflows that turned observed discrepancies into software or modelling corrective actions.",
            "Worked in large shared technical environments with review discipline, code reusability, and support for calibration and modelling decisions.",
        ],
        "fit": "complex-system modelling, test integration, V&V, user support, and work in broad industrial engineering environments.",
    },
}

JOB_FR_INTRO_OVERRIDES = {
    "A2": [
        "Ingénieure logicielle scientifique issue de la physique expérimentale, avec plusieurs années d'expérience dans le développement de workflows réutilisables en Python/C++ pour la calibration, la validation et l'inférence sur des systèmes de mesure bruités.",
        "Mon point fort est de transformer des mesures imparfaites et des modèles imparfaits en workflows fiables et exploitables pour la décision, grâce à l'analyse du signal, à l'extraction de paramètres, à la logique de correction et à une validation robuste.",
        "Je suis particulièrement pertinente pour des rôles où la rigueur scientifique, l'automatisation, l'analyse de données expérimentales et la fiabilité de la calibration comptent davantage que l'analytics générique.",
    ]
}


@dataclass
class ExperienceSection:
    title: str
    organization: str
    bullets: list[str]


@dataclass
class ResumeLanguageContent:
    summary_paragraphs: list[str]
    outcomes: list[str]
    skills: list[str]
    highlights: list[str]
    experience_sections: list[ExperienceSection]
    experience_label: str
    education_lines: list[str]
    languages: list[str]


@dataclass
class ResumeSource:
    en: ResumeLanguageContent
    fr: ResumeLanguageContent


@dataclass
class ProjectCase:
    case_id: str
    title: str
    tags: list[str]
    preview: str
    methods: str
    impact: str
    relevance: str


@dataclass
class SiteSource:
    positioning_title: str
    positioning_text: str
    hero_about: str
    hero_copy: list[str]
    projects: list[ProjectCase]
    tools_methods: list[str]


@dataclass
class JobSpec:
    code: str
    company: str
    role: str
    title: str
    summary: list[str]
    bullets: list[str]
    fit: str
    risk: str
    links: list[str]
    language: str

    @property
    def filename(self) -> str:
        company_slug = "".join(
            part.capitalize() for part in re.split(r"[^A-Za-z0-9]+", ascii_slug(self.company)) if part
        )
        return f"CV_YingruiHou_{company_slug}.pdf"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate targeted CV PDFs for each A-grade job in the shortlist."
    )
    parser.add_argument("--resume-html", type=Path, default=DEFAULT_RESUME_HTML)
    parser.add_argument("--index-html", type=Path, default=DEFAULT_INDEX_HTML)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--shortlist", type=Path, nargs="+", default=[DEFAULT_SHORTLIST])
    parser.add_argument("--exclude-shortlist", type=Path, nargs="*", default=[])
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def parse_front_matter(path: Path) -> dict[str, str]:
    raw = read_text(path).strip()
    if not raw.startswith("---\n"):
        return {}
    end = raw.find("\n---\n", 4)
    if end == -1:
        if raw.endswith("\n---"):
            end = len(raw) - 4
        else:
            return {}
    block = raw[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def ascii_slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    return normalized


def normalize_text(value: str) -> str:
    value = unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def html_fragment_to_lines(fragment: str) -> list[str]:
    text = fragment
    replacements = {
        r"<br\s*/?>": "\n",
        r"</p>": "\n",
        r"</div>": "\n",
        r"</section>": "\n",
        r"</h1>": "\n",
        r"</h2>": "\n",
        r"</h3>": "\n",
        r"</h4>": "\n",
        r"</li>": "\n",
        r"</ul>": "\n",
        r"</ol>": "\n",
        r"<li[^>]*>": "• ",
        r"<code[^>]*>(.*?)</code>": r"\1",
        r"<strong[^>]*>(.*?)</strong>": r"\1",
        r"<em[^>]*>(.*?)</em>": r"\1",
        r"<a[^>]*>(.*?)</a>": r"\1",
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", "", text)
    lines = [normalize_text(line) for line in text.splitlines()]
    return [line for line in lines if line]


def html_fragment_to_paragraphs(fragment: str) -> list[str]:
    paragraphs = [
        strip_html_text(match)
        for match in re.findall(r"<p[^>]*>(.*?)</p>", fragment, flags=re.IGNORECASE | re.DOTALL)
    ]
    return [paragraph for paragraph in paragraphs if paragraph]


def html_fragment_to_list(fragment: str) -> list[str]:
    items = [
        strip_html_text(match)
        for match in re.findall(r"<li[^>]*>(.*?)</li>", fragment, flags=re.IGNORECASE | re.DOTALL)
    ]
    return [item for item in items if item]


def strip_html_text(fragment: str) -> str:
    lines = html_fragment_to_lines(fragment)
    return " ".join(lines)


def parse_experience_html(fragment: str) -> list[ExperienceSection]:
    lines = html_fragment_to_lines(fragment)
    sections: list[ExperienceSection] = []
    current_title = ""
    current_org = ""
    current_bullets: list[str] = []

    def flush() -> None:
        nonlocal current_title, current_org, current_bullets
        if current_title:
            sections.append(
                ExperienceSection(
                    title=current_title,
                    organization=current_org,
                    bullets=current_bullets[:],
                )
            )
        current_title = ""
        current_org = ""
        current_bullets = []

    for line in lines:
        if line.startswith("• "):
            current_bullets.append(line[2:].strip())
            continue
        if current_title and current_bullets:
            flush()
        if not current_title:
            current_title = line
        elif not current_org:
            current_org = line
        else:
            current_bullets.append(line)
    flush()
    return sections


def extract_resume_json(html: str) -> dict:
    match = re.search(r"const\s+resumeContent\s*=\s*(\{.*?\});", html, flags=re.DOTALL)
    if not match:
        raise ValueError("Could not find resumeContent JSON in resume.html")
    return json.loads(match.group(1))


def parse_resume_source(path: Path) -> ResumeSource:
    data = extract_resume_json(read_text(path))

    def parse_language(lang: str) -> ResumeLanguageContent:
        section = data[lang]
        return ResumeLanguageContent(
            summary_paragraphs=html_fragment_to_paragraphs(section["summary_html"]),
            outcomes=html_fragment_to_list(section["outcomes_html"]),
            skills=html_fragment_to_list(section["skills_html"]),
            highlights=html_fragment_to_list(section["highlights_html"]),
            experience_sections=parse_experience_html(section["experience_html"]),
            experience_label=normalize_text(section.get("experience_label", "")),
            education_lines=html_fragment_to_lines(section["education_html"]),
            languages=html_fragment_to_list(section["languages_html"]),
        )

    return ResumeSource(en=parse_language("en"), fr=parse_language("fr"))


def first_group(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return strip_html_text(match.group(1)) if match else ""


def first_group_raw(pattern: str, text: str) -> str:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return match.group(1) if match else ""


def parse_projects(index_html: str) -> list[ProjectCase]:
    articles = re.findall(
        r'<article class="case-study[^"]*" id="([^"]+)">(.*?)</article>',
        index_html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    projects: list[ProjectCase] = []
    for case_id, block in articles:
        title = first_group(r"<h3>(.*?)</h3>", block)
        tags = [normalize_text(tag) for tag in re.findall(r'<span class="case-tag">(.*?)</span>', block)]
        preview = first_group(r'<div class="case-preview">.*?<p>(.*?)</p>', block)
        methods = first_group(r'<p class="case-meta"><strong>Methods:</strong>\s*(.*?)</p>', block)
        impact = first_group(r'<p class="impact-note"><strong>Impact:</strong>\s*(.*?)</p>', block)
        relevance = first_group(r'<p class="impact">Industry relevance:\s*(.*?)</p>', block)
        if title:
            projects.append(
                ProjectCase(
                    case_id=case_id,
                    title=title,
                    tags=tags,
                    preview=preview,
                    methods=methods,
                    impact=impact,
                    relevance=relevance,
                )
            )
    return projects


def dedupe_preserve_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        cleaned = normalize_text(item)
        if not cleaned:
            continue
        key = ascii_slug(cleaned).lower()
        if key in seen:
            continue
        seen.add(key)
        ordered.append(cleaned)
    return ordered


def parse_site_tools_methods(index_html: str) -> list[str]:
    skill_pills = [
        normalize_text(item)
        for item in re.findall(r'<span class="skill-pill">(.*?)</span>', index_html, flags=re.IGNORECASE | re.DOTALL)
    ]
    case_tags = [
        normalize_text(item)
        for item in re.findall(r'<span class="case-tag">(.*?)</span>', index_html, flags=re.IGNORECASE | re.DOTALL)
    ]
    method_blocks = re.findall(
        r'<p class="case-meta"><strong>Methods:</strong>\s*(.*?)</p>',
        index_html,
        flags=re.IGNORECASE | re.DOTALL,
    )
    method_items: list[str] = []
    for block in method_blocks:
        method_items.extend(normalize_text(part) for part in block.split(","))
    return dedupe_preserve_order([*skill_pills, *case_tags, *method_items])


def classify_tool_method(item: str) -> str:
    lowered = ascii_slug(item).lower()

    ml_keywords = (
        "scikit",
        "catboost",
        "gradient boosting",
        "gbdt",
        "reweighting",
        "feature",
        "domain adaptation",
        "train-test",
    )
    validation_keywords = (
        "validation",
        "calibration",
        "bias correction",
        "alignment",
        "monitoring",
        "diagnostic",
        "root-cause",
        "comparison",
        "pseudoexperiment",
        "simulation correction",
    )
    tools_keywords = (
        "python",
        "numpy",
        "pandas",
        "statsmodels",
        "matplotlib",
        "seaborn",
        "c/c++",
        "root / roofit",
        "geant4",
        "workflow automation",
        "scientific software",
        "framework integration",
        "gaudi-package",
    )

    if any(keyword in lowered for keyword in ml_keywords):
        return "ML"
    if any(keyword in lowered for keyword in validation_keywords):
        return "Validation"
    if any(keyword in lowered for keyword in tools_keywords):
        return "Tools"
    return "Methods"


def group_tools_methods_for_job(
    job: JobSpec, tools_methods: list[str], per_group_limit: int = 10
) -> list[tuple[str, list[str]]]:
    query = " ".join([job.company, job.role, job.title, job.fit, job.risk, *job.summary, *job.bullets])
    grouped: dict[str, list[tuple[int, int, str]]] = {group: [] for group in SKILL_GROUP_ORDER}

    for index, item in enumerate(tools_methods):
        group = classify_tool_method(item)
        score = text_score(item, query)
        if item in SKILL_KEYWORDS:
            for keyword in SKILL_KEYWORDS[item]:
                if ascii_slug(keyword).lower() in ascii_slug(query).lower():
                    score += 3
        grouped[group].append((score, index, item))

    selected_groups: list[tuple[str, list[str]]] = []
    for group in SKILL_GROUP_ORDER:
        ranked = sorted(grouped[group], key=lambda value: (-value[0], value[1]))
        selected = [item for _, _, item in ranked[:per_group_limit]]
        if len(ranked) > per_group_limit:
            selected.append("etc")
        if selected:
            selected_groups.append((group, selected))
    return selected_groups


def parse_site_source(path: Path) -> SiteSource:
    html = read_text(path)
    hero_copy_block = first_group_raw(r'<div class="hero-copy">(.*?)</div>', html)
    return SiteSource(
        positioning_title=first_group(r'<div class="closing-panel profile-positioning">.*?<h2>(.*?)</h2>', html),
        positioning_text=first_group(r'<div class="closing-panel profile-positioning">.*?<p>(.*?)</p>', html),
        hero_about=first_group(r'<p class="hero-about">(.*?)</p>', html),
        hero_copy=html_fragment_to_paragraphs(hero_copy_block),
        projects=parse_projects(html),
        tools_methods=parse_site_tools_methods(html),
    )


def detect_language(text: str) -> str:
    lowered = ascii_slug(text).lower()
    if re.search(r"\b(scientific|engineer|workflow|measurement|reliable|roles|software)\b", lowered):
        return "en"
    return "fr"


def parse_shortlist(path: Path) -> list[JobSpec]:
    markdown = read_text(path)
    bucket_match = re.search(
        r"##\s+Bucket A\b.*?(.*?)(?=\n##\s+Bucket B\b|\Z)",
        markdown,
        flags=re.DOTALL,
    )
    if not bucket_match:
        raise ValueError("Could not find Bucket A in shortlist markdown")
    bucket = bucket_match.group(1).strip()
    raw_jobs = re.split(r"(?=^### A\d+\.\s)", bucket, flags=re.MULTILINE)
    jobs: list[JobSpec] = []

    for raw_job in raw_jobs:
        block = raw_job.strip()
        if not block.startswith("### "):
            continue

        heading_match = re.match(r"###\s+(A\d+)\.\s+([^\n]+)", block)
        if not heading_match:
            continue

        code = heading_match.group(1)
        heading = heading_match.group(2)
        company, role = split_company_role(heading)
        links = [f"{label}: {url}" for label, url in re.findall(r"-\s+([^:\n]+):\s+\[[^\]]+\]\(([^)]+)\)", block)]
        fit = capture_markdown_field(block, "Pourquoi c'est un bon fit")
        risk = capture_markdown_field(block, "Risque principal")
        title = capture_code_block(block, "CV title")
        summary_block = capture_section(block, "Summary", "Top 6 bullets")
        summary = split_markdown_paragraphs(summary_block)
        bullets = [normalize_text(item) for item in re.findall(r"^\d+\.\s+(.+)$", block, flags=re.MULTILINE)]
        language = detect_language(" ".join([title, *summary, *bullets]))

        jobs.append(
            JobSpec(
                code=code,
                company=company,
                role=role,
                title=title,
                summary=summary,
                bullets=bullets,
                fit=fit,
                risk=risk,
                links=links,
                language=language,
            )
        )
    return jobs


def split_company_role(heading: str) -> tuple[str, str]:
    parts = re.split(r"\s+[—–-]\s+", heading, maxsplit=1)
    if len(parts) == 2:
        company = parts[0].strip()
        role = re.sub(r"\s*\([^)]*\)\s*$", "", parts[1].strip()).strip()
        return company, role
    return heading.strip(), ""


def capture_markdown_field(block: str, name: str) -> str:
    match = re.search(
        rf"-\s+{re.escape(name)}:\n\s+(.+?)(?=\n-\s+\S|\n#### |\n### |\Z)",
        block,
        flags=re.DOTALL,
    )
    return normalize_text(match.group(1)) if match else ""


def capture_code_block(block: str, heading: str) -> str:
    match = re.search(
        rf"####\s+{re.escape(heading)}[^\n]*\s+`([^`]+)`",
        block,
        flags=re.DOTALL,
    )
    if match:
        return normalize_text(match.group(1))
    match = re.search(
        rf"####\s+{re.escape(heading)}[^\n]*\s+(.*?)\n#### ",
        block,
        flags=re.DOTALL,
    )
    return normalize_text(match.group(1).replace("`", "")) if match else ""


def capture_section(block: str, start_heading: str, end_heading: str) -> str:
    match = re.search(
        rf"####\s+{re.escape(start_heading)}[^\n]*\s+(.*?)\n####\s+{re.escape(end_heading)}[^\n]*",
        block,
        flags=re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def job_key(job: JobSpec) -> str:
    normalized = f"{job.company}::{job.role}"
    normalized = normalized.replace("—", "-").replace("–", "-")
    normalized = re.sub(r"\s*-\s*", "-", normalized)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return ascii_slug(normalized).lower()


def split_markdown_paragraphs(block: str) -> list[str]:
    paragraphs = []
    for piece in re.split(r"\n\s*\n|  \n", block):
        cleaned = normalize_text(piece.replace("`", ""))
        if cleaned:
            paragraphs.append(cleaned)
    return paragraphs


def normalized_tokens(text: str) -> set[str]:
    ascii_text = ascii_slug(text).lower()
    tokens = re.findall(r"[a-z0-9]{3,}", ascii_text)
    return {token for token in tokens if token not in STOPWORDS}


def text_score(text: str, query: str) -> int:
    haystack = ascii_slug(text).lower()
    hay_tokens = normalized_tokens(text)
    score = 0
    for token in normalized_tokens(query):
        if token in hay_tokens:
            score += 2
        if token in haystack:
            score += 1
    return score


def choose_skills(job: JobSpec, skills: list[str], limit: int = 8) -> list[str]:
    query = " ".join([job.role, job.title, job.fit, job.risk, *job.summary, *job.bullets])
    scored: list[tuple[int, int, str]] = []
    for index, skill in enumerate(skills):
        score = text_score(skill, query)
        for keyword in SKILL_KEYWORDS.get(skill, ()):
            if ascii_slug(keyword).lower() in ascii_slug(query).lower():
                score += 3
        scored.append((score, -index, skill))
    selected = [skill for _, _, skill in sorted(scored, reverse=True)[:limit]]
    return selected


def select_experience_sections(job: JobSpec, sections: list[ExperienceSection]) -> list[ExperienceSection]:
    query = " ".join([job.role, job.title, job.fit, *job.summary, *job.bullets])
    selected_sections: list[ExperienceSection] = []
    for section in sections:
        scored_bullets = [
            (text_score(f"{section.title} {bullet}", query), idx, bullet)
            for idx, bullet in enumerate(section.bullets)
        ]
        shortlisted = sorted(scored_bullets, key=lambda item: (-item[0], item[1]))[:4]
        ordered = [bullet for _, _, bullet in sorted(shortlisted, key=lambda item: item[1])]
        selected_sections.append(
            ExperienceSection(
                title=section.title,
                organization=section.organization,
                bullets=ordered[:3] if ordered else section.bullets[:3],
            )
        )
    return selected_sections


def select_projects(job: JobSpec, projects: list[ProjectCase], limit: int = 3) -> list[ProjectCase]:
    query = " ".join([job.role, job.title, job.fit, *job.summary, *job.bullets])
    scored: list[tuple[int, ProjectCase]] = []
    for project in projects:
        combined = " ".join(
            [
                project.title,
                " ".join(project.tags),
                project.preview,
                project.methods,
                project.impact,
                project.relevance,
            ]
        )
        score = text_score(combined, query)
        lowered = ascii_slug(query).lower()
        if "validation" in lowered and project.case_id == "work-6":
            score += 6
        if "calibration" in lowered and project.case_id == "work-5":
            score += 6
        if "simulation" in lowered and project.case_id == "work-4":
            score += 6
        if ("modelisation" in lowered or "modeling" in lowered or "modelisation" in lowered) and project.case_id == "work-2":
            score += 3
        scored.append((score, project))
    ranked = [project for _, project in sorted(scored, key=lambda item: item[0], reverse=True)[:limit]]
    return ranked


def job_display_bullets(job: JobSpec) -> list[str]:
    override = JOB_EN_OVERRIDES.get(job.code)
    bullets = override["bullets"] if override and "bullets" in override else job.bullets
    return [bullet.replace("`", "") for bullet in bullets]


def job_display_fit(job: JobSpec) -> str:
    override = JOB_EN_OVERRIDES.get(job.code)
    fit = override["fit"] if override and "fit" in override else job.fit
    return fit.replace("`", "")


def job_personal_intro(job: JobSpec) -> list[str]:
    override = JOB_FR_INTRO_OVERRIDES.get(job.code)
    if override:
        return override
    return [paragraph.replace("`", "") for paragraph in job.summary]


def format_experience_timeline(label: str) -> str:
    cleaned = normalize_text(label)
    bracket_match = re.search(r"\[(.+)\]", cleaned)
    if bracket_match:
        cleaned = bracket_match.group(1)
    cleaned = cleaned.replace("(", "| ").replace(")", "")
    cleaned = re.sub(r"\s+\|\s+", " | ", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned


def truncate_text(text: str, limit: int) -> str:
    cleaned = normalize_text(text)
    if len(cleaned) <= limit:
        return cleaned
    cut = cleaned[: limit - 1].rsplit(" ", 1)[0].strip()
    return f"{cut}…"


def display_url(url: str) -> str:
    cleaned = normalize_text(url)
    cleaned = re.sub(r"^https?://", "", cleaned)
    return cleaned.rstrip("/")


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_styles(primary: colors.Color, light: colors.Color) -> StyleSheet1:
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="Name",
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=26,
            textColor=primary,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="RoleTitle",
            fontName="Helvetica-Bold",
            fontSize=11.2,
            leading=13.5,
            textColor=colors.HexColor("#243447"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="HeaderMeta",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.8,
            textColor=colors.HexColor("#4E6072"),
            alignment=TA_RIGHT,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionLabel",
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=11.5,
            textColor=primary,
            spaceAfter=5,
            textTransform=None,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodySmall",
            fontName="Helvetica",
            fontSize=8.9,
            leading=11.8,
            textColor=colors.HexColor("#243447"),
            spaceAfter=5.5,
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyTight",
            fontName="Helvetica",
            fontSize=8.4,
            leading=10.8,
            textColor=colors.HexColor("#243447"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="JobBullet",
            parent=styles["BodySmall"],
            leftIndent=10,
            firstLineIndent=-6,
            bulletIndent=0,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CardTitle",
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=colors.HexColor("#1F2D3D"),
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Muted",
            fontName="Helvetica-Oblique",
            fontSize=8.2,
            leading=10.3,
            textColor=colors.HexColor("#596B7E"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Banner",
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=11.2,
            textColor=colors.white,
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Tag",
            fontName="Helvetica",
            fontSize=7.8,
            leading=9.2,
            textColor=colors.HexColor("#405266"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="FooterSmall",
            fontName="Helvetica",
            fontSize=8.1,
            leading=10.4,
            textColor=colors.HexColor("#5A6A78"),
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="RightBody",
            fontName="Helvetica",
            fontSize=8.2,
            leading=10.4,
            textColor=colors.HexColor("#243447"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BaseNormal",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11.5,
            textColor=colors.HexColor("#243447"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TargetLine",
            fontName="Helvetica-Bold",
            fontSize=8.8,
            leading=11,
            textColor=primary,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="InfoBlockTitle",
            fontName="Helvetica-Bold",
            fontSize=8.4,
            leading=10.2,
            textColor=primary,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ProjectBody",
            fontName="Helvetica",
            fontSize=8.5,
            leading=10.9,
            textColor=colors.HexColor("#243447"),
            spaceAfter=3,
        )
    )
    styles._job_primary = primary
    styles._job_light = light
    return styles


def card(flowables: list, primary: colors.Color, light: colors.Color, padding: int = 8) -> Table:
    table = Table([[flowables]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), light),
                ("BOX", (0, 0), (-1, -1), 0.6, primary),
                ("INNERPADDING", (0, 0), (-1, -1), padding),
                ("LEFTPADDING", (0, 0), (-1, -1), padding),
                ("RIGHTPADDING", (0, 0), (-1, -1), padding),
                ("TOPPADDING", (0, 0), (-1, -1), padding),
                ("BOTTOMPADDING", (0, 0), (-1, -1), padding),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def banner(text: str, primary: colors.Color) -> Table:
    content = Paragraph(escape_xml(text), getSampleStyleSheet()["BodyText"])
    style = ParagraphStyle(
        "BannerText",
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=TA_CENTER,
    )
    content = Paragraph(escape_xml(text), style)
    table = Table([[content]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), primary),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def make_bullet_paragraph(text: str, styles: StyleSheet1, style_name: str = "JobBullet") -> Paragraph:
    return Paragraph(f"• {escape_xml(text)}", styles[style_name])


def skills_table(skills: list[str], styles: StyleSheet1, primary: colors.Color) -> Table:
    rows = []
    for index in range(0, len(skills), 2):
        left = Paragraph(escape_xml(skills[index]), styles["Tag"])
        right_text = skills[index + 1] if index + 1 < len(skills) else ""
        right = Paragraph(escape_xml(right_text), styles["Tag"]) if right_text else ""
        rows.append([left, right])

    table = Table(rows, colWidths=[78 * mm, 78 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                ("BOX", (0, 0), (-1, -1), 0.5, primary),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D2DDE7")),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def personal_info_flowables(labels: dict[str, str], profile: dict[str, str], styles: StyleSheet1) -> list:
    items = [
        (labels["email"], profile.get("email", "")),
        (labels["city"], profile.get("location", "")),
        (labels["phone"], profile.get("phone", "")),
        (labels["portfolio"], display_url(profile.get("homepage", ""))),
    ]
    flowables = []
    for label, value in items:
        flowables.append(Paragraph(f"<b>{escape_xml(label)}:</b>", styles["FooterSmall"]))
        flowables.append(Paragraph(escape_xml(value), styles["FooterSmall"]))
    return flowables


def education_languages_flowables(
    labels: dict[str, str], resume_content: ResumeLanguageContent, styles: StyleSheet1
) -> list:
    flowables = [Paragraph(f"<b>{escape_xml(labels['education'])}</b>", styles["FooterSmall"])]
    flowables.extend(Paragraph(escape_xml(line), styles["FooterSmall"]) for line in resume_content.education_lines)
    flowables.append(Spacer(1, 3))
    flowables.append(Paragraph(f"<b>{escape_xml(labels['languages'])}</b>", styles["FooterSmall"]))
    flowables.extend(Paragraph(escape_xml(line), styles["FooterSmall"]) for line in resume_content.languages)
    return flowables


def section_rule(title: str, styles: StyleSheet1, primary: colors.Color) -> Table:
    table = Table([[Paragraph(escape_xml(title), styles["SectionLabel"])]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.8, primary),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def build_document(
    job: JobSpec,
    resume: ResumeSource,
    site: SiteSource,
    profile: dict[str, str],
    output_path: Path,
) -> None:
    palette = ACCENTS.get(job.code, ACCENTS["A1"])
    primary = palette["primary"]
    light = palette["light"]
    styles = build_styles(primary, light)
    labels = PROJECT_LABELS["en"]
    resume_content = resume.en
    display_bullets = job_display_bullets(job)
    display_fit = job_display_fit(job)
    personal_intro = job_personal_intro(job)
    grouped_tools_methods = group_tools_methods_for_job(job, site.tools_methods, per_group_limit=10)
    selected_experience = select_experience_sections(job, resume_content.experience_sections)
    selected_projects = select_projects(job, site.projects, limit=3)
    experience_timeline = format_experience_timeline(resume_content.experience_label)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=13 * mm,
        rightMargin=13 * mm,
        topMargin=12 * mm,
        bottomMargin=11 * mm,
        title=f"{profile.get('name', 'Yingrui Hou')} - {job.company}",
        author=profile.get("name", "Yingrui Hou"),
    )

    story = []
    header_left = [
        Paragraph(escape_xml(profile.get("name", "Yingrui Hou")), styles["Name"]),
        Paragraph(escape_xml(job.title), styles["RoleTitle"]),
        Paragraph(f"{escape_xml(labels['target'])}: {escape_xml(job.company)} | {escape_xml(job.role)}", styles["TargetLine"]),
    ]
    header_right = [
        Paragraph(escape_xml(profile.get("email", "")), styles["HeaderMeta"]),
        Paragraph(escape_xml(profile.get("phone", "")), styles["HeaderMeta"]),
        Paragraph(escape_xml(profile.get("location", "")), styles["HeaderMeta"]),
        Paragraph(escape_xml(display_url(profile.get("homepage", ""))), styles["HeaderMeta"]),
    ]
    header = Table([[header_left, header_right]], colWidths=[109 * mm, 69 * mm])
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LINEBELOW", (0, 0), (-1, -1), 1.0, primary),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.extend([header, Spacer(1, 8)])

    story.extend([section_rule(labels["intro"], styles, primary), Spacer(1, 4)])
    story.extend(Paragraph(escape_xml(paragraph), styles["BodySmall"]) for paragraph in personal_intro)

    story.extend([Spacer(1, 4), section_rule(labels["fit"], styles, primary), Spacer(1, 4)])
    story.extend(make_bullet_paragraph(bullet, styles) for bullet in display_bullets)
    if display_fit:
        story.extend([Spacer(1, 1), Paragraph(escape_xml(truncate_text(display_fit, 220)), styles["Muted"])])

    education_text = "<br/>".join(escape_xml(line) for line in resume_content.education_lines)
    languages_text = "<br/>".join(escape_xml(line) for line in resume_content.languages)
    page_one_info = Table(
        [[
            [
                Paragraph(escape_xml(labels["education"]), styles["InfoBlockTitle"]),
                Paragraph(education_text, styles["FooterSmall"]),
            ],
            [
                Paragraph(escape_xml(labels["languages"]), styles["InfoBlockTitle"]),
                Paragraph(languages_text, styles["FooterSmall"]),
            ],
        ]],
        colWidths=[98 * mm, 80 * mm],
    )
    page_one_info.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), light),
                ("LINEABOVE", (0, 0), (-1, -1), 0.8, primary),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.extend([Spacer(1, 8), page_one_info])

    story.extend([Spacer(1, 6), section_rule(labels["skills"], styles, primary), Spacer(1, 4)])
    for group_name, items in grouped_tools_methods:
        group_line = f"<b>{escape_xml(group_name)}:</b> {escape_xml(' | '.join(items))}"
        story.append(Paragraph(group_line, styles["BodyTight"]))

    story.append(Spacer(1, 8))

    story.extend([section_rule(labels["experience"], styles, primary), Spacer(1, 4)])
    if experience_timeline:
        story.extend([Paragraph(escape_xml(experience_timeline), styles["Muted"]), Spacer(1, 2)])
    for section in selected_experience:
        story.append(
            KeepTogether(
                [
                    Paragraph(escape_xml(section.title), styles["CardTitle"]),
                    Paragraph(escape_xml(section.organization), styles["Muted"]),
                ]
            )
        )
        story.extend(make_bullet_paragraph(bullet, styles) for bullet in section.bullets)
        story.append(Spacer(1, 5))

    story.extend([Spacer(1, 3), section_rule(labels["projects"], styles, primary), Spacer(1, 4)])
    for project in selected_projects:
        story.extend(
            [
                Paragraph(escape_xml(project.title), styles["CardTitle"]),
                Paragraph(escape_xml(" | ".join(project.tags[:4])), styles["Muted"]),
            ]
        )
        preview = truncate_text(project.preview, 190)
        if preview:
            story.append(Paragraph(escape_xml(preview), styles["ProjectBody"]))
        methods = truncate_text(project.methods, 130)
        impact = truncate_text(project.impact, 150)
        relevance = truncate_text(project.relevance, 130)
        if methods:
            story.append(
                Paragraph(f"<b>{escape_xml(labels['methods'])}:</b> {escape_xml(methods)}", styles["ProjectBody"])
            )
        if impact:
            story.append(
                Paragraph(f"<b>{escape_xml(labels['impact'])}:</b> {escape_xml(impact)}", styles["ProjectBody"])
            )
        if relevance:
            story.append(
                Paragraph(f"<b>{escape_xml(labels['relevance'])}:</b> {escape_xml(relevance)}", styles["ProjectBody"])
            )
        story.append(Spacer(1, 6))

    def draw_footer(canvas, document) -> None:  # noqa: ANN001
        canvas.saveState()
        canvas.setStrokeColor(primary)
        canvas.setLineWidth(0.6)
        canvas.line(document.leftMargin, 10 * mm, A4[0] - document.rightMargin, 10 * mm)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(colors.HexColor("#5A6A78"))
        page_text = f"{profile.get('name', 'Yingrui Hou')} | {job.company} | {canvas.getPageNumber()}"
        canvas.drawRightString(A4[0] - document.rightMargin, 6.5 * mm, page_text)
        canvas.restoreState()

    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)


def main() -> None:
    args = parse_args()
    profile = parse_front_matter(args.profile)
    resume_source = parse_resume_source(args.resume_html)
    site_source = parse_site_source(args.index_html)
    excluded_keys = {
        job_key(job)
        for shortlist in args.exclude_shortlist
        for job in parse_shortlist(shortlist)
    }
    jobs: list[JobSpec] = []
    seen_keys = set(excluded_keys)
    for shortlist in args.shortlist:
        for job in parse_shortlist(shortlist):
            key = job_key(job)
            if key in seen_keys:
                continue
            seen_keys.add(key)
            jobs.append(job)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for job in jobs:
        output_path = args.output_dir / job.filename
        build_document(job, resume_source, site_source, profile, output_path)
        print(output_path)


if __name__ == "__main__":
    main()
