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
**Calibrated a classifier’s estimated mistag probabilities for the Bs → φγ analysis, using real-data reference channels and a simulation cross-check.**

### Problem and scope
The model returned a flavour decision (−1, 0 or +1) and an estimated mistag probability between 0 and 0.5. It had been trained on simulated samples of a particular process. Differences between simulation and real collision data required calibration. The mismatch depends on the target process, so the calibration cannot be assumed to transfer universally.

### Personal contribution
- Selected **B+ → J/ψ K and Bs → Ds π** as calibration channels based on the tagger and target-signal characteristics.
- Checked key kinematic distributions before calibration, using **gradient-boosting reweighting** when needed to align the reference samples with the signal, because the model response depends on event kinematics.
- Used reference-flavour information from reconstructed final-state charges and quantum numbers. Compared reference information with model decisions, then **fitted the relationship between predicted and observed mistag probabilities** and applied it to the signal analysis.
- **Cross-checked the data-driven result using signal simulation reweighted to the expected data kinematics. The mistag estimates agreed within uncertainties**, supporting the calibration’s reliability for this analysis.
- Participated in model-construction and training discussions for later calibration and validation; did not train the model.

### Transfer to engineering
Selecting relevant reference data, addressing distribution differences before transferring a calibration, fitting a correction to model confidence and corroborating it with simulation. The outcome supports the specific analysis; it does not establish universal calibration or zero residual bias.
