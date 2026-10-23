---
number: 05
homepage_order: 4
collapsible: true
title: Signal decomposition for sensor design
tags: Signal Processing | Simulation | Design Validation
methods: particle-dependent timing models, component fitting, correlation-based correction
impact: showed that PSD-derived shower fractions can improve reconstructed energy and help judge which detector materials remain usable for timing-based separation.
industry: Time-Resolved Sensing | Signal Decomposition | Measurement-System Design
---
Used measured pulse profiles and simulation to assess whether signal components could be separated reliably and improve energy reconstruction.

### Problem
Two candidate sensor materials produced overlapping light-pulse profiles. A reconstruction method could only work if the component signals remained distinguishable.

### My contribution
- Compared measured time profiles; engineers operated the measurement setup and sources.
- Used measured timing parameters in simulation and fitted the resulting signals with component templates.
- Checked parameter correlations and bias distributions to assess component recovery before applying an energy correction.

### Validation and result
The study supported the team’s choice of ZnWO4: BGO profiles were insufficiently separated at low energies. One representative simulated correction study reduced a resolution term by about a factor of two. This result concerns that simulation study, not a measured gain in a deployed sensor.

### Figures

![PSD-assisted resolution before and after correction](assets/selected-work/work-5/res_compare.png "Resolution improves after PSD-based correction across the tested energy range.")
![Time-profile fit used to recover shower fractions](assets/selected-work/work-5/time_fit.png "Representative time-profile fit showing the recovered EM fraction close to the injected value.")
