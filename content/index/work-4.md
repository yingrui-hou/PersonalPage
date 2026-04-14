---
number: 04
homepage_order: 1
collapsible: true
title: Sensor Simulation & Reconstruction
tags: Signal Processing | Simulation Calibration | Digital Twins
methods: Geant4 simulation, beam-test analysis, response-map reconstruction
impact: linked measured non-uniformity to system-level resolution through both simulation code and experimental validation.
industry: Sensor Analytics | Measurement Systems | Simulation-Assisted Design
---
**Built a simulation-and-measurement workflow to quantify how detector non-uniformity affects energy resolution, using beam-test data to constrain the model instead of assuming ideal sensor response.**

![Energy-resolution comparison under measured non-uniformity maps](assets/selected-work/work-4/resolution.png "Measured-response curves show the resolution penalty relative to a flat-response reference.")

### Problem
The key question was how much detector non-uniformity would degrade the energy resolution of a calorimeter. A flat-response simulation was not sufficient, because the measured light-collection efficiency changed across the detector volume, while a full optical simulation would add major complexity and computational cost. *At the prototype development stage, combining a simplified simulation with an effective light-collection efficiency map measured from test-beam data is the most practical way to evaluate resolution.*

### Workflow
- Built the measurement-to-simulation chain around the beam-test setup, combining the first prototype response, beam-position tracking, and dedicated analysis code to recover position-dependent light-yield information.
- Used the June 2024 test-beam analysis to turn beam-position-resolved measurements into an effective light-yield / uniformity map and then injected that map into the Geant4-based energy-deposition simulation so that effective detected energy could be computed event by event under realistic response assumptions.
- Implemented detector geometry, stepping, and response logic in Geant4/C++ and used the resulting distributions to fit energy-resolution curves under both measured and idealised response maps.

![Test bench setup](assets/selected-work/work-4/tbArch.png "Beam-test measurement system used to characterise the detector response.")
![Prototype](assets/selected-work/work-4/troll_2.png "The first detector prototype, which forms the sensitive part of the measurement setup.")
![Workflow to get the light-collection efficiency map](assets/selected-work/work-4/to_have_nPE_map.png "Workflow that turns beam-test measurements from the prototype system into the light-collection efficiency map used in simulation.")

### Result
- Turned a beam-test measurement into a usable simulation input rather than leaving it as a standalone detector study.
- Showed explicitly that non-flat response maps worsen the reconstructed energy resolution relative to a flat-response reference, with a non-uniformity-driven constant term less than `1.0%` in the detailed study, which strengthens confidence in simulation-informed design decisions.
