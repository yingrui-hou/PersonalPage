# Shortlist de postes ciblés: Simulation / Validation / R&D systèmes physiques

Date de vérification (Europe/Paris): `2026-04-21`

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit application” visible).

## Positionnement & logique de tri (rappel)

- Cible: `ingénierie simulation/validation` + `scientific software` pour systèmes physiques instrumentés (calibration, validation, correlation essai↔modèle, root-cause).
- Angle candidat (preuves dans le repo): workflows `Python/C++` réutilisables, validation sous bruit/biais, calibration/correction, simulation↔mesure, diagnostics menant à actions (fix logiciel, update calibration).
- Déprioriser: `meshing/SALOME/geometry-kernel`, “FEA/maillage” centré construction du modèle mécanique, et backend générique sans angle systèmes physiques.

### Priorités

- `A` = fit direct + transfert très clair
- `B` = bon fit mais gap (stack/domaine/seniority)
- `C` = stretch assumé (domaine très différent / prérequis manquants)

---

## Bucket A — priorité haute

### A1. Alice & Bob — Workflow Engineer - Calibration (H/F) (Paris, Hybrid)

- Liens (vérifiés le `2026-04-21`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070/apply
- Pourquoi c’est un fit:
  - Orchestration / DAG / retries / idempotence + “hardware-in-the-loop” et exigences de fiabilité: bon alignement avec ton angle “validation + workflows robustes”.
  - Calibration “en production” = boucle mesure → diagnostic → correction → monitoring.
- Risque/gap principal:
  - Attente “workflow systems” (Airflow/Prefect ou équivalent) + expérience production/fault-tolerance: il faut cadrer ce que tu as fait en termes de robustesse, monitoring, et triage.

#### CV title (tailored)

`Ingénieure workflows de calibration & validation (Python/C++) — systèmes physiques instrumentés`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la conception de workflows `Python/C++` pour calibration, validation et diagnostics sur données de mesure bruitées (sans vérité terrain directe).
J’apporte une culture “model & pipeline credibility” : métriques, stress tests, traçabilité, et boucles de correction qui transforment des écarts en actions (calibration updates, bug fixes).
À l’aise dans des environnements à code partagé et exigences de reproductibilité.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python/ROOT` workflows for weak-signal extraction, time-dependent inference, and validation on noisy datasets where direct event-level truth was unavailable.
2. Built benchmark-based monitoring workflows to validate reconstruction/calibration quality and traced anomalies to detector behaviour or software issues (incl. a missing-energy bug later fixed downstream).
3. Developed robust calibration & correction workflows (`ROOT/C++`) to reduce structured bias and compare performance before/after across operating conditions.
4. Implemented likelihood-based models and joint fits under finite resolution, biased observations, and sample mismatch, with uncertainty stress checks.
5. Aligned simulation and observed datasets via control-sample calibration and gradient-boosting reweighting to avoid mismatch-driven bias.
6. Worked in large technical collaborations with shared codebases and review discipline; delivered reusable components and documented validation procedures.

---

## Bucket B — bon fit avec gap réel

### B1. Alice & Bob — Senior Software Engineer - Calibration Software (Paris, Hybrid)

- Liens (vérifiés le `2026-04-21`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/b7386caa-70dd-4670-bb69-a5c97322332f
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/alice-bob/b7386caa-70dd-4670-bb69-a5c97322332f/apply
- Pourquoi c’est un fit:
  - Automatisation de calibrations, intégration software↔hardware, CI/CD, qualité/stabilité: très cohérent avec ton positionnement “calibration/validation/correction”.
- Risque/gap principal:
  - “Senior” + architecture + déploiement: il faut être factuelle sur ton niveau d’expérience “production engineering” vs “R&D tooling”.

#### CV title (tailored)

`Senior Python/C++ Engineer — Calibration software, validation & diagnostics (physical systems)`

#### Summary (tailored)

Scientific software engineer orientée calibration/validation: je conçois des pipelines `Python/C++` qui rendent des procédures expérimentales robustes, testables et traçables.
Je sais transformer des signaux réels (bruit, biais, non-uniformité) en métriques de performance, diagnostics, et corrections quantifiées, et livrer des outils réutilisables dans un environnement collaboratif.
Je vise des équipes où la fiabilité des calibrations et la gestion des échecs comptent autant que la performance nominale.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built calibration/correction workflows to reduce structured bias and quantify before/after improvements across conditions.
2. Built monitoring/validation pipelines that exposed issues and supported root-cause diagnosis (system vs software vs data), leading to concrete follow-up actions.
3. Implemented time-dependent inference and parameter estimation under imperfect observations (transfer to calibration loops and control software).
4. Developed reusable, versioned `Python/C++` components used in shared frameworks, with documented checks and reproducible runs.
5. Aligned simulation and observed datasets using control samples and reweighting to stabilize downstream inference decisions.
6. Contributed uncertainty stress checks for inference workflows (robustness under dataset shift / mismatch).

---

## Bucket C — stretch / à tenter si tu veux élargir

### C1. Aqemia — Scientific Software Engineer - Computational Chemistry (Paris/London, Hybrid)

- Liens (vérifiés le `2026-04-21`):
  - Offre (Lever): https://jobs.lever.co/aqemia.com/b1471d84-57f6-4122-9428-050a75b470c2
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/aqemia.com/b1471d84-57f6-4122-9428-050a75b470c2/apply
- Pourquoi c’est potentiellement intéressant:
  - Scientific software + pipelines/workflows + reproductibilité/traçabilité: pattern transférable.
- Risque/gap principal:
  - Pré-requis affichés en chimie computationnelle / RDKit / drug discovery (gap domaine significatif).

#### CV title (tailored)

`Scientific Software Engineer — Reproducible modeling & validation workflows (Python/C++)`

#### Summary (tailored)

Scientific software engineer avec background physique expérimentale, orientée “workflow quality”: je construis des pipelines de modélisation/validation reproductibles sur données et modèles imparfaits, avec diagnostics et traçabilité.
Je peux apporter une méthodologie de validation et une discipline d’outillage (tests, checks, stress tests), tout en restant factuelle sur un gap de domaine en chimie computationnelle.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python/ROOT` workflows for inference and validation under noise, bias, and limited ground truth.
2. Implemented likelihood-based models/joint fits and robustness checks to quantify sensitivity to assumptions.
3. Produced decision-facing validation outputs with traceability (metrics, comparisons, failure modes → corrective actions).
4. Built reproducible pipelines and documentation in shared environments with review discipline.
5. Developed calibration/correction workflows with quantified before/after performance.
6. Aligned simulated and observed datasets via calibration/reweighting to mitigate mismatch.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — “apply” non vérifiable (bloqué / dynamique / erreur)

- Framatome — Ingénieur Python – Validation et Développement (ref `2025-22838`): offre ouverte, mais la page de candidature TalentSoft n’a pas pu être ouverte de façon fiable (cache/erreur), donc **non retenu en A/B/C**.
  - Offre: https://www.framatome.com/en/jobseekers/job-offers/ingenieur-python-validation-et-developpement-f-h-ref-2025-22838/
- Safran — AI Engineer F/H (ref `175328`): candidature non vérifiable (erreur/cache) → exclu.
  - Offre: https://www.safran-group.com/jobs/france/chateaufort/ai-engineer-fh-175328
- EDF/Cyclife — Chef de Projet IA & Data Scientist Senior (ref `2026-161333`): bouton “Je postule” visible, mais chemin “/postuler” non vérifiable (erreur/cache) → exclu.
  - Offre: https://www.edf.fr/edf-recrute/offre/detail/2026-161333
- Schneider Electric (via Welcome to the Jungle) — apply externe equest non vérifiable (erreur/cache) → exclu.
  - Offre: https://www.welcometothejungle.com/fr/companies/schneider-electric/jobs/lead-data-scientist-timeseries-ml-optimization_rueil-malmaison
- SBG Systems (via Welcome to the Jungle) — apply externe Beetween “Loading…” (JS) donc statut de dépôt non vérifiable → exclu.
  - Offre: https://www.welcometothejungle.com/cs/companies/sbg-systems/jobs/ingenieur-algorithmes-de-navigation-confirme-f-h_carrieres-sur-seine
- Alice & Bob — Calibration API Software Engineer: page offre visible, mais page `/apply` non ouverte de façon fiable (erreur/cache) → exclu.
  - Offre: https://jobs.lever.co/alice-bob/b40a5281-ac51-439f-b690-0a30b0e9ced2

### Exclus — hors-cible (rappel)

- SIMVIA — rôles “Maillage & Simulation numérique” (trop `meshing/geometry/SALOME`) → hors-cible.
- Accenture — “Ingénieur simulation numérique F/H” (centré `maillage/FEA`) → hors-cible.
  - Offre: https://www.accenture.com/fr-fr/careers/jobdetails?id=R00288335_fr-fr
