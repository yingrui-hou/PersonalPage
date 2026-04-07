# Content Modules

This site is driven by Markdown modules, but `index.html` and `resume.html` are generated with full content.

## Shared data

- `content/shared/profile.md`
  Used by both `index.html` and `resume.html`.
  Keep these keys in front matter:
  - `name`
  - `location`
  - `email`
  - `phone`
  - `linkedin`
  - `orcid`
  - `personal_gitlab`
  - `cern_gitlab`
  - `audio`

## Homepage modules

- `content/index/intro.md`
  Controls:
  - eyebrow
  - hero title
  - short intro paragraph
  - supporting body copy

- `content/index/seeking.md`
  Controls the short text under `Seeking`.

- `content/index/skills.md`
  Use one bullet per skill/tool.

- `content/index/overview.md`
  Controls the right-side overview panel and the `Selected Work Map` label.

- `content/index/work-1.md` to `content/index/work-5.md`
  One file per case study.
  Required front matter:
  - `number`
  - `title`
  - `tags`
  - `methods`
  - `impact`
  - `industry`
  Optional:
  - `evidence_title`
  Body structure:
  - short intro paragraph
  - bullet list
  - optional `## Evidence` section with bullets

- `content/index/positioning.md`
  Controls the closing block at the bottom of the homepage.

## Resume modules

Each language has its own directory:
- `content/resume/en`
- `content/resume/fr`

Files:
- `shell.md`
  Labels, metadata, and UI strings in front matter.
- `summary.md`
- `education.md`
- `skills.md`
- `languages.md`
- `highlights.md`
- `experience.md`

## Templates

Copy from `content/templates/` when creating a new module:
- `profile.template.md`
- `index-section.template.md`
- `index-work.template.md`
- `resume-shell.template.md`
- `resume-section.template.md`

## Editing notes

- After changing any module, rebuild the generated HTML files:

```bash
python3 scripts/build_site.py
```

- Front matter must be wrapped in:

```md
---
key: value
---
```

- Multi-value front matter currently uses ` | ` as a separator.
  Example:

```md
tags: XGBoost | Reweighting | Feature Validation
```

- Preview locally with a static server after rebuilding:

```bash
python3 -m http.server
```
