---
number: 06
homepage_order: 3
collapsible: true
title: Performance diagnosis and software correction
tags: Root-Cause Analysis | Model Validation | Code Review
methods: benchmark-channel checks, MC-data comparison, detector-level diagnostics
impact: translated validation discrepancies into concrete calibration, detector, and software follow-ups before they became accepted bias.
industry: Research Monitoring | Model Validation | Observability | Quality Assurance
---
Investigated reconstruction and image-recognition performance, then delivered an algorithm correction used in subsequent analyses.

### Problem
Unexpected sensor-reconstruction results could originate in data, calibration, simulation labels or software. The cause had to be isolated before changing the model.

### My contribution
- Evaluated an image-recognition clustering model on real data and investigated discrepancies across benchmark samples. My role covered validation, not training this model.
- Traced anomalous simulated photon resolution to incorrect reference-label associations in crowded sensor data.
- Revised matching to select the largest individual energy contributor within the reconstructed cluster, using total simulated energy deposited in that cluster for normalisation.
- Improved legacy code’s thread safety in response to merge-request review.

### Validation and result
Checked reference identities, reconstructed energies and selected event records across several simulated processes. The merge request was accepted and used for LHCb Run 3 analyses and reconstruction-performance checks. Separately, real-data diagnostics informed calibration and software follow-up.

### Figures

![Data validation](assets/selected-work/work-6/data_validation.png "Validation plots exposed an energy miscalibration issue, and performance improved after the fix.")

### Publications

- Publication: *Monitoring reconstruction software in LHCb*. DOI: [10.1051/epjconf/202125103044](https://doi.org/10.1051/epjconf/202125103044)
