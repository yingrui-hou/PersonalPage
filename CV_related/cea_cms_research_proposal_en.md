## Research Proposal

### Title
**Robust analysis, detector-performance validation, and calorimetry-driven R&D for CMS at the HL-LHC and beyond**

### 1. Research vision and fit with the position

My research profile is built around a simple idea: precise physics results require a tight connection between analysis methods, detector response, and software validation. My work has therefore combined reusable C++/Python/ROOT analysis workflows, likelihood-based inference under imperfect observations, simulation-to-data alignment, Geant4 detector studies, and beam-test-informed performance modelling. I would like to bring this integrated profile to the CMS group at CEA Saclay.

This proposal is designed to match the position's stated needs: detector work during the LHC long shutdown from 2026 to 2029, commissioning around 2030, analysis of LHC and HL-LHC data, and detector-performance studies for future colliders. It is also aligned with Saclay's strengths in Higgs physics, electromagnetic-object calibration, and calorimeter and timing instrumentation. The IRFU highlight published on April 2, 2026, on the CMS Higgs-boson mass measurement in the diphoton channel, enabled by new photon-energy calibration techniques developed at Irfu, is a strong example of the analysis-detector interface that motivates me.

My main strength is the ability to connect challenging measurements to the experimental chain that limits them, from weak-signal extraction and uncertainty-aware inference to detector-response modelling and validation workflows that turn discrepancies into detector, calibration, or software actions.

Within CMS at Saclay, I propose to organize my work around three strongly coupled research directions:

1. precision analyses robust to modelling and detector limitations;
2. detector-performance, calibration, and commissioning work for the HL-LHC era;
3. future collider detector R&D driven by physics performance requirements.

### 2. Research direction A: Precision CMS analyses with robust control of mismodelling

The HL-LHC program will not be limited by statistical power alone. In many flagship channels, the dominant limitations will come from calibration, reconstruction, pileup, detector response, and modelling uncertainties. I therefore want to contribute to CMS analyses in which robust treatment of imperfect measurements is a central ingredient rather than a technical afterthought.

A natural entry point is analyses involving electromagnetic objects and calorimeter-sensitive observables, because this is where Saclay has a strong legacy and where my own background is especially relevant. Photon and electron calibration, energy-resolution modelling, control-sample design, and weak-signal extraction are directly connected to the skills I have developed in collider analysis and detector validation. The same methodology can also be applied more broadly to Higgs, electroweak, top, and new-physics analyses pursued by the group.

My contribution in this direction would focus on four methodological pillars:

- **Control-sample-driven calibration and validation.** I want to help build workflows in which calibration and residual mismodelling are constrained with explicit control samples instead of absorbed into large effective uncertainties.
- **Inference under imperfect detector response.** I have experience with likelihood fits and joint modelling in situations where finite resolution, acceptance distortion, and sample mismatch can bias the extracted parameters. These tools are directly useful in precision measurements and rare-signal analyses.
- **Validated ML under dataset shift.** Modern CMS analyses rely heavily on multivariate methods, but these are only reliable if their behaviour remains stable under simulation-data mismatch. I want to contribute validation schemes in which reweighting, feature checks, train/test diagnostics, and uncertainty propagation are integrated into the analysis workflow.
- **Reusable statistical and software components.** Instead of ad hoc analysis code, I aim to develop reusable components for fitting, calibration, and validation that can be shared across channels and students.

In the first years I would seek to join an existing CMS physics effort at Saclay where detector performance and calibration are strongly coupled to the physics reach. Possible examples include precision measurements or searches involving photons, electrons, jets, missing transverse energy, or timing information. My goal would be to strengthen ongoing work through systematic calibration, modelling, and validation tools that remain reusable within the collaboration.

### 3. Research direction B: Detector performance, commissioning, and validation for HL-LHC CMS

The long shutdown from 2026 to 2029 and the startup of the upgraded detector around 2030 represent a critical phase for CMS. The scientific return of the HL-LHC will depend not only on hardware readiness, but also on the quality of detector-performance studies, commissioning procedures, synchronization, reconstruction validation, and rapid diagnosis of unexpected effects.

My detector-oriented work has combined Geant4 simulation, beam-test interpretation, signal-chain modelling, correction workflows, and anomaly-driven validation. I have used measured response maps to quantify how non-uniformity affects calorimeter resolution, developed timing-based signal-decomposition methods to improve reconstructed energy, and built validation workflows that traced discrepancies to detector behaviour or software issues. This is well suited to LS3 and early Phase-2 commissioning.

In CMS at Saclay, I would contribute to an end-to-end validation program linking instrumentation, reconstruction, and analysis:

- **Commissioning-oriented performance modelling.** Use simulation, bench data, and early detector data to build realistic response models and identify the observables most sensitive to synchronization, calibration drift, or reconstruction bias.
- **Benchmark-channel validation.** Develop physics-motivated benchmark workflows that can quickly reveal where discrepancies enter the chain: detector, calibration constants, clustering, object identification, or downstream software.
- **Data-quality and anomaly diagnosis.** Build validation procedures that do not stop at plotting discrepancies, but instead help isolate whether the origin is detector-related, calibration-related, or software-related.
- **Fast feedback loops between hardware and physics.** Use analysis-level sensitivity to prioritize detector studies, and conversely use detector findings to refine reconstruction and uncertainty models.

This direction is especially relevant for calorimetry and timing, where Saclay has a strong tradition in ECAL calibration and monitoring, as well as HL-LHC detector developments. My own experience in detector-response modelling and time-resolved signal analysis provides a credible path to contribute at this interface. The main deliverables would include validated software tools, commissioning procedures, performance notes, and contributions to publications where detector understanding is a limiting factor.

### 4. Research direction C: Physics-driven detector R&D for future colliders

The position also calls for defining detector-performance requirements for future colliders and contributing to the associated R&D. I see this as a natural extension of my current work. In several projects, I have already studied how detector response, non-uniformity, timing information, and simplified modelling assumptions propagate into reconstructed observables and measurement performance. I want to extend this approach into a more systematic physics-to-detector loop for future experiments.

My proposal in this direction is to develop studies in which detector design choices are evaluated not only with low-level metrics, but also with explicit propagation to physics performance. Relevant questions include:

- How do granularity, timing resolution, non-uniformity, and calibration stability affect precision Higgs or electroweak measurements?
- Which detector-response features are most critical for maintaining sensitivity in high-pileup environments?
- How should full simulation, fast simulation, and surrogate models be combined to explore design space efficiently while preserving physics credibility?
- Which beam-test observables are the most constraining for validating detector models before large-scale integration?

My background in Geant4 detector studies, response-map-based modelling, and timing-sensitive reconstruction provides a useful basis for these questions. I am especially interested in calorimetry and timing because they sit at the intersection of object reconstruction, trigger performance, particle-flow strategies, and future high-rate environments.

In practical terms, I would like to contribute to future-collider studies through:

- simulation campaigns that translate physics resolutions into detector specifications;
- analysis-oriented performance metrics for calorimetry and timing concepts;
- comparison of material, geometry, and response assumptions under realistic reconstruction scenarios;
- beam-test-informed tuning and validation of detector models;
- shared software tools that make these studies reusable by students and collaborators.

This program would help articulate detector priorities in a language directly connected to physics reach.

### 5. Implementation strategy and expected impact

I would implement this program in stages.

**Phase 1: integration and first contributions (late 2026 to 2027).**  
I would integrate into one Saclay CMS analysis effort and one detector-performance or upgrade-related task, with priority on areas where calibration and validation are immediately useful. During this phase, I would also identify the software and methodological components that can be generalized across projects.

**Phase 2: LS3-focused detector and performance work (2027 to 2029).**  
I would strengthen my contribution to detector validation, commissioning preparation, and reconstruction-performance studies, while maintaining a physics-analysis thread that keeps the work connected to final observables.

**Phase 3: startup and HL-LHC preparation (2030 onward).**  
I would help turn commissioning knowledge into stable reconstruction and analysis practices for the upgraded detector, and extend the most successful methods to HL-LHC analyses and future-collider studies.

Across all phases, I want to contribute to the collective life of the group through mentoring, code review culture, documentation, teaching, and dissemination. I value reproducible software, explicit uncertainty handling, and validation standards that make collaboration work more efficient.

### 6. Conclusion

My objective at CEA Saclay would be to strengthen the interface between detector understanding and precision physics within CMS. I want to contribute not only results, but also methods and software that remain useful beyond a single analysis. I believe my background in collider-data analysis, detector modelling, simulation-to-data alignment, and validation-oriented software development would allow me to contribute effectively to CMS during LS3, detector commissioning, HL-LHC preparation, and future collider R&D.
