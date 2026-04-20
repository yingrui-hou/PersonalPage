---
number: 05
homepage_order: 2
collapsible: true
title: Pulse-Shape Discrimination for Energy Reconstruction
tags: Pulse Shape Discrimination | Detector Simulation | Time-Resolved Signal Analysis | Resolution Optimisation
methods: particle-dependent timing models, component fitting, correlation-based correction
impact: showed that PSD-derived shower fractions can improve reconstructed energy and help judge which detector materials remain usable for timing-based separation.
industry: Time-Resolved Sensing | Signal Decomposition | Measurement-System Design
---
**Built a PSD-oriented simulation and analysis workflow to extract shower composition from scintillation time profiles and use it to improve reconstructed energy.**

![PSD-assisted resolution before and after correction](assets/selected-work/work-5/res_compare.png "Resolution improves after PSD-based correction across the tested energy range.")

### Problem
The problem was to recover useful composition information from scintillation timing, instead of treating total light yield as a single undifferentiated signal. For the method to be credible, it also had to remain usable under realistic material behaviour, particle-dependent time constants, and the limited separation between EM-like and hadronic-like components.

### Workflow
- Generated `e/p/pi` simulation samples in two crystal-material candidates (`ZnWO4` and `BGO`) over `1 to 20 GeV` and first validated that the relevant correlation structure between deposited hadronic energy, EM fraction, and total energy remained stable across the energy range.
- Extended the simulation with scintillation timing, updating time constants dynamically by particle type and `dE/dx`, then fitted the time distributions with EM-, hadronic-, and proton-like components instead of relying only on total signal amplitude.
- Used the extracted fractions inside a correction workflow for reconstructed energy, then compared the resulting resolution before and after correction while checking which material choices stayed separable enough for PSD-based inference.

![Time-profile fit used to recover shower fractions](assets/selected-work/work-5/time_fit.png "Representative time-profile fit showing the recovered EM fraction close to the injected value.")

### Result
- Showed that the PSD-based correction improves deposited-energy resolution, with one representative rotation-based study reducing the resolution term by about a factor of `2`.
- Demonstrated that the time-profile fit can recover the dominant EM component with usable accuracy, for example `F_em = 0.740 +/- 0.055` for a reference value of `0.738` in one validation study.
- Identified a practical design constraint rather than just a positive result: one material candidate (`BGO`) did not separate proton-like and electron-like timing strongly enough for accurate EM-fraction extraction, while `ZnWO4` retained more distinguishable time shapes and therefore offered a more credible PSD route.

### Publications & Reports
- [Internal report: *PSD study update*] summarizes the time-profile fitting, EM-fraction recovery, and resolution-improvement studies behind this PSD workflow.
