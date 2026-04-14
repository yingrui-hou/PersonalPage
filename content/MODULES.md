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
  This file now drives both:
  - homepage `Skills & Tools`
  - resume `Skills` section
  The French resume uses the same source list through a translation map in `scripts/build_site.py`.

- `content/index/overview.md`
  Controls the right-side overview panel and the `Selected Work Map` label.

- `content/index/outcomes.md`
  Controls the short `Selected Outcomes` proof block on the homepage.

- `content/index/additional-methods.md`
  Controls the secondary homepage section used for more statistical or academic case studies.

- `content/index/work-*.md`
  One file per case study.
  Any number of `work-*.md` files can be used.
  Required front matter:
  - `number`
  - `title`
  - `tags`
  - `methods`
  - `impact`
  - `industry`
  Optional:
  - `evidence_title`
  - `homepage_order` to control homepage display order without renaming files
  - `homepage_group: secondary` to move a case into the secondary homepage grouping
  - `collapsible: true` to show only title, tags, summary, and preview image until the reader clicks `Read more`
  - `homepage: false` to keep a work file in the repo but hide it from the homepage
  Body structure:
  - short intro paragraph
  - bullet list
  - optional standalone Markdown image lines such as `![Alt text](assets/example.png)` or `![Alt text](assets/example.png "Caption")`
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
- `outcomes.md`
- `education.md`
- `skills.md`
  Currently not used for rendering. Resume skills are generated from `content/index/skills.md`.
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
