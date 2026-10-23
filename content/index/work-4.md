---
number: 04
homepage_order: 2
collapsible: true
title: Sensor simulation and test automation
tags: Geant4 | Measurement | Shell Automation
methods: Geant4 simulation, beam-test analysis, response-map reconstruction
impact: linked measured non-uniformity to system-level resolution through both simulation code and experimental validation.
industry: Sensor Analytics | Measurement Systems | Simulation-Assisted Design
---
Connected prototype measurements to simulation and automated acquisition, calibration and initial data-quality checks.

### Problem
Spatial variations in sensor response affected measurement resolution. The simulation needed measured response maps to represent the prototype realistically.

### My contribution
- Implemented sensor geometry and response models in Geant4/C++ and incorporated response maps derived from beam-test measurements.
- Developed a Shell pipeline connecting existing readout, tracking and timing-calibration algorithms with storage and initial quality checks.
- Participated in on-site setup and data acquisition; assisted subsequent fitting and measurement-effect corrections.

### Validation and result
Compared simulated resolution with measured and uniform response maps. The prototype study quantified a non-uniformity contribution below 1% to the resolution’s constant term. The workflow connected physical tests, usable simulation inputs and design evaluation.

### Figures

![Energy-resolution comparison under measured non-uniformity maps](assets/selected-work/work-4/resolution.png "Measured-response curves show the resolution penalty relative to a flat-response reference.")
![Test bench setup](assets/selected-work/work-4/tbArch.png "Beam-test measurement system used to characterise the detector response.")
![Prototype](assets/selected-work/work-4/troll_2.png "The first detector prototype, which forms the sensitive part of the measurement setup.")
![Workflow to get the light-collection efficiency map](assets/selected-work/work-4/to_have_nPE_map.png "Workflow that turns beam-test measurements from the prototype system into the light-collection efficiency map used in simulation.")

### Publications

- Publication: *Studying the GRAiNITA concept: first test beam results*. DOI: [10.1088/1748-0221/21/03/P03048](https://doi.org/10.1088/1748-0221/21/03/P03048)
