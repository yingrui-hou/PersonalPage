# PersonalPage

Free personal portfolio site for GitHub Pages.

## Files

- `index.html`: main portfolio page
- `styles.css`: site styling
- `portfolio.md`: source content in Markdown

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

Open `index.html` directly in a browser, or run a simple static server such as:

```bash
python3 -m http.server
```
