---
number: 06
homepage_order: 4
collapsible: true
title: Test-Data Validation & Root-Cause Analysis
tags: Monitoring | Data Validation | Performance Diagnostics | Root-Cause Analysis
methods: benchmark-channel checks, MC-data comparison, detector-level diagnostics
impact: translated validation discrepancies into concrete calibration, detector, and software follow-ups before they became accepted bias.
industry: Production Monitoring | Model Validation | Observability | Quality Assurance
---
**Built a production-style validation workflow for early Run 3 photon reconstruction, focused on finding actionable detector and software issues.**

### Problem
The early Run 3 reconstruction chain needed validation before performance discrepancies hardened into accepted bias. The main challenge was to distinguish normal modelling differences from issues that were actually actionable at detector, calibration, or software level.

### Workflow
- Used multiple high- and low-momentum photon channels as benchmark datasets for reconstruction and identification checks.
- Compared MC and data across trigger streams and offline selections to isolate where discrepancies entered the pipeline.
- Traced anomalies back to detector-level and software-level causes instead of stopping at monitoring plots, leading to several fixes in the reconstruction chain and measurable improvement in energy-reconstruction performance.
  
![Data validation](assets/selected-work/work-6/data_validation.png "Validation plots exposed an energy miscalibration issue, and performance improved after the fix.")

### Result
- Turned validation discrepancies into concrete follow-up actions, including detector checks, calibration/alignment validation, and software fixes.
- Documented specific findings rather than generic monitoring noise, including an abnormal bump linked to a specific calorimeter cell, detector-region asymmetries in photon distributions, energy miscalibration, and a missing-energy software issue later fixed in reconstruction.
