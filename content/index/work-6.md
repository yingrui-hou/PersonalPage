---
number: 06
homepage_order: 3
collapsible: true
title: Image-Recognition Model Validation & ECAL Performance
tags: Image Recognition | Real-Data Validation | Performance Optimisation | Root-Cause Analysis
methods: benchmark-channel checks, MC-data comparison, detector-level diagnostics
impact: translated validation discrepancies into concrete calibration, detector, and software follow-ups before they became accepted bias.
industry: Research Monitoring | Model Validation | Observability | Quality Assurance
---
**Investigated performance discrepancies using real data and identified findings for calibration and software follow-up. The work included evaluating and optimising an image-recognition model for LHCb Run 3 ECAL clustering.**

### Problem
The early Run 3 reconstruction chain needed validation before performance discrepancies hardened into accepted bias. The main challenge was to distinguish normal modelling differences from issues that were actually actionable at detector, calibration, or software level.

### Workflow
- Used multiple high- and low-momentum photon channels as benchmark datasets for reconstruction and identification checks.
- Compared MC and data across trigger streams and offline selections to isolate where discrepancies entered the pipeline.
- Traced anomalies to detector and software causes, documenting findings for calibration and corrective follow-up by the responsible teams.
- Used real-data-driven checks to study and optimise the performance of the image-recognition model used for ECAL clustering.
- Participated in model-construction and training discussions to support subsequent validation; did not train the clustering model.
  
![Data validation](assets/selected-work/work-6/data_validation.png "Validation plots exposed an energy miscalibration issue, and performance improved after the fix.")

### Result
- Turned validation discrepancies into concrete follow-up actions, including detector checks, calibration/alignment validation, and software fixes.
- Documented specific findings rather than generic monitoring noise, including an abnormal bump linked to a specific calorimeter cell, detector-region asymmetries in photon distributions, energy miscalibration, and a missing-energy software issue later fixed in reconstruction.

### Publications & Reports
- [Internal note: *Run3 performance check with photon-involved channels*] documents the benchmark-channel validation strategy, selection checks, and reconstruction issues tracked in this work.
- Publication: *Monitoring reconstruction software in LHCb*. DOI: [10.1051/epjconf/202125103044](https://doi.org/10.1051/epjconf/202125103044)
