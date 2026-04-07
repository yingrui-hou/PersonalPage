import { loadModule, renderCaseStudy, renderMarkdown, renderSkillPills, renderTopbarLinks } from "./content-loader.js";

const WORK_MODULES = [
  "content/index/work-1.md",
  "content/index/work-2.md",
  "content/index/work-3.md",
  "content/index/work-4.md",
  "content/index/work-5.md",
];

async function initIndexPage() {
  const modules = await Promise.all([
    loadModule("content/shared/profile.md"),
    loadModule("content/index/intro.md"),
    loadModule("content/index/seeking.md"),
    loadModule("content/index/skills.md"),
    loadModule("content/index/overview.md"),
    loadModule("content/index/positioning.md"),
    ...WORK_MODULES.map((path) => loadModule(path)),
  ]);

  const [profile, intro, seeking, skills, overview, positioning, ...works] = modules;

  renderTopbar(profile.attributes);
  renderIntro(intro);
  renderSeeking(seeking);
  renderSkillPills(document.getElementById("skills-module"), skills.body);
  renderOverview(overview, works);
  renderSelectedWork(works);
  renderPositioning(positioning);
}

function renderTopbar(profile) {
  const brand = document.getElementById("profile-name-link");
  const links = document.getElementById("topbar-links");

  if (brand) {
    brand.textContent = profile.name;
  }

  if (links) {
    links.innerHTML = renderTopbarLinks(profile);
  }
}

function renderIntro(module) {
  const container = document.getElementById("intro-module");
  if (!container) {
    return;
  }

  container.innerHTML = `
    <p class="eyebrow">${module.attributes.eyebrow || "Personal Introduction"}</p>
    <h1>${module.attributes.title || ""}</h1>
    <p class="hero-about">${module.attributes.about || ""}</p>
    <div class="hero-copy">${renderMarkdown(module.body)}</div>
  `;
}

function renderSeeking(module) {
  const container = document.getElementById("seeking-module");
  if (!container) {
    return;
  }

  const paragraphs = renderMarkdown(module.body).replace(/<\/?p>/g, "");
  container.innerHTML = paragraphs;
}

function renderOverview(module, works) {
  const container = document.getElementById("overview-module");
  const mapLabel = document.getElementById("work-map-label");
  const mapList = document.getElementById("work-map-list");

  if (container) {
    container.innerHTML = `
      <p class="eyebrow">${module.attributes.eyebrow || "Overview"}</p>
      <h2>${module.attributes.title || ""}</h2>
      <div class="toc-copy">${renderMarkdown(module.body)}</div>
    `;
  }

  if (mapLabel) {
    mapLabel.textContent = module.attributes.map_label || "Selected Work Map";
  }

  if (mapList) {
    mapList.innerHTML = works
      .map(
        (work, index) =>
          `<li><a href="#work-${index + 1}">${work.attributes.title || `Work ${index + 1}`}</a></li>`,
      )
      .join("");
  }
}

function renderSelectedWork(works) {
  const grid = document.getElementById("selected-work-grid");
  if (!grid) {
    return;
  }

  grid.innerHTML = works.map((work, index) => renderCaseStudy(work, index)).join("");
}

function renderPositioning(module) {
  const container = document.getElementById("positioning-module");
  if (!container) {
    return;
  }

  container.innerHTML = `
    <p class="eyebrow">${module.attributes.eyebrow || "Positioning"}</p>
    <h2>${module.attributes.title || ""}</h2>
    ${renderMarkdown(module.body)}
  `;
}

initIndexPage().catch((error) => {
  console.error(error);
});
