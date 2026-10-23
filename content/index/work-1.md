---
number: 01
homepage_order: 8
homepage_group: secondary
collapsible: true
title: Weak-signal analysis
tags: Statistical Modelling | Uncertainty | Validation
methods: likelihood fitting, control-sample validation, reproducible yield workflows
impact: turned rare-signal extraction into a reproducible workflow with stability checks and auditable validation logic.
industry: Rare Event Analytics | Anomaly Detection | Weakly Labeled Systems
---
Developed reusable Python/C++ analysis software to estimate a weak signal within noisy, mixed data.

### Problem
The signal could not be identified reliably observation by observation. The analysis needed to estimate its contribution while accounting for background and measurement uncertainty.

### My contribution
- Built likelihood models to separate signal and background statistically.
- Automated data selection, signal estimation and reference-sample comparisons in Python/C++/ROOT.
- Checked variable correlations, fitted-parameter correlations and bias in repeated simulated experiments as part of each analysis’s uncertainty assessment.

### Validation and result
Compared fit stability across datasets and selection settings. The checks performed found no problematic dependence or bias; the workflow supported a dedicated measurement. This is evidence of the checks performed, rather than a claim that every possible bias was excluded.

### Figures

![Weak-signal mass fit case 2](assets/selected-work/work-1/BToVG.png "A narrow signal peak is recovered from dominant background through an explicit signal-plus-background fit.")
