# Shortlist de postes ciblés: Simulation / Validation / R&D systèmes physiques

Date de vérification (Europe/Paris): `2026-04-24` (dernière vérification: `11:34` CEST)

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Cible: `ingénierie simulation/validation` + `scientific software` pour systèmes physiques instrumentés (calibration, validation, corrélation essai↔modèle, root-cause).
- Angle candidat (preuves dans ce repo, notamment `resume.html`): workflows `Python/C++/ROOT`, simulation capteur (`Geant4/C++`), validation sous bruit/biais, calibration/correction, simulation↔mesure, monitoring & diagnostic menant à actions.
- Déprioriser: `meshing/SALOME/geometry-kernel`, rôles purement “maillage/FEA mécanique”, BI/dashboards, backend générique sans angle systèmes physiques.

### Priorités

- `A` = fit direct + transfert très clair
- `B` = bon fit mais gap (stack/domaine/seniority)
- `C` = stretch assumé (domaine très différent / prérequis manquants)

---

## Bucket A — priorité haute

### A1. Outsight — Customer Validation Engineer (Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre (Lever): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3/apply
- Pourquoi c’est un fit:
  - Validation/acceptance sur système “terrain” (mesures + critères d’acceptation) avec outillage `Python` → mapping direct vers ton axe `validation/calibration/diagnostic`.
  - Problème “systèmes physiques + données bruitées + décision” (éviter l’overfit sur métriques nominales).
- Risque/gap principal:
  - Contexte delivery/client + déplacements + réseaux/IT (sur site) → à cadrer comme “validation strategy + tooling + reporting + boucle corrective”.

#### CV title (tailored)

`Ingénieure validation & calibration (Python/C++) — systèmes physiques / capteurs`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la **validation** et la **calibration/correction** de modèles et pipelines sur données de mesure bruitées, via des workflows reproductibles en `Python/C++`.
J’identifie et quantifie les écarts “attendu vs observé”, puis je les transforme en diagnostics et actions (corrections, critères d’acceptation, monitoring).

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python/ROOT` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented likelihood-based models and joint fits to estimate latent parameters under sample mismatch, finite resolution, and biased observations.
3. Aligned simulated and observed datasets through gradient-boosting reweighting and control-sample calibration before downstream decisions.
4. Developed `ROOT/C++` calibration and correction workflows to reduce structured bias; quantified before/after across operating conditions.
5. Built monitoring workflows to validate reconstruction/calibration quality; traced anomalies to detector behaviour or software issues and drove follow-up actions.
6. Communicated uncertainty/limitations clearly to keep acceptance decisions aligned with evidence (stress checks, robustness under shift).

---

## Bucket B — bon fit avec gap réel

### B1. Fairmat — Software Engineer - Robotics (Bouguenais/Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre (Lever): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091/apply
- Pourquoi c’est un fit:
  - Dév `C++/Python` sur cellules robotiques industrielles + **tests/validation/non-régression** + analyse de données de prod → très cohérent avec ton axe “validation + diagnostic + boucle corrective”.
  - “Terrain + mesures + anomalies” : bon transfert de ton expérience monitoring/diagnostic.
- Risque/gap principal:
  - Stack `ROS`/robotique (Gazebo/RViz) + pratique terrain usine → gap à assumer; se positionner sur “validation, tests, robustness, triage”.

#### CV title (tailored)

`Scientific software / validation engineer (C++/Python) — tests, diagnostic, systèmes industriels`

#### Summary (tailored)

Scientific software engineer orientée fiabilité: je construis des workflows `C++/Python` robustes et traçables pour relier modèles/logiciels et comportements observés via mesures, puis transformer les écarts en actions (correctifs, tests, monitoring).
Je peux contribuer fortement sur la partie validation/diagnostic et outillage de non-régression, tout en restant factuelle sur un gap `ROS`.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that surfaced anomalies and supported root-cause diagnosis (system vs software vs data).
2. Delivered reproducible pipelines with traceable outputs and documented checks enabling reliable reruns and comparisons.
3. Developed calibration/correction tooling to reduce structured bias and compare performance before/after across operating conditions.
4. Implemented robustness checks under mismatch/shift; quantified sensitivity to assumptions and failure modes.
5. Worked in large shared codebases with review discipline; delivered reusable components feeding validation and calibration decisions.
6. Modelled measurement-chain behaviour (signal chain / sensor response) to interpret test data and avoid overconfident conclusions.

### B2. Alice & Bob — Workflow Engineer - Calibration (H/F) (Paris, Hybrid)

- Liens (vérifiés le `2026-04-24`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070/apply
- Pourquoi c’est un fit:
  - Sujet “workflows fiables + contrôles qualité + auditabilité + (hardware-in-the-loop)” = ton axe “validation/calibration sous bruit/biais + monitoring/diagnostic”.
  - Forte composante “orchestration + checks + recovery” où ton approche “stress tests + validation” est transférable.
- Risque/gap principal:
  - Attentes seniorité (5+ ans) + expérience orchestration/DAG/hardware control; bien cadrer l’impact sur “validation, monitoring, robustness, tooling”.

#### CV title (tailored)

`Scientific software engineer — calibration/validation workflows & monitoring (Python/C++)`

#### Summary (tailored)

Ingénieure issue de la physique expérimentale, spécialisée dans la **calibration** et la **validation** de pipelines sur systèmes de mesure bruités, avec une approche “workflow credibility” (checks, monitoring, diagnostics, corrections).
Je rends des procédures de calibration plus fiables et actionnables en fermant la boucle entre écarts observés et actions correctives.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python/ROOT` workflows for validation and inference under noisy measurements with limited ground truth.
2. Developed calibration/correction workflows that reduced structured bias; quantified before/after improvements across regimes.
3. Built monitoring pipelines that exposed anomalies; traced issues to detector behaviour vs software and triggered follow-up fixes.
4. Implemented robustness/stress checks under mismatch/shift to prevent overconfident conclusions.
5. Contributed reusable components in shared codebases with review discipline; made workflows auditable and reproducible.
6. Aligned simulation and measurement constraints to improve model credibility (simulation-to-data alignment, correction workflows).

---

## Bucket C — stretch assumé

### C1. MaiaSpace — Flight Engineering Software Development and Validation Engineer (Paris — La Défense, On-site)

- Liens (vérifiés le `2026-04-24`):
  - Offre + candidature (formulaire “Send” visible sur la page): https://careers.maia-space.com/o/flight-engineering-software-development-and-validation-engineer?lang=en
- Pourquoi c’est un fit “technique”:
  - 6DoF simulation + intégration de modèles physiques + campagnes de simulation + validation GNC: coeur “simulation & validation”.
  - Stack affichée `Matlab`, `C/C++`, `Python`: ton angle “scientific software + validation” reste crédible.
- Risque/gap principal:
  - Pré-requis affichés “5–7 years” + domaine spatial/GNC → vrai gap seniorité/domaine; candidature seulement si tu acceptes un positionnement “adjacent / learning curve”.

#### CV title (tailored)

`Ingénieure simulation & validation (Python/C++) — corrélation modèle↔mesure, diagnostics`

#### Summary (tailored)

Ingénieure simulation/validation issue de la physique expérimentale: je construis des workflows `Python/C++` qui relient simulation et données de mesure via calibration/correction, stress tests et diagnostics reproductibles.
Je peux contribuer à structurer des campagnes de simulation/validation (critères, métriques, exploitation des écarts), tout en restant factuelle sur un gap GNC.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built and adapted `Geant4/C++` simulation code for detector/system response studies, including geometry and analysis outputs.
2. Combined test data, simulation, and response maps to model measurement-chain behaviour and quantify system-level effects (e.g., resolution contributions).
3. Developed `ROOT/C++` calibration and correction workflows to reduce structured bias; compared performance before/after across conditions.
4. Implemented likelihood-based models and joint fits to estimate latent parameters under finite resolution and biased observations.
5. Ran sensitivity/robustness studies by varying model assumptions and quantifying impact on outputs.
6. Built monitoring workflows to validate calibration/reconstruction quality; traced anomalies to root causes and drove corrective actions.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — hors-cible (QA générique / consulting)

- ELEPHANT Technologies — Ingénieur en test et validation (Nantes, Hybride): offre orientée QA/consulting (Robotframework/Selenium/Jenkins, ISTQB) sans angle “simulation↔mesure / systèmes physiques” → hors-track.
  - Offre (formulaire “Envoyer” visible sur la page au `2026-04-24`): https://elephanttechnologies.recruitee.com/o/ingenieur-en-test-et-validation

### Exclus — hors-cible (intégration/PS) malgré apply vérifiable

- Outsight — Python Backend Developer (Paris, Hybrid): rôle “Professional Services / intégration IAM + BI + data flows” plutôt que simulation/validation systèmes physiques → hors-track.
  - Offre: https://jobs.lever.co/outsight/214bac75-5f85-4988-99c8-bf0ab834a5d8
  - Candidature (formulaire “Submit application” visible au `2026-04-24`): https://jobs.lever.co/outsight/214bac75-5f85-4988-99c8-bf0ab834a5d8/apply

### Exclus — statut “apply” non vérifiable

- KONTRON Transportation — pages carrière Recruitee: l’URL tentative redirige vers une page marketing Recruitee (pas de liste d’offres visible) au moment de la vérification (`2026-04-24`) → **exclu** (“apply” non vérifiable).
  - Page testée: https://kontrontransportation.recruitee.com/

### Exclus — hors-cible (niveau/stage)

- HEMERIA — Stage Ingénieur calcul CFD (Ayguesvives): stage/CFD mécanique des fluides (profil + niveau non alignés) → hors-track.
  - Offre (bouton “Postuler” visible au `2026-04-24`): https://hemeriagroup.recruitee.com/o/stage-ingenieur-calcul-cfd-fh
