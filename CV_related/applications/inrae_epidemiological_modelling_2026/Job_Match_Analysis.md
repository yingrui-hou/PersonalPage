# INRAE OT-30377 - Match Analysis

Job: Postdoctoral Researcher - Epidemiological Modelling, Bayesian Inference and Artificial Intelligence  
Location: UMR Epidemiology of Animal and Zoonotic Diseases, Marcy-l'Étoile  
Contract: 24 months, starting 4 January 2027  
Salary: from EUR 3,559.17 gross per month  
Application deadline: 20 September 2026  
Reference: OT-30377

## Overall Assessment

Estimated evidence-based match: **65-72%**.

This is a strong and credible methodological transition. The posting explicitly accepts a PhD in physics, and the candidate directly matches Python, statistical inference, simulation calibration, latent-parameter estimation, uncertainty validation, large heterogeneous datasets, Git/Linux, reproducible pipelines, research autonomy, publications, and international collaboration.

The main selection risk is the requirement for strong knowledge in at least two of mechanistic modelling, Bayesian or simulation-based inference, deep learning, and phylodynamic/genomic analysis. The current evidence strongly supports simulation and statistical inference, but does not establish formal Bayesian simulation-based inference, neural density estimation, deep learning, epidemiology, phylodynamics, or genomics.

## Strong Matches

- PhD in experimental physics, explicitly listed as an accepted quantitative discipline.
- Mechanistic simulation and calibration against experimental measurements.
- Probabilistic and maximum-likelihood inference, mixture models, joint fits, and latent-parameter estimation.
- Time-dependent inference under finite resolution, selection effects, and dataset mismatch.
- Covariance-aware validation, pseudoexperiments, uncertainty propagation, and robustness studies.
- Integration of simulated, control, and measured datasets for model calibration.
- Python, C++, Git, Linux, workflow automation, CI/CD, and large-scale reproducible analysis.
- Autonomous research and collaboration in large international scientific teams.
- Peer-reviewed publications, technical documentation, and presentation of scientific results.
- Experience translating model-validation findings into concrete methodological or software actions.

## Partial Matches

- **Simulation-based inference:** substantial simulation-calibration and likelihood-free problem structure is present, but NPE/NLE or formal SBI frameworks are not documented.
- **Mechanistic modelling:** detailed physical-response models are documented, but not compartmental, agent-based, spatial epidemic, or transmission models.
- **Bayesian inference:** probabilistic inference and uncertainty analysis transfer well, but Bayesian posterior modelling is not explicitly evidenced.
- **Heterogeneous data integration:** simulated and measured sources are integrated, but not epidemiological, genomic, mobility, environmental, or geospatial databases.
- **Open-source research software:** reusable collaboration code is documented, but public packaging and maintenance are not strongly evidenced.

## Missing or Weakly Evidenced Requirements

- Epidemiological transmission modelling for structured human or animal populations.
- Neural Posterior Estimation and Neural Likelihood Estimation.
- PyTorch, JAX, Pyro, sbi, and Stan.
- Deep learning and neural density estimation.
- Bayesian workflow diagnostics, posterior predictive checking, and simulation-based calibration.
- Spatial epidemiology, geospatial analysis, and population mobility data.
- Phylodynamic modelling and genomic data analysis.
- Near-real-time sequential updating of epidemiological projections.

## Short-Term Gap Plan

### Feasible before the 20 September 2026 deadline

- Implement a compact SIR or SEIR simulator and calibrate it with the Python `sbi` package using NPE and NLE.
- Compare neural posterior estimates with a conventional likelihood or approximate Bayesian computation baseline.
- Add simulation-based calibration, posterior coverage, posterior predictive checks, and sensitivity analysis.
- Use a public epidemic dataset and document the full workflow in a reproducible Git repository with environment files, tests, and a concise methodological report.
- Review core epidemiological quantities: force of infection, reproduction number, generation interval, observation models, under-reporting, and identifiability.

### Feasible in 1-3 months

- Add spatially structured populations, mobility matrices, sequential updating, and heterogeneous data streams.
- Develop working familiarity with PyTorch, JAX, Stan or Pyro, and compare their modelling and computational trade-offs.
- Study phylodynamic and genomic-data fundamentals sufficiently to collaborate effectively with specialists.

### Not credibly fixable through a short project alone

- Established publication experience in epidemiology or phylodynamics.
- Deep expertise in pathogen transmission and public-health surveillance.
- Production experience maintaining near-real-time epidemic intelligence systems.

These gaps should be acknowledged directly while emphasizing the unusually close transfer between the candidate's existing simulation-calibration problems and the proposed simulation-based inference research.
