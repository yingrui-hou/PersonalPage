---
number: 09
homepage_order: 2
collapsible: true
title: Deep-Learning Model Calibration
tags: Deep Learning | Calibration | Real-Data Validation
methods: real-data model checks, flavour-tagging calibration, collaborative review
impact: calibrated and validated a flavour-tagging model for use in physics analysis.
industry: Applied ML | Model Validation | Scientific Data Analysis
---
**Calibrated a classifier’s estimated mistag probability against real data before its use in a physics measurement. The model performed flavour tagging.**

### Problem and scope
The model returned a flavour decision (−1, 0 or +1) and an estimated mistag probability between 0 and 0.5. It had been trained on simulated samples of a particular process. Differences between simulation and real collision data meant that the predicted mistag probabilities required calibration.

The mismatch depends on the target process: a calibration cannot be assumed to apply universally to other signals.

### Personal contribution
- Used a reference process whose flavour could be identified from reconstructed real data, comparing that reference with the model’s flavour decision to calibrate its estimated mistag probability.
- Applied data-driven mistag calibration for the signal analysis to address the influence of miscalibrated estimates on the downstream measurement.
- Participated in model-construction and training discussions to inform later calibration and validation; did not train the model.

### Transfer to engineering
Calibrating model confidence against observed outcomes, recognising simulation-to-data mismatch and checking the scope of a calibration before transferring it to another use case. This experience concerns calibration of model outputs for scientific analysis.
