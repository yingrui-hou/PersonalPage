---
number: 03
homepage_order: 7
collapsible: true
title: Domain Adaptation for ML
tags: GBDT | CatBoost | Reweighting | Feature Validation
methods: CatBoost training, train-test diagnostics, gradient-boosting reweighting
impact: improved downstream model reliability by treating dataset mismatch and overtraining checks as part of the production workflow.
industry: Domain Adaptation | Applied ML | Dataset Shift
---
**Built an ML validation and sample-alignment workflow in a shared analysis environment for noisy selection problems under dataset shift.**

![Background veto performance](assets/selected-work/work-3/bkg_veto_performance.png "Background is strongly reduced after applying the final GBDT selection model.")
![Train-test GBDT response comparison](assets/selected-work/work-3/train-test.png "Train and test response curves remain aligned for both classes, providing a direct overtraining check before threshold tuning.")
![Feature importance ranking](assets/selected-work/work-3/feature_importance.png "Feature-importance ranking of the final model after iterative refinement.")

### Problem
The ML problem was not only to classify noisy events, but to do so under dataset shift, where calibration and control samples do not naturally match the target sample. Without explicit validation and alignment, model scores would look good in training while degrading downstream inference.

### Workflow
- Trained CatBoost-based classifiers and used train-test response comparisons to check separation quality and overtraining behaviour before optimising thresholds.
- Reweighted calibration and control samples so their kinematics better matched the target signal sample before downstream inference.
- Treated reweighting, score validation, threshold scans, job configuration, and saved model outputs as one integrated workflow rather than isolated model-training steps.

### Result
- Improved downstream model reliability by making dataset mismatch and overtraining checks part of the production pipeline instead of optional diagnostics.
- Kept train and test response curves aligned for both classes, providing a direct validation that the classifier behaviour remained stable before selection tuning.
