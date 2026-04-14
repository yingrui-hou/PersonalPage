---
number: 02
homepage_order: 6
collapsible: true
title: Time-Series Inference
tags: Time-Series Modelling | Bias Correction | Calibration | Joint Fitting
methods: acceptance modelling, resolution calibration, custom fit components, joint fitting
impact: converted a bias-sensitive latent-dynamics problem into a controlled inference workflow with dataset-specific corrections.
industry: Durability Modelling | State Estimation | Latent-Dynamics Inference
---
**Built a bias-corrected time-series inference workflow for data affected by selection effects, detector resolution, and sample mismatch.**

### Problem
The core problem was to infer latent time-dependent behaviour from observations distorted by selection effects, finite resolution, and data-simulation mismatch. Without explicit correction, those effects would bias the inferred dynamics rather than just broaden the uncertainty.

![Reconstruction effect on time distribution](assets/selected-work/work-2/time_rec_eff.png "Reconstruction effects reduce sensitivity to the oscillatory time structure.")

### Workflow
![Workflow of the analysis](assets/selected-work/work-2/workflow.png "Workflow used to extract latent observables from raw data.")
- Modelled acceptance and resolution explicitly instead of absorbing reconstruction effects into a single nuisance term.
- Estimated Run 1 and Run 2 corrections separately to avoid over-sharing assumptions across datasets with different operating conditions.
- Matched signal and control samples through GB reweighting before building acceptance corrections, and implemented reusable fit components for mass, lifetime, efficiency, and resolution modelling.

### Result
- Converted a bias-sensitive time-series problem into a controlled inference workflow with dataset-specific corrections and auditable assumptions.
- Propagated residual mismodelling as quantified uncertainty rather than hiding it inside nominal fit parameters, which made the method reusable across datasets and reviews.
