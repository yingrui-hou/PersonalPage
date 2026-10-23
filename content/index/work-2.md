---
number: 02
homepage_order: 5
collapsible: true
title: Time-dependent modelling
tags: Bias Correction | Calibration | Model Fitting
methods: acceptance modelling, resolution calibration, custom fit components, joint fitting
impact: converted a bias-sensitive latent-dynamics problem into a controlled inference workflow with dataset-specific corrections.
industry: Durability Modelling | State Estimation | Latent-Dynamics Inference
---
Built a statistical modelling workflow to recover time-dependent behaviour from measurements affected by selection bias and limited sensor resolution.

### Problem
Observed time distributions differed from the underlying process because of data selection, measurement resolution and simulation–data mismatch.

### My contribution
- Modelled selection efficiency and measurement resolution explicitly.
- Estimated corrections separately for datasets collected under different operating conditions.
- Aligned reference and target samples through gradient-boosting reweighting; implemented reusable components for joint model fitting.

### Validation and result
Compared corrected simulation and measurements, and included residual model differences in the uncertainty assessment. The workflow made assumptions and dataset-specific corrections available for technical review.

### Figures

![Reconstruction effect on time distribution](assets/selected-work/work-2/time_rec_eff.png "Reconstruction effects reduce sensitivity to the oscillatory time structure.")
![Workflow of the analysis](assets/selected-work/work-2/workflow.png "Workflow used to extract latent observables from raw data.")
