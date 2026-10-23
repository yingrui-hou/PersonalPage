---
number: 03
homepage_order: 1
collapsible: true
title: ML under dataset shift
tags: CatBoost | Reweighting | Cross-validation
methods: control-sample checks, feature correlations, gradient-boosting reweighting, ROC/AUC and precision-oriented threshold scans
impact: connected data quality, model selection and the operating threshold to the precision objective of a rare-signal measurement.
industry: Applied ML | Dataset Shift | Decision Optimisation
---
Trained a CatBoost classifier to select rare signals, aligning simulated training data with measurements and choosing a threshold for the measurement objective.

### Problem
Training data combined simulated signals and background from real measurements. Distribution differences and limited labelled samples required careful validation.

### My contribution
- Selected features using domain knowledge, correlation checks and feature importance.
- Used reference measurements and hep_ml reweighting to address simulation–data differences before training.
- Applied five-fold validation for feature selection and hyperparameter tuning; compared training and test responses using KS diagnostics.
- Scanned the operating threshold with `S / sqrt(S + B)`, using expected signal and background counts derived from fitted yields and selection efficiencies.

### Validation and result
Applied the selected threshold to the analysis data and checked background suppression. Performance estimates came from the five-fold development validation; no additional untouched labelled holdout was available. Threshold efficiencies used pooled training and test events after compatible KS checks. These checks do not establish an independent final generalisation estimate.

### Figures

![Background veto performance](assets/selected-work/work-3/bkg_veto_performance.png "The displayed Run 1 comparison shows lower background after BDT selection, with the signal peak retained. LHCb unofficial study plot; no numerical improvement is inferred from the image.")
![Train-test GBDT response comparison](assets/selected-work/work-3/train-test.png "Training and test score distributions broadly agree for both classes in the displayed diagnostic; this is an overtraining check, not a guarantee of independent evaluation.")
![Feature importance ranking](assets/selected-work/work-3/feature_importance.png "Feature importance was used with separation diagnostics to simplify the model.")
