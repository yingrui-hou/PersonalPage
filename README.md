# PersonalPage

Free personal portfolio site for GitHub Pages.

## Files

- `index.html`: main portfolio page
- `styles.css`: site styling
- `portfolio.md`: source content in Markdown
- `content/shared/profile.md`: shared personal info used by both pages
- `content/index/*.md`: homepage content modules
- `content/resume/en/*.md`: English resume content modules
- `content/resume/fr/*.md`: French resume content modules
- `content/templates/*.md`: copyable module templates
- `content/MODULES.md`: module format and mapping guide
- `scripts/build_site.py`: builds `index.html` and `resume.html` from the markdown modules

## Editing workflow

1. Find the module you want to change in `content/`.
2. If you are adding a new block, start from the matching file in `content/templates/`.
3. Keep front matter keys consistent with `content/MODULES.md`.
4. Run `python3 scripts/build_site.py` to regenerate `index.html` and `resume.html`.
5. Preview locally with a static server before pushing.

## Publish on GitHub Pages

1. Push this repository to GitHub.
2. In GitHub, open `Settings` -> `Pages`.
3. Under `Build and deployment`, set:
   - `Source`: `Deploy from a branch`
   - `Branch`: `main` and `/ (root)`
4. Save. GitHub will publish the site in a minute or two.

If you name the repository `<your-github-username>.github.io`, your site will be published at the root domain:

`https://<your-github-username>.github.io/`

Otherwise it will be published as a project page. For this repository, the published URL is:

`https://yingrui-hou.github.io/PersonalPage/`

## Recommended edits before publishing

- Replace or expand the intro text in `index.html` if you want a more specific job target.
- Add your email, LinkedIn, CV link, and GitHub profile in the hero area.
- If you want recruiters to see concrete proof, add one section with:
  - tools used (`Python`, `ROOT`, `XGBoost`, `pandas`, etc.)
  - data scale
  - measurable results

## Local preview

After updating any module, rebuild the generated pages:

```bash
python3 scripts/build_site.py
```

Then preview locally with a static server:

```bash
python3 -m http.server
```
