---
number: 03
title: Machine Learning under Distribution Shift
tags: GBDT | XGBoost | Reweighting | Feature Validation
methods: GBDT, reweighting, feature-distribution validation
impact: reduced dataset mismatch and improved downstream model generalisation.
industry: domain adaptation, production ML, dataset shift handling.
evidence_title: Selected evidence from project work
---
Improved model robustness when training and real-world data did not follow the same distribution.

- Trained Gradient Boosted Decision Trees and compared feature distributions.
- Applied gradient-boosting-based reweighting before retraining.
- Validated alignment at the feature level to improve downstream generalisation.

## Evidence
- Train/test BDT response comparisons were used to verify score separation before downstream threshold tuning.
- Reweighting was treated as part of the validation loop whenever calibration and signal-like samples differed in kinematics.
