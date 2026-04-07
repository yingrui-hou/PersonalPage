import {
  loadModule,
  renderMarkdown,
  renderResumeContact,
} from "./content-loader.js";

const RESUME_MODULES = ["summary", "education", "skills", "languages", "highlights", "experience"];

const dom = {
  html: document.documentElement,
  descriptionMeta: document.querySelector('meta[name="description"]'),
  eyebrow: document.getElementById("resume-eyebrow"),
  name: document.getElementById("resume-name"),
  location: document.getElementById("resume-location"),
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
  langButtons: document.querySelectorAll("[data-lang-btn]"),
  nameAudioButton: document.getElementById("name-audio-button"),
  nameAudioSource: document.getElementById("name-audio-source"),
  nameAudio: document.getElementById("name-audio"),
};

let sharedProfile = null;

async function initResumePage() {
  sharedProfile = (await loadModule("content/shared/profile.md")).attributes;

  dom.name.textContent = sharedProfile.name;
  dom.location.textContent = sharedProfile.location;
  if (dom.nameAudioSource) {
    dom.nameAudioSource.src = sharedProfile.audio;
  }
  if (dom.nameAudio) {
    dom.nameAudio.load();
  }

  bindLanguageToggle();
  bindAudioButton();
  await renderResume(window.localStorage.getItem("resume-lang") || "en");
}

async function renderResume(lang) {
  const modules = await Promise.all([
    loadModule(`content/resume/${lang}/shell.md`),
    ...RESUME_MODULES.map((module) => loadModule(`content/resume/${lang}/${module}.md`)),
  ]);

  const [shell, summary, education, skills, languages, highlights, experience] = modules;

  dom.html.lang = lang;
  document.title = shell.attributes.title;
  if (dom.descriptionMeta) {
    dom.descriptionMeta.setAttribute("content", shell.attributes.description || "");
  }

  dom.eyebrow.textContent = shell.attributes.eyebrow;
  dom.backHomeLink.textContent = shell.attributes.back_home;
  dom.contactLabel.textContent = shell.attributes.contact_label;
  dom.educationLabel.textContent = shell.attributes.education_label;
  dom.skillsLabel.textContent = shell.attributes.skills_label;
  dom.languagesLabel.textContent = shell.attributes.languages_label;
  dom.highlightsLabel.textContent = shell.attributes.highlights_label;
  dom.experienceLabel.textContent = shell.attributes.experience_label;

  dom.summary.innerHTML = renderMarkdown(summary.body);
  dom.contact.innerHTML = renderResumeContact(sharedProfile, shell.attributes.phone_label);
  dom.education.innerHTML = renderMarkdown(education.body);
  dom.skills.innerHTML = renderMarkdown(skills.body);
  dom.languages.innerHTML = renderMarkdown(languages.body);
  dom.highlights.innerHTML = renderMarkdown(highlights.body);
  dom.experience.innerHTML = renderMarkdown(experience.body);

  bindPhoneReveal();
  updateLangButtons(lang);
  window.localStorage.setItem("resume-lang", lang);
}

function bindLanguageToggle() {
  dom.langButtons.forEach((button) => {
    button.addEventListener("click", () => {
      renderResume(button.dataset.langBtn).catch((error) => {
        console.error(error);
      });
    });
  });
}

function updateLangButtons(lang) {
  dom.langButtons.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.langBtn === lang);
  });
}

function bindPhoneReveal() {
  const phoneButton = dom.contact.querySelector("[data-reveal='phone']");
  if (!phoneButton) {
    return;
  }

  phoneButton.addEventListener("click", () => {
    phoneButton.textContent = phoneButton.dataset.value;
    phoneButton.classList.add("is-revealed");
    phoneButton.disabled = true;
  });
}

function bindAudioButton() {
  if (!dom.nameAudioButton || !dom.nameAudio) {
    return;
  }

  const setAudioState = (isPlaying) => {
    dom.nameAudioButton.classList.toggle("is-playing", isPlaying);
  };

  dom.nameAudio.addEventListener("play", () => {
    setAudioState(true);
  });

  dom.nameAudio.addEventListener("pause", () => {
    setAudioState(false);
  });

  dom.nameAudio.addEventListener("ended", () => {
    setAudioState(false);
  });

  dom.nameAudioButton.addEventListener("click", async () => {
    if (!dom.nameAudio.paused) {
      dom.nameAudio.pause();
      dom.nameAudio.currentTime = 0;
      return;
    }

    dom.nameAudio.currentTime = 0;

    try {
      await dom.nameAudio.play();
    } catch (error) {
      dom.nameAudioButton.disabled = true;
      dom.nameAudioButton.title = "Audio playback is blocked in this browser";
    }
  });
}

initResumePage().catch((error) => {
  console.error(error);
});
