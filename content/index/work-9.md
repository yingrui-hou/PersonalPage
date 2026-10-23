---
number: 09
homepage_order: 2
collapsible: true
title: Calibrating classifier confidence
tags: Calibration | Dataset Shift | Real-Data Validation
methods: real-data model checks, flavour-tagging calibration, collaborative review
impact: calibrated and validated a flavour-tagging model for use in physics analysis.
industry: Applied ML | Model Validation | Scientific Data Analysis
---
Calibrated a classifier’s estimated error probabilities using reference measurements, then cross-checked the correction with simulation.

### Problem
The classifier was trained on simulation whose distributions differed from real data. Its estimated error probabilities needed calibration for the target analysis.

### My contribution
- Selected suitable reference processes with identifiable classes and checked their relevance to the target data.
- Aligned key input distributions through gradient-boosting reweighting where needed.
- Fitted the relationship between predicted and observed misclassification probabilities and applied the correction to the target analysis.

### Validation and result
Cross-checked the data-based calibration using reweighted target simulation; error estimates agreed within uncertainties. My contribution covered calibration and validation, with participation in training discussions. I did not train this model. The calibration is specific to the target process and reference-data conditions.
