# Review of `CV_YingruiHou_DS.pdf`

Source file: `/Users/hou/Projects/PersonalPage/CV_related/output/pdf/CV_YingruiHou_DS.pdf`

Overall assessment:
- Current level is strong enough to send.
- Approximate fit score: `8/10` for Michelin `IS & Digital`, higher for `R&D data / validation` roles.
- Main issue is no longer profile direction, but recruiter readability and page efficiency.

## Priority Fixes

### 1. Second page does not add enough signal

Problem:
- The `Target Roles` section repeats what is already stated in the summary.
- Page 2 looks sparse, which weakens first-pass recruiter impression.

Recommended changes:
- Remove `Target Roles`, or compress it into a single line on page 1.
- Use page 2 only if it adds real evidence.
- If keeping 2 pages, replace the empty space with one of:
  - quantified outcomes,
  - tools/environment,
  - one more concrete project,
  - selected achievements with measurable impact.

Best practical option:
- Try to compress the CV into one page.

### 2. First experience bullets are still too research-specific

Problem:
- Terms such as `weak-signal extraction`, `latent parameters`, and `unbinned inference` are technically accurate, but too academic for HR screening.
- A recruiter in `IS & Digital` may not classify the profile quickly enough.

Recommended changes:
- Rewrite the first 3-4 bullets in more standard applied data science language.
- Prioritize wording around:
  - noisy data,
  - model validation,
  - bias correction,
  - monitoring,
  - anomaly detection,
  - dataset shift,
  - decision support.

Example direction:
- `Built reusable Python/C++ workflows to analyse noisy measurement data, validate model behaviour, and support reliable downstream decisions.`
- `Developed calibration and bias-correction workflows to improve model reliability under sample mismatch and imperfect observation conditions.`
- `Built monitoring and diagnostic pipelines to detect anomalies, compare expected vs observed behaviour, and support root-cause analysis.`

### 3. Skills section can be optimized for recruiter keyword scanning

Problem:
- The current skills section is cleaner than before, but still grouped too broadly.
- Some strong recruiter keywords are not visible early enough.

Recommended changes:
- Put the most market-recognizable skills first.
- Keep niche scientific tools, but move them later.

Suggested order:
- `Python, Statistical Modelling, Model Validation, Calibration, Monitoring`
- `scikit-learn, pandas, NumPy, statsmodels, CatBoost`
- `Anomaly Detection, Bias Correction, Decision-Support Modelling`
- `C/C++, Linux, Workflow Automation`
- `ROOT / RooFit, Geant4`

Note:
- Only keep keywords that you can confidently defend in interview discussion.

### 4. Education section would be easier to scan with years

Problem:
- Degrees are listed without dates.
- This makes the timeline slightly harder to read.

Recommended changes:
- Add graduation years or year ranges for each degree.

Example:
- `PhD in Particle Physics, University of Chinese Academy of Sciences, YYYY-YYYY`
- `BSc in Applied Physics, China University of Mining and Technology, YYYY-YYYY`

## Suggested Editing Plan

If only one round of edits is planned, focus on these items in order:

1. Compress or redesign page 2.
2. Rewrite the first 3-4 experience bullets in more recruiter-readable language.
3. Reorder and densify the skills section.
4. Add years to education.

## Positioning Reminder

This CV is strongest for roles such as:
- Applied Data Science
- Model Validation / Monitoring
- Analytics for Complex Measurement Data
- Industrial Data Science for physical or measurement systems

It is less suited to:
- generic business analytics,
- traditional enterprise IT support,
- purely software-platform roles with no modelling or validation component.

## Final Recommendation

This CV is already usable for outreach and applications, especially if the role sits between:
- applied data science,
- validation / monitoring,
- industrial or physical-system data.

However, one more refinement pass would improve recruiter response rate, especially for Michelin `IS & Digital`.
