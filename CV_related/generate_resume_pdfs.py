#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path

try:
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
except ImportError as exc:  # pragma: no cover - runtime dependency guard
    raise SystemExit(
        "Missing PDF dependencies. Install with: "
        "python3 -m pip install reportlab pypdf pdfplumber"
    ) from exc

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "content" / "shared" / "profile.md"
DEFAULT_RESUME_HTML = ROOT / "resume.html"
DEFAULT_INDEX_HTML = ROOT / "index.html"
DEFAULT_OUTPUT = SCRIPT_DIR / "output" / "pdf"


@dataclass(frozen=True)
class ExperienceSection:
    heading: str
    organization: str
    bullets: list[str]


@dataclass(frozen=True)
class SourceContent:
    profile: dict[str, str]
    resume_summary: list[str]
    resume_outcomes: list[str]
    resume_skills: list[str]
    resume_highlights: list[str]
    experience_label: str
    experience_sections: list[ExperienceSection]
    education: list[str]
    languages: list[str]
    positioning_title: str
    positioning_copy: list[str]
    hero_about: str
    hero_copy: list[str]
    overview_copy: list[str]
    project_summaries: list["ProjectSummary"]


@dataclass(frozen=True)
class SkillGroup:
    title: str
    keywords: tuple[str, ...]


@dataclass(frozen=True)
class ProjectSummary:
    title: str
    preview: str
    methods: str
    tags: tuple[str, ...] = ()


@dataclass(frozen=True)
class ResumeVariant:
    filename: str
    title: str
    headline: str
    summary_sources: tuple[str, ...]
    skill_groups: tuple[SkillGroup, ...]
    experience_keywords: tuple[str, ...]
    summary_override: tuple[str, ...] = ()
    skill_lines_override: tuple[str, ...] = ()
    experience_bullets_override: tuple[str, ...] = ()
    secondary_experience_title: str = ""
    secondary_experience_bullets: tuple[str, ...] = ()
    outcomes_override: tuple[str, ...] = ()
    max_summary: int = 2
    max_experience_bullets: int = 7
    max_outcomes: int = 3
    include_outcomes: bool = False
    include_highlights: bool = False
    force_second_page: bool = False
    include_context: bool = False
    context_title: str = "INDUSTRIAL FIT"
    context_sources: tuple[str, ...] = ()
    max_context_paragraphs: int = 0
    include_target_roles: bool = False
    target_roles: tuple[str, ...] = ()
    include_projects: bool = False
    project_keywords: tuple[str, ...] = ()
    preferred_project_titles: tuple[str, ...] = ()
    max_projects: int = 0
    additional_section_title: str = ""
    additional_section_bullets: tuple[str, ...] = ()
    include_research_links: bool = True
    compact_education: bool = False
    compact_education_inline: bool = False
    modern_layout: bool = False
    top_margin_mm: float = 16
    bottom_margin_mm: float = 14


VARIANTS = [
    ResumeVariant(
        filename="CV_YingruiHou_Sim.pdf",
        title="Yingrui Hou - Simulation Engineer Resume",
        headline="Simulation Engineer - Physical Systems, Calibration and Validation",
        summary_sources=("index_hero", "resume_summary", "index_positioning", "index_overview"),
        skill_groups=(
            SkillGroup(
                "Simulation and modelling",
                ("simulation", "geant4", "root", "roofit", "signal processing"),
            ),
            SkillGroup(
                "Calibration and validation",
                ("calibration", "validation", "alignment", "bias correction", "domain adaptation"),
            ),
            SkillGroup(
                "Data and inference",
                ("probabilistic", "statistical", "maximum likelihood", "large-scale"),
            ),
            SkillGroup(
                "Engineering workflow",
                ("python", "c/c++", "linux", "git", "ci/cd", "workflow"),
            ),
        ),
        experience_keywords=(
            "geant4",
            "simulation",
            "beam-test",
            "response maps",
            "measurement-chain",
            "signal-analysis",
            "calibration",
            "correction",
            "resolution",
            "monitoring",
            "anomalies",
            "model-correction",
            "measured constraints",
        ),
        max_summary=3,
        max_experience_bullets=9,
        include_outcomes=True,
        include_highlights=True,
        force_second_page=True,
        include_context=True,
        context_title="INDUSTRIAL FIT",
        context_sources=("index_positioning", "index_overview"),
        max_context_paragraphs=2,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_MichelinSIMIX.pdf",
        title="Yingrui Hou - Michelin SIMIX Resume",
        headline="Simulation & Validation Engineer | Physical Modelling, Test Correlation & Technical Application",
        summary_sources=("index_hero", "resume_summary", "index_positioning"),
        summary_override=(
            "Simulation and validation engineer with a PhD in experimental physics and several years of experience building C++/Python workflows for calibration, validation, inference, and monitoring on complex physical measurement systems.",
            "My core strength is making imperfect models useful for engineering decisions by connecting simulation, measurements, and physics-based interpretation through simulation-to-test alignment, bias correction, dataset preparation, and uncertainty-aware analysis.",
            "My BSc in Applied Physics included solid mechanics and finite element analysis coursework, and I ramp quickly on new physical domains. Combined with a PhD in experimental physics, this gives me a strong base for tyre, chassis, and vehicle-system simulation topics.",
        ),
        skill_lines_override=(
            "Simulation and modelling: physical-system modelling, simulation-to-measurement alignment, Geant4, ROOT / RooFit",
            "Validation and test correlation: calibration, bias correction, anomaly diagnostics, uncertainty-aware analysis",
            "Dataset and model preparation: response-map reconstruction, model correction, statistical modelling, monitoring",
            "Engineering workflow: Python, C/C++, Linux, reproducible analysis pipelines, shared codebases",
            "Technical collaboration and foundation: multidisciplinary coordination, technical communication, solid mechanics and FEA coursework",
        ),
        experience_bullets_override=(
            "Built reusable C++/Python workflows that connected simulation, noisy measurements, and physics-based interpretation for decision-facing analyses on complex systems.",
            "Combined test-beam data, simulation, and response maps to quantify how non-ideal behaviour affected overall performance, including a quantified contribution below 1% in a detailed study.",
            "Developed calibration and correction workflows to reduce structured bias and improve model credibility across operating conditions.",
            "Built monitoring and diagnostic pipelines that traced discrepancies back to detector behaviour or software issues and supported concrete corrective actions.",
            "Worked in shared Linux-based codebases with reproducible workflows, collaborative review discipline, and frequent interaction with multidisciplinary experts.",
        ),
        outcomes_override=(
            "Quantified that response non-uniformity contributed less than 1% to system-resolution degradation in a detailed measurement-to-model study.",
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis and calibration on realistic measurement data.",
        ),
        skill_groups=(
            SkillGroup(
                "Simulation and modelling",
                ("simulation", "geant4", "root", "roofit", "signal processing"),
            ),
            SkillGroup(
                "Validation and test correlation",
                ("calibration", "validation", "alignment", "bias correction", "domain adaptation"),
            ),
            SkillGroup(
                "Data and model preparation",
                ("measurement", "dataset", "monitoring", "statistical", "correction"),
            ),
            SkillGroup(
                "Engineering workflow",
                ("python", "c/c++", "linux", "git", "workflow"),
            ),
        ),
        experience_keywords=(
            "simulation",
            "measurement",
            "response maps",
            "calibration",
            "validation",
            "monitoring",
            "anomalies",
            "model correction",
            "test data",
            "decision",
        ),
        max_summary=3,
        max_experience_bullets=5,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=False,
        include_context=False,
        include_target_roles=False,
        include_projects=False,
        include_research_links=False,
        compact_education=True,
        compact_education_inline=True,
        bottom_margin_mm=10,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_R&D.pdf",
        title="Yingrui Hou - Simulation & Data Scientist Resume",
        headline="Simulation & Data Scientist | Calibration, Validation & Modelling for Physical Systems",
        summary_sources=("index_hero", "resume_summary", "index_positioning"),
        summary_override=(
            "Simulation and data scientist with a background in experimental physics and several years of experience building C++/Python workflows for calibration, validation, inference, and monitoring on complex measurement systems.",
            "My core strength is connecting simulations, noisy measurements, and statistical models to produce decision-ready results. I work best on problems where the true state is only indirectly observable and model credibility depends on calibration, bias correction, uncertainty-aware analysis, and rigorous validation, with strong intuition for instruments, detector behaviour, measurement limitations, and test-data interpretation.",
        ),
        skill_lines_override=(
            "Simulation and modelling: physical-system modelling, simulation-to-measurement alignment, Geant4, ROOT / RooFit",
            "Calibration and validation: model validation, calibration, bias correction, uncertainty-aware analysis",
            "Data science and inference: statistical modelling, anomaly detection, monitoring, dataset-shift handling, probabilistic inference",
            "Engineering workflow: Python, C/C++, Linux, workflow automation, reproducible analysis pipelines",
            "Experimental systems: noisy measurement systems, detector response, test-data interpretation, instrumentation-aware analysis",
        ),
        experience_bullets_override=(
            "Built C++/Python workflows to align simulations with noisy measurement data through calibration, validation, and model correction for decision-facing analyses.",
            "Developed statistical and simulation-based methods to estimate latent system behaviour when direct ground truth was unavailable.",
            "Built monitoring and diagnostic pipelines to compare expected versus observed behaviour, detect anomalies, and support root-cause analysis.",
            "Combined detector understanding, test data, and model outputs to improve calibration quality and reduce structured bias across operating conditions.",
            "Worked in Linux-based shared codebases with reproducible workflows and collaborative review discipline, translating validation results into calibration updates, software fixes, and improved model credibility.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed Geant4/C++ simulation, signal-modelling, and calibration workflows during doctoral research to connect detector response, measurement data, and system-level performance studies.",
        ),
        outcomes_override=(
            "Quantified that detector-response non-uniformity contributed less than 1% to system-resolution degradation in a detailed measurement-to-model study.",
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis and calibration on realistic measurement data.",
        ),
        skill_groups=(
            SkillGroup(
                "Simulation and modelling",
                ("simulation", "geant4", "root", "roofit", "signal processing"),
            ),
            SkillGroup(
                "Calibration and validation",
                ("calibration", "validation", "alignment", "bias correction", "domain adaptation"),
            ),
            SkillGroup(
                "Data science and inference",
                ("probabilistic", "statistical", "maximum likelihood", "monitoring", "anomaly", "large-scale"),
            ),
            SkillGroup(
                "Engineering workflow",
                ("python", "c/c++", "linux", "git", "ci/cd", "workflow"),
            ),
            SkillGroup(
                "Experimental systems",
                ("measurement", "detector", "test-data", "instrument"),
            ),
        ),
        experience_keywords=(
            "simulation",
            "measurement",
            "calibration",
            "validation",
            "monitoring",
            "anomalies",
            "dataset shift",
            "bias",
            "test data",
            "decision",
        ),
        max_summary=2,
        max_experience_bullets=5,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=False,
        include_context=False,
        include_target_roles=False,
        include_projects=False,
        include_research_links=False,
        compact_education=True,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_AWAKE.pdf",
        title="Yingrui Hou - AWAKE Industrial Data and Modelling Resume",
        headline="Data Scientist & Ingénieur Modélisation | Validation, Monitoring & Systèmes Industriels",
        summary_sources=("index_hero", "resume_summary", "index_positioning"),
        summary_override=(
            "Data scientist et ingénieur en modélisation titulaire d'un doctorat en physique expérimentale, avec plusieurs années d'expérience dans le développement de workflows Python/C++ pour l'analyse de données complexes, la calibration, la validation et le monitoring de systèmes physiques.",
            "Je souhaite transférer cette expérience vers des projets industriels à impact dans les secteurs New Energies & Infrastructures et Connectivity & Data, notamment pour l'analyse de systèmes énergétiques, la maintenance prédictive, la corrélation simulation-essais et le diagnostic d'anomalies.",
        ),
        skill_lines_override=(
            "Industrial data and ML: Python, pandas, NumPy, scikit-learn, statsmodels, CatBoost / Gradient Boosting",
            "Physical modelling: simulation-to-measurement alignment, response modelling, signal analysis, Geant4, ROOT / RooFit",
            "Validation and monitoring: calibration, model validation, anomaly detection, dataset-shift diagnostics, root-cause analysis",
            "Statistical methods: probabilistic inference, maximum-likelihood estimation, bias correction, uncertainty-aware analysis",
            "Engineering workflow: C/C++, Linux, Git, CI/CD practices, YAML / Shell / CMake automation, shared codebases",
            "Technical delivery: reproducible pipelines, documented results, multidisciplinary collaboration, decision-facing analysis",
        ),
        experience_bullets_override=(
            "Developed reusable Python/C++ workflows that connected simulations, complex measurement data, and statistical models for decision-facing technical analyses.",
            "Built monitoring and diagnostic pipelines to compare expected and observed behaviour, detect anomalies and distribution shifts, and support root-cause analysis.",
            "Implemented calibration and bias-correction methods that improved model credibility when direct ground truth was incomplete and operating conditions differed between datasets.",
            "Developed CatBoost-based workflows with feature studies, train/test diagnostics, reproducible model application, and dataset-shift mitigation through reweighting.",
            "Combined experimental understanding, test data, response maps, and simulation outputs to quantify performance limitations and separate physical effects from modelling artefacts.",
            "Worked in Linux-based shared codebases using Git, modular programming, collaborative review, reproducible configurations, and automated workflows across international teams.",
            "Translated validation findings into concrete follow-up actions, including calibration updates and the identification of a software issue that was subsequently corrected downstream.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed Geant4/C++ simulation, signal-modelling, calibration, and validation workflows to connect sensor response, experimental measurements, and system-level performance.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis, statistical fitting, and calibration on realistic measurement data.",
            "Quantified that response non-uniformity contributed less than 1% to system-resolution degradation in a measurement-to-model validation study.",
        ),
        skill_groups=(),
        experience_keywords=(
            "simulation",
            "measurement",
            "calibration",
            "validation",
            "monitoring",
            "anomalies",
            "dataset shift",
            "catboost",
            "root-cause",
            "decision",
        ),
        max_summary=2,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=True,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "sensor",
            "simulation",
            "test-data",
            "monitoring",
            "root-cause",
            "catboost",
            "dataset shift",
            "time-series",
            "model correction",
            "calibration",
        ),
        preferred_project_titles=(
            "Sensor Simulation & Reconstruction",
            "Test-Data Validation & Root-Cause Analysis",
            "Domain Adaptation for ML",
            "Time-Series Inference",
            "Model Correction Workflow",
        ),
        max_projects=5,
        include_research_links=False,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_ResilienceCare_MLDataScientist.pdf",
        title="Yingrui Hou - Resilience Care Machine Learning Data Scientist Resume",
        headline="Machine Learning Data Scientist | Longitudinal Modelling, Validation & Monitoring",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "PhD-trained applied data scientist with several years of experience developing Python/C++ workflows for statistical modelling, machine-learning validation, time-dependent inference, and monitoring on large, noisy real-world measurement datasets.",
            "Experienced in extracting reliable information when ground truth is incomplete, defining robustness checks under dataset mismatch, and translating complex analytical results into documented decisions. Motivated to bring this methodology to longitudinal patient data, real-world evidence, and responsible healthcare machine learning.",
        ),
        skill_lines_override=(
            "Data science and ML: Python, NumPy, pandas, scikit-learn, statsmodels, CatBoost / Gradient Boosting",
            "Longitudinal and statistical modelling: time-dependent inference, repeated observations, joint fitting, probabilistic models, maximum-likelihood estimation",
            "Validation: validation strategy, train/test diagnostics, calibration, bias correction, uncertainty quantification, robustness studies",
            "Monitoring and data quality: anomaly detection, expected-versus-observed monitoring, dataset-shift diagnostics, root-cause analysis",
            "Reproducible delivery: Linux, Git, CI/CD practices, modular pipelines, workflow automation, technical documentation",
            "Technical communication: assumptions and limitations, interpretable results, collaborative review, multidisciplinary teamwork",
        ),
        experience_bullets_override=(
            "Developed reusable Python/C++ analytical pipelines for large, noisy datasets with time-dependent observations, incomplete event-level ground truth, and changing operating conditions.",
            "Implemented probabilistic and maximum-likelihood models, including joint fits, to estimate latent parameters under background contamination, finite resolution, and sample mismatch.",
            "Designed validation strategies using control samples, train/test diagnostics, pseudoexperiments, uncertainty stress tests, and stability checks across datasets and selections.",
            "Built CatBoost-based predictive workflows with feature studies, threshold scans, reproducible scoring, and gradient-boosting reweighting to improve reliability under distribution shift.",
            "Developed automated monitoring and quality-control workflows that detected anomalies and traced discrepancies to calibration, detector, or software causes.",
            "Produced documented statistical summaries, diagnostic visualisations, and clear explanations of model assumptions, limitations, and results for multidisciplinary collaborators.",
            "Worked autonomously across parallel analysis topics in Linux-based shared codebases using Git, modular programming, collaborative review, and reproducible configurations.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed simulation-backed statistical analyses combining time-resolved signal reconstruction, calibration, probabilistic modelling, and validation against experimental data.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved component modelling, statistical fitting, and calibration on realistic measurement data.",
            "Identified a reconstruction-software issue through structured validation and monitoring; the issue was subsequently corrected downstream.",
        ),
        skill_groups=(),
        experience_keywords=(
            "python",
            "time-dependent",
            "statistical",
            "machine learning",
            "validation",
            "monitoring",
            "anomalies",
            "automation",
            "documentation",
            "collaboration",
        ),
        max_summary=2,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=True,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "time-series",
            "time-dependent",
            "catboost",
            "dataset shift",
            "monitoring",
            "validation",
            "weak-signal",
            "inference",
        ),
        preferred_project_titles=(
            "Time-Series Inference",
            "Domain Adaptation for ML",
            "Test-Data Validation & Root-Cause Analysis",
            "Advanced Inference Workflow Validation",
            "Weak-Signal Inference",
        ),
        max_projects=5,
        additional_section_title="RESEARCH & KNOWLEDGE SHARING",
        additional_section_bullets=(
            "Contributed to peer-reviewed publications and internal technical notes covering machine-learning validation, software monitoring, simulation-to-data studies, and statistical inference.",
            "Turned methodological ideas into reusable workflows with documented assumptions, limitations, validation evidence, and review-ready analytical outputs.",
            "Evaluated emerging inference methods under realistic measurement effects before their use in collaborative analyses.",
        ),
        include_research_links=False,
        compact_education=False,
        modern_layout=True,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_DS.pdf",
        title="Yingrui Hou - Applied Data Scientist Resume",
        headline="Applied Data Scientist | Statistical Modelling, Validation & Monitoring",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Applied data scientist with a background in experimental physics and several years of experience building Python/C++ workflows for calibration, validation, inference, and monitoring on noisy real-world measurement systems.",
            "Experience spans calibration, uncertainty-aware analysis, weak-label inference, dataset-shift mitigation, anomaly diagnostics, and reproducible pipelines for complex measurement data.",
            "Best fit: applied data science roles in analytics, model validation, monitoring, anomaly detection, or decision support for complex measurement data.",
        ),
        skill_lines_override=(
            "Core data science stack: Python, Statistical Modelling, Model Validation, Calibration, Monitoring",
            "Libraries and ML: scikit-learn, pandas, NumPy, statsmodels, CatBoost / Gradient Boosting",
            "Applied methods: Anomaly Detection, Bias Correction, Weak-label Inference, Dataset-shift Mitigation",
            "Engineering workflow: C/C++, Linux, Workflow Automation (YAML / Shell / CMake)",
            "Scientific computing: ROOT / RooFit, Geant4",
        ),
        experience_bullets_override=(
            "Built reusable Python/C++ workflows to analyse noisy measurement data, validate model behaviour, and support reliable downstream decisions.",
            "Developed calibration and bias-correction workflows to improve model reliability under sample mismatch and imperfect observation conditions.",
            "Built monitoring and diagnostic pipelines to detect anomalies, compare expected versus observed behaviour, and support root-cause analysis.",
            "Developed CatBoost-based validation pipelines with train/test diagnostics, reproducible model application, and dataset-shift mitigation through reweighting.",
            "Implemented fit-based inference where reliable event-level ground truth was unavailable, using control samples and structured validation.",
            "Worked in shared technical codebases with review discipline and reproducible delivery for decision-facing analyses.",
            "Turned validation findings into concrete follow-up actions, including calibration updates and a software issue later fixed downstream.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Built simulation-backed statistical workflows during doctoral research, combining model fitting, calibration, and bias-aware analysis on noisy measurements.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis and calibration on realistic measurement data.",
            "Quantified that detector-response non-uniformity contributed less than 1% to system-resolution degradation in a measurement-to-model validation study, helping separate true design risk from modelling noise.",
        ),
        skill_groups=(
            SkillGroup(
                "Applied data science",
                ("python", "pandas", "numpy", "scikit", "statsmodels", "matplotlib", "seaborn", "catboost", "gradient boosting"),
            ),
            SkillGroup(
                "Statistical modelling",
                ("probabilistic", "statistical", "maximum likelihood", "signal processing", "joint fitting", "likelihood"),
            ),
            SkillGroup(
                "Validation and monitoring",
                ("validation", "calibration", "alignment", "domain adaptation", "monitoring", "diagnostics", "reweighting", "large-scale"),
            ),
            SkillGroup(
                "Engineering workflow",
                ("workflow", "automation", "c/c++", "linux", "git", "ci/cd"),
            ),
            SkillGroup(
                "Scientific computing",
                ("root", "roofit", "geant4"),
            ),
        ),
        experience_keywords=(
            "weak-signal",
            "time-dependent inference",
            "likelihood",
            "joint fits",
            "catboost",
            "diagnostics",
            "reweighting",
            "calibration",
            "uncertainty",
            "monitoring",
            "anomalies",
            "large technical collaborations",
            "large-scale",
        ),
        max_summary=3,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=False,
        include_context=False,
        include_target_roles=False,
        target_roles=(
            "Applied Data Science",
            "Model Validation / Monitoring",
            "Analytics for Complex Measurement Data",
        ),
        include_projects=False,
        project_keywords=(
            "catboost",
            "validation",
            "monitoring",
            "diagnostics",
            "time-series",
            "time-dependent",
            "reweighting",
            "data validation",
            "anomaly",
            "dataset shift",
            "calibration",
        ),
        preferred_project_titles=(
            "Domain Adaptation for ML",
            "Test-Data Validation & Root-Cause Analysis",
            "Time-Series Inference",
        ),
        max_projects=3,
        include_research_links=False,
        compact_education=True,
        compact_education_inline=True,
        bottom_margin_mm=9,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_Michelin_AI.pdf",
        title="Yingrui Hou - Michelin Industrial AI Data Scientist Resume",
        headline="Data Scientist IA industrielle | Validation, Monitoring & Industrialisation",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Data scientist titulaire d'un doctorat en physique expérimentale, avec plusieurs années d'expérience dans le développement de workflows Python/C++ reproductibles pour la modélisation statistique, la validation, la calibration et le monitoring de systèmes de mesure complexes.",
            "Mon point fort est de transformer des données réelles bruitées et des modèles imparfaits en solutions fiables et exploitables, en combinant diagnostic d'anomalies, correction des biais, suivi des performances et collaboration avec des équipes techniques multidisciplinaires.",
        ),
        skill_lines_override=(
            "Data science and AI: Python, pandas, NumPy, scikit-learn, statsmodels, CatBoost / Gradient Boosting",
            "Validation and monitoring: model validation, calibration, anomaly detection, dataset-shift diagnostics, bias correction, uncertainty-aware analysis",
            "Industrialisation foundation: Git, CI/CD, Linux, modular and reusable workflows, YAML / Shell / CMake automation",
            "Delivery and collaboration: technical documentation, structured model outputs, data-quality checks, cross-functional teamwork, knowledge transfer",
            "Engineering and scientific computing: C/C++, ROOT / RooFit, Geant4, large-scale data-processing workflows",
        ),
        experience_bullets_override=(
            "Built reusable Python/C++ workflows to analyse noisy real-world measurement data, validate model behaviour, and deliver reliable outputs for downstream technical decisions.",
            "Designed monitoring and diagnostic pipelines to compare expected versus observed behaviour, detect anomalies and distribution shifts, and support root-cause analysis.",
            "Developed CatBoost-based validation workflows with train/test diagnostics, reproducible model application, feature studies, and dataset-shift mitigation through reweighting.",
            "Implemented calibration and bias-correction methods that improved model reliability when direct ground truth was incomplete and operating conditions differed between datasets.",
            "Automated repeatable analysis steps in Linux-based shared codebases using Git, CI/CD practices, YAML, Shell, and CMake, with collaborative review discipline.",
            "Produced documented analysis methods, structured diagnostics, and interpretable results for multidisciplinary collaborators, clearly communicating model use, assumptions, and limitations.",
            "Turned validation findings into concrete follow-up actions, including calibration updates and the identification of a software issue that was later corrected downstream.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed simulation-backed statistical workflows combining model fitting, calibration, signal analysis, and bias-aware validation on complex measurement data.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis and calibration on realistic measurement data.",
            "Quantified that response non-uniformity contributed less than 1% to system-resolution degradation, helping distinguish genuine system risk from modelling effects.",
        ),
        skill_groups=(),
        experience_keywords=(
            "monitoring",
            "anomalies",
            "diagnostics",
            "dataset shift",
            "validation",
            "calibration",
            "workflow",
            "automation",
            "collaboration",
            "decision",
        ),
        max_summary=2,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=True,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "monitoring",
            "validation",
            "root-cause",
            "catboost",
            "dataset shift",
            "reweighting",
            "model correction",
            "framework integration",
            "time-series",
            "calibration",
            "weak-signal",
            "production yield",
        ),
        preferred_project_titles=(
            "Test-Data Validation & Root-Cause Analysis",
            "Domain Adaptation for ML",
            "Model Correction Workflow",
            "Time-Series Inference",
            "Weak-Signal Inference",
        ),
        max_projects=5,
        include_research_links=False,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_Sanofi_DataScientist.pdf",
        title="Yingrui Hou - Sanofi Data Scientist Resume",
        headline="Data Scientist | Statistical Modelling, Validation & Monitoring",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Data scientist with a PhD in experimental physics and several years of experience building reusable Python/C++ workflows for statistical modelling, machine-learning validation, calibration, monitoring, and inference on complex measurement data.",
            "Strongest in problems where observations are noisy, ground truth is incomplete, and reliable decisions require dataset alignment, bias correction, uncertainty-aware analysis, and robust validation across operating conditions.",
            "Seeking to transfer this problem-solving experience to industrial data products for manufacturing, process monitoring, and model-driven decision support.",
        ),
        skill_lines_override=(
            "Data science: Python, NumPy, pandas, scikit-learn, statsmodels, CatBoost / Gradient Boosting",
            "Modelling: statistical inference, maximum-likelihood estimation, probabilistic modelling, time-series modelling under noise",
            "ML and data quality: supervised learning, feature engineering, domain adaptation, reweighting, train/test diagnostics",
            "Validation: model validation, calibration, bias correction, uncertainty quantification, monitoring, anomaly diagnosis",
            "Engineering: C/C++, Linux, Git, CI/CD, YAML / Shell / CMake automation, large-scale data-processing workflows",
            "Visualisation and scientific computing: matplotlib, seaborn, ROOT / RooFit, Geant4",
        ),
        experience_bullets_override=(
            "Built reusable Python/C++/ROOT workflows for weak-signal extraction, time-dependent inference, and validation on noisy datasets where reliable event-level ground truth was unavailable.",
            "Implemented likelihood-based models and joint fits to estimate latent parameters under sample mismatch, finite resolution, and biased observation conditions.",
            "Developed CatBoost-based selection and validation pipelines with feature studies, train/test diagnostics, threshold scans, and reproducible model application.",
            "Aligned simulated and observed datasets through gradient-boosting reweighting and control-sample calibration before downstream inference and selection decisions.",
            "Built monitoring workflows that compared expected and observed behaviour, traced anomalies to detector or software causes, and supported calibration updates and corrective actions.",
            "Worked in Linux-based shared codebases with review discipline, reproducible workflows, and collaboration across large international technical teams.",
            "Contributed reusable statistical components and uncertainty-stress checks for weighted and unbinned inference workflows on large datasets.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed simulation-backed statistical workflows combining Geant4/C++, signal modelling, calibration, and bias-aware analysis of noisy measurements.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis, component fitting, and calibration on realistic measurement data.",
            "Quantified a response non-uniformity contribution below 1% in a measurement-to-model validation study and separated physical performance effects from modelling artefacts.",
        ),
        skill_groups=(),
        experience_keywords=(
            "python",
            "catboost",
            "validation",
            "monitoring",
            "time-dependent",
            "likelihood",
            "reweighting",
            "calibration",
            "large",
        ),
        max_summary=3,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=True,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "catboost",
            "validation",
            "monitoring",
            "time-series",
            "reweighting",
            "data validation",
            "root-cause",
            "calibration",
        ),
        preferred_project_titles=(
            "Domain Adaptation for ML",
            "Time-Series Inference",
            "Test-Data Validation & Root-Cause Analysis",
            "Weak-Signal Inference",
            "Advanced Inference Workflow Validation",
        ),
        max_projects=5,
        include_research_links=False,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_Sanofi_ScientificDataAnalyst.pdf",
        title="Yingrui Hou - Sanofi Vaccines Scientific Data Analyst Resume",
        headline="Scientific Data Analyst | Python, Statistical Modelling & Reproducible Workflows",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Scientific data analyst with a PhD in experimental physics and several years of experience developing Python/C++ workflows for statistical modelling, data manipulation, calibration, validation, inference, and monitoring on large, noisy, real-world measurement datasets.",
            "Experienced in building reusable and reviewable analytical pipelines, producing documented figures and statistical summaries, validating ML and inference workflows, and collaborating with scientists in international teams.",
            "Motivated to transfer this rigorous open-source programming practice to clinical-trial analytics while developing expertise in CDISC standards and clinical development.",
        ),
        skill_lines_override=(
            "Data analysis: Python, NumPy, pandas, data manipulation, exploratory analysis, statistical summaries, visualisation",
            "Statistical modelling: maximum-likelihood estimation, probabilistic and mixture models, joint fitting, latent-parameter inference",
            "AI and ML: scikit-learn, statsmodels, CatBoost / Gradient Boosting, feature studies, train/test diagnostics",
            "Validation and QC: model validation, calibration, bias correction, uncertainty checks, pseudoexperiments, anomaly diagnosis",
            "Reproducible programming: Git, code review, modular workflows, CI/CD practices, YAML / Shell / CMake automation",
            "Engineering and delivery: C/C++, Linux, shared codebases, large-scale data processing, technical documentation",
        ),
        experience_bullets_override=(
            "Developed reusable Python/C++/ROOT pipelines for data preparation, exploratory analysis, statistical inference, validation, and production of documented analytical outputs on large datasets.",
            "Implemented probabilistic and maximum-likelihood models, including joint fits, under background contamination, finite resolution, incomplete event-level ground truth, and dataset mismatch.",
            "Built CatBoost-based workflows with feature studies, train/test diagnostics, threshold scans, reproducible model application, and gradient-boosting reweighting.",
            "Developed automated monitoring and QC workflows that compared expected and observed behaviour, detected anomalies, and traced discrepancies to calibration, detector, or software causes.",
            "Contributed covariance-aware checks, pseudoexperiments, uncertainty-stress studies, and control-sample validation for advanced inference workflows.",
            "Produced structured statistical summaries, diagnostic figures, documented methods, and interpretable results for review by multidisciplinary collaborators.",
            "Worked in Linux-based shared codebases using Git, modular programming, collaborative review, reproducible configurations, and automated workflows across international teams.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed Geant4/C++ simulation and statistical-analysis workflows combining response modelling, calibration, signal reconstruction, bias-aware interpretation, and validation against experimental data.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved component modelling, statistical fitting, and calibration on realistic measurement data.",
            "Identified a reconstruction-software issue through structured validation and monitoring; the issue was subsequently corrected downstream.",
        ),
        skill_groups=(),
        experience_keywords=(
            "python",
            "statistical",
            "validation",
            "monitoring",
            "catboost",
            "pseudoexperiment",
            "documentation",
            "reproducible",
            "collaboration",
        ),
        max_summary=3,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=True,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "statistical",
            "validation",
            "pseudoexperiment",
            "weak-signal",
            "catboost",
            "time-series",
            "monitoring",
            "root-cause",
        ),
        preferred_project_titles=(
            "Advanced Inference Workflow Validation",
            "Weak-Signal Inference",
            "Domain Adaptation for ML",
            "Time-Series Inference",
            "Test-Data Validation & Root-Cause Analysis",
        ),
        max_projects=5,
        include_research_links=False,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_Limagrain_Biostatistician.pdf",
        title="Yingrui Hou - Limagrain Biostatistician Data Scientist Resume",
        headline="Biostatistics & Data Science | Modelling, ML Validation & Decision Support",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Statistical data scientist with a PhD in experimental physics and several years of experience developing reusable Python/C++ workflows for probabilistic modelling, machine-learning validation, time-dependent inference, and decision support on large, noisy datasets.",
            "Experienced in extracting latent information when ground truth is incomplete, aligning mismatched datasets, testing model robustness, quantifying uncertainty, and translating analytical results into calibration or software decisions.",
            "Seeking to transfer this quantitative and collaborative R&D experience to breeding innovation while developing domain expertise in quantitative genetics and plant-science data.",
        ),
        skill_lines_override=(
            "Statistics: probabilistic modelling, maximum-likelihood estimation, mixture models, joint fitting, uncertainty quantification",
            "Data science and ML: Python, NumPy, pandas, scikit-learn, statsmodels, CatBoost / Gradient Boosting",
            "Analytical methods: supervised learning, feature engineering, time-series modelling, domain adaptation, reweighting",
            "Validation: train/test diagnostics, model validation, calibration, bias correction, robustness studies, monitoring",
            "Software and reproducibility: C/C++, Linux, Git, CI/CD, YAML / Shell / CMake automation, shared codebases",
            "Visualisation and scientific computing: matplotlib, seaborn, ROOT / RooFit, Geant4, large-scale data workflows",
        ),
        experience_bullets_override=(
            "Developed reusable Python/C++/ROOT analytical workflows for weak-signal extraction, time-dependent inference, and model validation on large datasets with incomplete event-level ground truth.",
            "Implemented probabilistic and maximum-likelihood models, including joint fits, to estimate latent parameters under sample mismatch, finite resolution, and biased observations.",
            "Built CatBoost-based classification workflows with feature studies, train/test diagnostics, threshold scans, and reproducible model application.",
            "Applied gradient-boosting reweighting and control-sample calibration to align datasets before downstream prediction and statistical inference.",
            "Contributed reusable fit components, covariance-aware checks, pseudoexperiments, and uncertainty-stress tests for advanced inference workflows.",
            "Built monitoring and diagnostic workflows that converted expected-versus-observed discrepancies into calibration follow-up and software corrective actions.",
            "Worked in Linux-based shared codebases with Git, review discipline, reproducible workflows, and international multidisciplinary teams.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed simulation-backed statistical analyses combining model fitting, signal reconstruction, calibration, and bias-aware interpretation of noisy measurements.",
        ),
        outcomes_override=(
            "Improved reconstructed-energy resolution by about 2x through time-resolved signal analysis, component fitting, and calibration on realistic measurement data.",
            "Validated a statistical extraction strategy through control samples, dataset-specific corrections, and explicit robustness checks under background, efficiency, and resolution effects.",
        ),
        skill_groups=(),
        experience_keywords=(
            "statistical",
            "likelihood",
            "catboost",
            "time-dependent",
            "reweighting",
            "validation",
            "uncertainty",
            "large",
            "shared",
        ),
        max_summary=3,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=True,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "statistical",
            "catboost",
            "validation",
            "time-series",
            "reweighting",
            "inference",
            "decision",
            "large-scale",
        ),
        preferred_project_titles=(
            "Advanced Inference Workflow Validation",
            "Domain Adaptation for ML",
            "Time-Series Inference",
            "Weak-Signal Inference",
            "Test-Data Validation & Root-Cause Analysis",
        ),
        max_projects=5,
        include_research_links=False,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_INRAE_EpidemiologicalModelling.pdf",
        title="Yingrui Hou - INRAE Epidemiological Modelling Postdoc Resume",
        headline="Statistical Modelling & Simulation | Inference, Validation & Python",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Quantitative researcher with a PhD in experimental physics and several years of postdoctoral experience developing Python/C++ workflows for probabilistic modelling, simulation calibration, latent-parameter inference, and uncertainty-aware validation on large, noisy datasets.",
            "Experienced in likelihood-based models, joint fits, simulation-to-data alignment, covariance-aware checks, pseudoexperiments, time-dependent inference, and reproducible analysis in international scientific collaborations.",
            "Motivated to transfer this methodological experience to simulation-based inference and mechanistic epidemiological models for real-time epidemic intelligence.",
        ),
        skill_lines_override=(
            "Statistical inference: maximum-likelihood estimation, probabilistic and mixture models, joint fitting, latent-parameter estimation",
            "Simulation and calibration: Geant4, simulation-to-data alignment, response modelling, bias correction, model validation",
            "Uncertainty and robustness: uncertainty quantification, covariance-aware checks, pseudoexperiments, stress tests",
            "Data science and ML: Python, NumPy, pandas, scikit-learn, statsmodels, CatBoost / Gradient Boosting",
            "Time-dependent analysis: time-series modelling under noise, acceptance and resolution modelling, dataset-specific corrections",
            "Reproducible research: C/C++, Linux, Git, CI/CD, YAML / Shell / CMake, shared codebases, large-scale workflows",
        ),
        experience_bullets_override=(
            "Developed reusable Python/C++/ROOT workflows for time-dependent inference and weak-signal extraction from large datasets with incomplete event-level ground truth.",
            "Implemented probabilistic and maximum-likelihood models, including joint fits, to estimate latent parameters under background contamination, finite resolution, and biased observations.",
            "Built simulation-to-data calibration and reweighting workflows that integrated heterogeneous simulated, control, and measured datasets before downstream inference.",
            "Contributed covariance-aware validation, pseudoexperiments, and uncertainty-stress checks for advanced weighted and unbinned inference methods.",
            "Developed CatBoost-based pipelines with feature studies, train/test diagnostics, threshold scans, and reproducible model application under dataset shift.",
            "Built monitoring workflows that compared predicted and observed behaviour, identified anomalies, and translated findings into calibration or software corrective actions.",
            "Worked autonomously in Linux-based shared codebases and international collaborations, contributing reusable methods, technical documentation, peer-reviewed publications, and scientific presentations.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed Geant4/C++ simulation and statistical-analysis workflows combining mechanistic response modelling, calibration, signal reconstruction, and validation against experimental data.",
        ),
        outcomes_override=(
            "Validated a novel inference workflow under background, efficiency, resolution, and modelling variations using covariance-aware checks and pseudoexperiments.",
            "Improved reconstructed-energy resolution by about 2x through time-resolved component modelling, statistical fitting, and calibration on realistic measurement data.",
        ),
        skill_groups=(),
        experience_keywords=(
            "inference",
            "simulation",
            "probabilistic",
            "likelihood",
            "time-dependent",
            "pseudoexperiment",
            "uncertainty",
            "python",
            "reproducible",
        ),
        max_summary=3,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=False,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "inference",
            "simulation",
            "time-series",
            "statistical",
            "validation",
            "pseudoexperiment",
            "calibration",
            "uncertainty",
        ),
        preferred_project_titles=(
            "Advanced Inference Workflow Validation",
            "Time-Series Inference",
            "Weak-Signal Inference",
            "Sensor Simulation & Reconstruction",
            "Domain Adaptation for ML",
        ),
        max_projects=5,
        include_research_links=True,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
    ResumeVariant(
        filename="CV_YingruiHou_Limagrain_DataEngineer.pdf",
        title="Yingrui Hou - Limagrain Digital Agriculture Data Engineer Resume",
        headline="Data Engineer / Applied Data Scientist | Analytics, Monitoring & Reliable Workflows",
        summary_sources=("resume_summary", "index_overview", "index_hero"),
        summary_override=(
            "Applied data scientist with a PhD in experimental physics and more than three years of postdoctoral experience developing Python/C++ data-processing, statistical-modelling, validation, and monitoring workflows for large, complex datasets.",
            "Experienced in reproducible pipeline development, data-quality diagnostics, ML validation, workflow automation, and root-cause analysis that converted anomalies into calibration or software corrective actions.",
            "Seeking to transfer this technical foundation to reliable digital-agriculture services and analytical products while developing advanced R, DevOps/MLOps, and platform-operations expertise.",
        ),
        skill_lines_override=(
            "Data processing: Python, NumPy, pandas, large-scale analysis workflows, structured data inputs and outputs",
            "Machine learning: scikit-learn, statsmodels, CatBoost / Gradient Boosting, feature studies, train/test validation",
            "Monitoring and quality: data validation, anomaly diagnosis, expected-versus-observed checks, root-cause analysis",
            "Workflow engineering: C/C++, Linux, YAML / Shell / CMake automation, reusable pipeline components",
            "Software practices: Git, CI/CD, shared codebases, technical review, reproducibility, documentation",
            "Analytics: statistical modelling, time-series analysis, calibration, uncertainty quantification, matplotlib, seaborn",
        ),
        experience_bullets_override=(
            "Developed reusable Python/C++/ROOT data-processing and analysis workflows for large, noisy datasets, replacing one-off analyses with structured and reproducible pipelines.",
            "Built monitoring workflows that compared expected and observed behaviour, identified data or software anomalies, and supported calibration updates and corrective actions.",
            "Developed CatBoost-based pipelines with feature studies, train/test diagnostics, threshold scans, saved model outputs, and reproducible application across datasets.",
            "Automated data preparation, statistical extraction, validation checks, and reporting inputs using Python/C++, YAML, Shell, and shared configuration.",
            "Integrated simulated, control, and measured datasets through reweighting, calibration, and data-quality checks before downstream analysis and decisions.",
            "Worked in Linux-based shared codebases using Git and CI/CD practices, with collaborative review, technical documentation, and reproducible delivery.",
            "Diagnosed concrete detector and software issues, including a missing-data problem later corrected in the reconstruction workflow, rather than stopping at descriptive monitoring.",
        ),
        secondary_experience_title="Doctoral Research | University of Chinese Academy of Sciences | 2016-2021",
        secondary_experience_bullets=(
            "Developed simulation and data-analysis software combining C++, automated processing, calibration, performance evaluation, and validation against experimental measurements.",
        ),
        outcomes_override=(
            "Built validation workflows that exposed actionable data and software issues and supported downstream corrective actions.",
            "Improved reconstructed-data resolution by about 2x through time-resolved analysis, model correction, and calibration on realistic measurements.",
        ),
        skill_groups=(),
        experience_keywords=(
            "workflow",
            "monitoring",
            "software",
            "data",
            "python",
            "validation",
            "automation",
            "catboost",
            "shared",
        ),
        max_summary=3,
        max_experience_bullets=7,
        max_outcomes=2,
        include_outcomes=True,
        include_highlights=False,
        force_second_page=False,
        include_context=False,
        include_target_roles=False,
        include_projects=True,
        project_keywords=(
            "monitoring",
            "validation",
            "software",
            "workflow",
            "catboost",
            "framework",
            "time-series",
            "automation",
        ),
        preferred_project_titles=(
            "Test-Data Validation & Root-Cause Analysis",
            "Domain Adaptation for ML",
            "Weak-Signal Inference",
            "Model Correction Workflow",
            "Time-Series Inference",
        ),
        max_projects=5,
        include_research_links=False,
        compact_education=False,
        top_margin_mm=13,
        bottom_margin_mm=11,
    ),
]


class BlockHTMLParser(HTMLParser):
    BLOCK_TAGS = {"p", "h1", "h2", "h3", "li"}
    SKIP_TAGS = {"script", "style", "svg"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.blocks: list[tuple[str, str]] = []
        self.current_tag: str | None = None
        self.current_parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "br" and self.current_tag:
            self.current_parts.append(" ")
            return
        if tag in self.BLOCK_TAGS:
            self.current_tag = tag
            self.current_parts = []

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if self.current_tag == tag:
            text = normalize_text("".join(self.current_parts))
            if text:
                self.blocks.append((tag, text))
            self.current_tag = None
            self.current_parts = []

    def handle_data(self, data: str) -> None:
        if self.skip_depth or not self.current_tag:
            return
        self.current_parts.append(data)


def normalize_text(text: str) -> str:
    cleaned = text.replace("\xa0", " ").replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", cleaned).strip()


def parse_front_matter(path: Path) -> dict[str, str]:
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = raw.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def extract_inner_html(raw: str, tag: str, selector: str, selector_type: str) -> str:
    if selector_type == "id":
        pattern = rf"<{tag}[^>]*\bid=\"{re.escape(selector)}\"[^>]*>(.*?)</{tag}>"
    elif selector_type == "class":
        pattern = rf"<{tag}[^>]*\bclass=\"[^\"]*{re.escape(selector)}[^\"]*\"[^>]*>(.*?)</{tag}>"
    else:  # pragma: no cover - internal misuse guard
        raise ValueError(f"Unsupported selector type: {selector_type}")

    match = re.search(pattern, raw, re.S)
    if not match:
        raise SystemExit(f"Could not locate <{tag}> with {selector_type}={selector!r}")
    return match.group(1)


def extract_text(raw: str, pattern: str, label: str) -> str:
    match = re.search(pattern, raw, re.S)
    if not match:
        raise SystemExit(f"Could not locate {label} in HTML source")
    return normalize_text(re.sub(r"<[^>]+>", " ", html.unescape(match.group(1))))


def parse_blocks(fragment_html: str) -> list[tuple[str, str]]:
    parser = BlockHTMLParser()
    parser.feed(fragment_html)
    return parser.blocks


def parse_paragraphs(fragment_html: str) -> list[str]:
    return [text for tag, text in parse_blocks(fragment_html) if tag == "p"]


def parse_bullets(fragment_html: str) -> list[str]:
    return [text for tag, text in parse_blocks(fragment_html) if tag == "li"]


def parse_heading_and_paragraphs(fragment_html: str) -> tuple[str, list[str]]:
    heading = ""
    paragraphs: list[str] = []
    for tag, text in parse_blocks(fragment_html):
        if tag in {"h1", "h2", "h3"} and not heading:
            heading = text
        elif tag == "p":
            paragraphs.append(text)
    return heading, paragraphs


def parse_education(fragment_html: str) -> list[str]:
    items: list[str] = []
    current_heading = ""
    for tag, text in parse_blocks(fragment_html):
        if tag in {"h2", "h3"}:
            current_heading = text
        elif tag == "p":
            items.append(f"{current_heading} - {text}" if current_heading else text)
            current_heading = ""
    if current_heading:
        items.append(current_heading)
    return items


def parse_experience(fragment_html: str) -> list[ExperienceSection]:
    sections: list[ExperienceSection] = []
    current_heading = ""
    current_org = ""
    current_bullets: list[str] = []

    for tag, text in parse_blocks(fragment_html):
        if tag == "h3":
            if current_heading or current_bullets:
                sections.append(ExperienceSection(current_heading, current_org, current_bullets))
            current_heading = text
            current_org = ""
            current_bullets = []
        elif tag == "p" and current_heading and not current_org:
            current_org = text
        elif tag == "li":
            current_bullets.append(text)

    if current_heading or current_bullets:
        sections.append(ExperienceSection(current_heading, current_org, current_bullets))
    return sections


def parse_project_summaries(index_raw: str) -> list[ProjectSummary]:
    project_matches = re.findall(
        r'<article class="case-study[^"]*" id="[^"]+">(.*?)</article>',
        index_raw,
        re.S,
    )
    projects: list[ProjectSummary] = []
    for block in project_matches:
        title_match = re.search(r"<h3>(.*?)</h3>", block, re.S)
        preview_match = re.search(r'<div class="case-preview">.*?<p>(.*?)</p>', block, re.S)
        methods_match = re.search(r'<p class="case-meta"><strong>Methods:</strong>\s*(.*?)</p>', block, re.S)
        tags = tuple(
            normalize_text(html.unescape(re.sub(r"<[^>]+>", " ", tag)))
            for tag in re.findall(r'<span class="case-tag">(.*?)</span>', block, re.S)
        )
        title = normalize_text(html.unescape(re.sub(r"<[^>]+>", " ", title_match.group(1)))) if title_match else ""
        preview = normalize_text(html.unescape(re.sub(r"<[^>]+>", " ", preview_match.group(1)))) if preview_match else ""
        methods = normalize_text(html.unescape(re.sub(r"<[^>]+>", " ", methods_match.group(1)))) if methods_match else ""
        if title and preview:
            projects.append(ProjectSummary(title=title, preview=preview, methods=methods, tags=tags))
    return projects


def load_source_content(
    profile: dict[str, str],
    resume_html_path: Path,
    index_html_path: Path,
) -> SourceContent:
    resume_raw = resume_html_path.read_text(encoding="utf-8")
    index_raw = index_html_path.read_text(encoding="utf-8")

    positioning_heading, positioning_copy = parse_heading_and_paragraphs(
        extract_inner_html(index_raw, "div", "profile-positioning", "class")
    )

    return SourceContent(
        profile=profile,
        resume_summary=parse_paragraphs(extract_inner_html(resume_raw, "section", "resume-summary", "id")),
        resume_outcomes=parse_bullets(extract_inner_html(resume_raw, "div", "resume-outcomes", "id")),
        resume_skills=parse_bullets(extract_inner_html(resume_raw, "div", "resume-skills", "id")),
        resume_highlights=parse_bullets(extract_inner_html(resume_raw, "div", "resume-highlights", "id")),
        experience_label=extract_text(
            resume_raw,
            r"<p[^>]*id=\"experience-label\"[^>]*>(.*?)</p>",
            "resume experience label",
        ),
        experience_sections=parse_experience(extract_inner_html(resume_raw, "div", "resume-experience", "id")),
        education=parse_education(extract_inner_html(resume_raw, "div", "resume-education", "id")),
        languages=parse_bullets(extract_inner_html(resume_raw, "div", "resume-languages", "id")),
        positioning_title=positioning_heading,
        positioning_copy=positioning_copy,
        hero_about=extract_text(index_raw, r"<p class=\"hero-about\">(.*?)</p>", "hero about"),
        hero_copy=parse_paragraphs(extract_inner_html(index_raw, "div", "hero-copy", "class")),
        overview_copy=parse_paragraphs(extract_inner_html(index_raw, "div", "toc-copy", "class")),
        project_summaries=parse_project_summaries(index_raw),
    )


def unique_nonempty(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        normalized = normalize_text(item)
        if not normalized:
            continue
        key = normalized.casefold()
        if key in seen:
            continue
        seen.add(key)
        result.append(normalized)
    return result


def summary_pool(source: SourceContent) -> dict[str, list[str]]:
    return {
        "resume_summary": source.resume_summary,
        "index_positioning": source.positioning_copy,
        "index_hero": [source.hero_about, *source.hero_copy],
        "index_overview": source.overview_copy,
    }


def choose_summary(source: SourceContent, variant: ResumeVariant) -> list[str]:
    if variant.summary_override:
        return list(variant.summary_override[: variant.max_summary])
    selected: list[str] = []
    for pool_name in variant.summary_sources:
        selected.extend(summary_pool(source).get(pool_name, []))
    return unique_nonempty(selected)[: variant.max_summary]


def choose_context_paragraphs(source: SourceContent, variant: ResumeVariant) -> list[str]:
    if not variant.include_context or not variant.context_sources or variant.max_context_paragraphs <= 0:
        return []
    selected: list[str] = []
    pools = summary_pool(source)
    for pool_name in variant.context_sources:
        selected.extend(pools.get(pool_name, []))
    return unique_nonempty(selected)[: variant.max_context_paragraphs]


def choose_projects(source: SourceContent, variant: ResumeVariant) -> list[ProjectSummary]:
    if not variant.include_projects or variant.max_projects <= 0:
        return []
    preferred_index = {title: index for index, title in enumerate(variant.preferred_project_titles)}
    ranked = sorted(
        source.project_summaries,
        key=lambda project: (
            preferred_index.get(project.title, len(preferred_index)),
            -score_text(
                " ".join([project.title, project.preview, project.methods, *project.tags]),
                variant.project_keywords,
            ),
            source.project_summaries.index(project),
        ),
    )
    return ranked[: variant.max_projects]


def grouped_skills(source: SourceContent, variant: ResumeVariant) -> list[str]:
    if variant.skill_lines_override:
        return list(variant.skill_lines_override)
    items = unique_nonempty(source.resume_skills)
    used: set[str] = set()
    lines: list[str] = []

    for group in variant.skill_groups:
        matched = [
            item
            for item in items
            if item not in used and any(keyword in item.casefold() for keyword in group.keywords)
        ]
        if matched:
            lines.append(f"{group.title}: {', '.join(matched)}")
            used.update(matched)

    leftovers = [item for item in items if item not in used]
    if leftovers:
        ranked_leftovers = sorted(
            leftovers,
            key=lambda item: (-score_text(item, variant.experience_keywords), items.index(item)),
        )
        relevant_leftovers = [item for item in ranked_leftovers if score_text(item, variant.experience_keywords) > 0]
        if relevant_leftovers:
            lines.append(f"Additional tools and methods: {', '.join(relevant_leftovers[:3])}")
    return lines


def choose_display_experience_bullets(source: SourceContent, variant: ResumeVariant) -> list[str]:
    if variant.experience_bullets_override:
        return list(variant.experience_bullets_override[: variant.max_experience_bullets])
    return choose_experience_bullets(source, variant)


def choose_outcomes(source: SourceContent, variant: ResumeVariant) -> list[str]:
    if variant.outcomes_override:
        return list(variant.outcomes_override[: variant.max_outcomes])
    return list(source.resume_outcomes[: variant.max_outcomes])


def score_text(text: str, keywords: tuple[str, ...]) -> int:
    lowered = text.casefold()
    score = 0
    total = len(keywords)
    for index, keyword in enumerate(keywords):
        if keyword in lowered:
            score += total - index
    return score


def choose_experience_bullets(source: SourceContent, variant: ResumeVariant) -> list[str]:
    candidates: list[tuple[int, int, int, str]] = []
    for section_index, section in enumerate(source.experience_sections):
        for bullet_index, bullet in enumerate(section.bullets):
            score = score_text(bullet, variant.experience_keywords)
            candidates.append((score, section_index, bullet_index, bullet))

    selected = [item for item in sorted(candidates, key=lambda item: (-item[0], item[1], item[2])) if item[0] > 0]
    selected = selected[: variant.max_experience_bullets]

    if len(selected) < variant.max_experience_bullets:
        selected_keys = {(section_index, bullet_index) for _, section_index, bullet_index, _ in selected}
        for item in sorted(candidates, key=lambda item: (item[1], item[2])):
            key = (item[1], item[2])
            if key in selected_keys:
                continue
            selected.append(item)
            selected_keys.add(key)
            if len(selected) >= variant.max_experience_bullets:
                break

    ordered = sorted(selected, key=lambda item: (item[1], item[2]))
    return [bullet for _, _, _, bullet in ordered]


def parse_experience_label(label: str) -> tuple[str, str]:
    inner_match = re.search(r"\[(.*?)\]", label)
    inner = inner_match.group(1) if inner_match else label
    date_match = re.search(r"^(.*?)\s*\(([^)]+)\)\s*$", inner)
    if not date_match:
        return normalize_text(inner), ""
    role = normalize_text(date_match.group(1))
    dates = normalize_text(date_match.group(2)).replace(" - ", "-").replace(" – ", "-")
    return role, dates


def make_styles(modern: bool = False) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    alignment = 0 if modern else 1
    primary = HexColor("#17324D") if modern else HexColor("#101820")
    accent = HexColor("#246B78") if modern else HexColor("#1d3557")
    return {
        "name": ParagraphStyle(
            "ResumeName",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=23 if modern else 20,
            leading=27 if modern else 24,
            textColor=primary,
            alignment=alignment,
            spaceAfter=1 if modern else 2,
        ),
        "headline": ParagraphStyle(
            "ResumeHeadline",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5 if modern else 12,
            leading=14.5 if modern else 15,
            textColor=accent,
            alignment=alignment,
            spaceAfter=5 if modern else 4,
        ),
        "contact": ParagraphStyle(
            "ResumeContact",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.1 if modern else 9.5,
            leading=11.2 if modern else 12,
            alignment=alignment,
            textColor=HexColor("#30343f"),
            spaceAfter=1 if modern else 2,
        ),
        "section": ParagraphStyle(
            "ResumeSection",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.2 if modern else 10.5,
            leading=12.5 if modern else 13,
            textColor=accent if modern else primary,
            spaceBefore=8 if modern else 9,
            spaceAfter=2 if modern else 4,
        ),
        "body": ParagraphStyle(
            "ResumeBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.8 if modern else 10,
            leading=12.3 if modern else 12.5,
            textColor=HexColor("#202124"),
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "ResumeBullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.45 if modern else 9.7,
            leading=12 if modern else 12.3,
            textColor=HexColor("#202124"),
            leftIndent=12,
            firstLineIndent=-10,
            spaceAfter=2,
        ),
        "job": ParagraphStyle(
            "ResumeJob",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10 if modern else 10.1,
            leading=12.4 if modern else 12.5,
            textColor=primary,
            spaceAfter=4,
        ),
        "project_meta": ParagraphStyle(
            "ResumeProjectMeta",
            parent=base["BodyText"],
            fontName="Helvetica-Oblique",
            fontSize=9.2,
            leading=11.4,
            textColor=HexColor("#4a5568"),
            spaceAfter=3,
        ),
        "compact_note": ParagraphStyle(
            "ResumeCompactNote",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.4,
            leading=9.8,
            textColor=HexColor("#202124"),
            spaceAfter=0,
        ),
        "compact_label": ParagraphStyle(
            "ResumeCompactLabel",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.2,
            leading=9.6,
            textColor=HexColor("#101820"),
            spaceAfter=0,
        ),
    }


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html.escape(text), style)


def bullet(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(html.escape(f"- {text}"), style)


def add_section_heading(
    story: list,
    title: str,
    styles: dict[str, ParagraphStyle],
    modern: bool,
) -> None:
    story.append(para(title, styles["section"]))
    if modern:
        story.append(
            HRFlowable(
                width="100%",
                thickness=0.6,
                color=HexColor("#9CB8BE"),
                spaceBefore=0,
                spaceAfter=4,
            )
        )
    else:
        story.append(Spacer(1, 2))


def short_url(url: str) -> str:
    return url.replace("https://", "").replace("http://", "").replace("www.", "").rstrip("/")


def profile_lines(profile: dict[str, str], variant: ResumeVariant) -> list[str]:
    phone = profile.get("phone", "").replace("(0)", " (0)")
    line_one = " | ".join(
        part
        for part in [
            profile.get("location", ""),
            phone,
            profile.get("email", ""),
        ]
        if part
    )
    lines = [line_one] if line_one else []

    if not variant.include_research_links:
        compact_links = " | ".join(
            part
            for part in [
                f"Website: {short_url(profile.get('homepage', ''))}" if profile.get("homepage") else "",
                f"LinkedIn: {short_url(profile.get('linkedin', ''))}" if profile.get("linkedin") else "",
            ]
            if part
        )
        if compact_links:
            lines.append(compact_links)
        return lines

    if profile.get("homepage"):
        lines.append(f"Website: {short_url(profile.get('homepage', ''))}")

    line_two = " | ".join(
        part
        for part in [
            f"LinkedIn: {short_url(profile.get('linkedin', ''))}" if profile.get("linkedin") else "",
            f"GitLab: {short_url(profile.get('personal_gitlab', ''))}" if profile.get("personal_gitlab") else "",
            f"CERN: {short_url(profile.get('cern_gitlab', ''))}" if profile.get("cern_gitlab") else "",
        ]
        if part
    )
    if line_two:
        lines.append(line_two)
    return lines


def build_resume(source: SourceContent, variant: ResumeVariant, output_path: Path) -> None:
    styles = make_styles(variant.modern_layout)
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=variant.top_margin_mm * mm,
        bottomMargin=variant.bottom_margin_mm * mm,
        title=variant.title,
        author=source.profile.get("name", "Yingrui Hou"),
        subject=variant.headline,
        keywords=", ".join(unique_nonempty([*source.resume_skills, *source.resume_highlights])),
    )

    story = [
        para(source.profile.get("name", "Yingrui Hou"), styles["name"]),
        para(variant.headline, styles["headline"]),
    ]

    for line in profile_lines(source.profile, variant):
        story.append(para(line, styles["contact"]))

    if variant.modern_layout:
        story.append(
            HRFlowable(
                width="100%",
                thickness=1.2,
                color=HexColor("#246B78"),
                spaceBefore=5,
                spaceAfter=2,
            )
        )
    else:
        story.append(Spacer(1, 6))
    add_section_heading(story, "PROFESSIONAL SUMMARY", styles, variant.modern_layout)
    for paragraph in choose_summary(source, variant):
        story.append(para(paragraph, styles["body"]))

    add_section_heading(story, "CORE SKILLS", styles, variant.modern_layout)
    for line in grouped_skills(source, variant):
        story.append(bullet(line, styles["bullet"]))

    add_section_heading(story, "PROFESSIONAL EXPERIENCE", styles, variant.modern_layout)
    role, dates = parse_experience_label(source.experience_label)
    organization = next((section.organization for section in source.experience_sections if section.organization), "")
    job_line = " | ".join(part for part in [role, organization, dates] if part)
    story.append(para(job_line, styles["job"]))
    for item in choose_display_experience_bullets(source, variant):
        story.append(bullet(item, styles["bullet"]))

    if variant.secondary_experience_title and variant.secondary_experience_bullets:
        secondary_story = [para(variant.secondary_experience_title, styles["job"])]
        for item in variant.secondary_experience_bullets:
            secondary_story.append(bullet(item, styles["bullet"]))
        story.append(KeepTogether(secondary_story))

    if variant.force_second_page:
        story.append(PageBreak())

    selected_outcomes = choose_outcomes(source, variant)
    if variant.include_outcomes and selected_outcomes:
        outcomes_story: list = []
        add_section_heading(outcomes_story, "SELECTED OUTCOMES", styles, variant.modern_layout)
        for item in selected_outcomes:
            outcomes_story.append(bullet(item, styles["bullet"]))
        story.append(KeepTogether(outcomes_story))

    if variant.include_highlights and source.resume_highlights:
        add_section_heading(story, "TECHNICAL HIGHLIGHTS", styles, variant.modern_layout)
        for item in source.resume_highlights:
            story.append(bullet(item, styles["bullet"]))

    if variant.include_target_roles and variant.target_roles:
        add_section_heading(story, "TARGET ROLES", styles, variant.modern_layout)
        for item in variant.target_roles:
            story.append(bullet(item, styles["bullet"]))

    selected_projects = choose_projects(source, variant)
    if selected_projects:
        add_section_heading(story, "SELECTED PROJECTS", styles, variant.modern_layout)
        for project in selected_projects:
            story.append(para(project.title, styles["job"]))
            story.append(para(project.preview, styles["body"]))
            if project.methods:
                story.append(para(f"Methods: {project.methods}", styles["project_meta"]))

    context_paragraphs = choose_context_paragraphs(source, variant)
    if context_paragraphs:
        add_section_heading(story, variant.context_title, styles, variant.modern_layout)
        for paragraph in context_paragraphs:
            story.append(para(paragraph, styles["body"]))

    if variant.additional_section_title and variant.additional_section_bullets:
        add_section_heading(story, variant.additional_section_title, styles, variant.modern_layout)
        for item in variant.additional_section_bullets:
            story.append(bullet(item, styles["bullet"]))

    if variant.compact_education:
        if variant.compact_education_inline:
            compact_footer = "Education: " + " | ".join(source.education)
            compact_footer += " | Languages: " + ", ".join(source.languages)
            story.append(para(compact_footer, styles["compact_note"]))
        else:
            footer_table = Table(
                [
                    [
                        para("EDUCATION", styles["compact_label"]),
                        para(" | ".join(source.education), styles["compact_note"]),
                    ],
                    [
                        para("LANGUAGES", styles["compact_label"]),
                        para(", ".join(source.languages), styles["compact_note"]),
                    ],
                ],
                colWidths=[25 * mm, doc.width - 25 * mm],
            )
            footer_table.setStyle(
                TableStyle(
                    [
                        ("LINEABOVE", (0, 0), (-1, 0), 0.5, HexColor("#d9dde3")),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 0),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                        ("TOPPADDING", (0, 0), (-1, -1), 2),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ]
                )
            )
            story.append(footer_table)
    else:
        add_section_heading(story, "EDUCATION & LANGUAGES", styles, variant.modern_layout)
        for item in source.education:
            story.append(bullet(item, styles["bullet"]))
        story.append(
            bullet(
                "Languages: " + ", ".join(source.languages),
                styles["bullet"],
            )
        )

    doc.build(story)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate ATS-safe PDFs from the current resume.html and index.html content."
    )
    parser.add_argument(
        "--resume-html",
        type=Path,
        default=DEFAULT_RESUME_HTML,
        help="Path to the rendered resume HTML file.",
    )
    parser.add_argument(
        "--index-html",
        type=Path,
        default=DEFAULT_INDEX_HTML,
        help="Path to the rendered index HTML file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Directory for generated PDFs.",
    )
    parser.add_argument(
        "--variant",
        action="append",
        default=[],
        help="Generate only the named PDF filename. May be repeated.",
    )
    args = parser.parse_args()

    profile = parse_front_matter(PROFILE_PATH)
    if not profile:
        raise SystemExit(f"Could not parse profile data from {PROFILE_PATH}")

    source = load_source_content(profile, args.resume_html, args.index_html)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    selected_variants = VARIANTS
    if args.variant:
        requested = set(args.variant)
        selected_variants = [variant for variant in VARIANTS if variant.filename in requested]
        missing = requested - {variant.filename for variant in selected_variants}
        if missing:
            available = ", ".join(variant.filename for variant in VARIANTS)
            raise SystemExit(f"Unknown variant(s): {', '.join(sorted(missing))}. Available: {available}")

    for variant in selected_variants:
        build_resume(source, variant, args.output_dir / variant.filename)
        print(args.output_dir / variant.filename)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
