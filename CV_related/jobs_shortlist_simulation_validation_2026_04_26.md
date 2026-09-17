# Shortlist de postes ciblés: Simulation / Validation / R&D systèmes physiques

Date de vérification (Europe/Paris): `2026-04-26` (dernière vérification: `09:34` CEST)

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Cible: `ingénierie simulation/validation` + `scientific software` pour systèmes physiques instrumentés (calibration, validation, corrélation essai↔modèle, root-cause).
- Angle candidat (preuves dans ce repo, notamment `cv.md` / `resume.html`): workflows `Python/C++`, calibration/correction, validation sous bruit/biais, simulation↔mesure, monitoring & diagnostic menant à actions.
- Déprioriser: `meshing/SALOME/geometry-kernel`, rôles purement “maillage/FEA mécanique”, BI/dashboards, backend générique sans angle systèmes physiques.

### Priorités

- `A` = fit direct + transfert très clair
- `B` = bon fit mais gap (stack/domaine/seniority)
- `C` = stretch assumé (domaine très différent / prérequis manquants / seniorité)

---

## Bucket A — priorité haute

### A1. Outsight — Customer Validation Engineer (Paris, Hybrid)

- Liens (vérifiés le `2026-04-26`):
  - Offre (Lever): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3/apply
- Pourquoi c’est un fit:
  - Cœur du rôle = **acceptance/validation** sur systèmes déployés, avec outillage `Python` + métriques + analyse d’écarts → mapping direct sur ton axe `validation/calibration/diagnostic`.
  - Contexte “systèmes physiques + mesures bruitées + décisions” (attendu↔observé + boucle corrective).
- Risque/gap principal:
  - Composante delivery/client + déplacements; cadrer ta valeur sur “test strategy + tooling + analyse + reporting”.

#### CV title (tailored)

`Ingénieure validation & calibration (Python/C++) — systèmes physiques / capteurs`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la **validation** et la **calibration/correction** de modèles et pipelines sur données de mesure bruitées, via des workflows reproductibles en `Python/C++`.
Je quantifie les écarts “attendu vs observé”, puis je les transforme en diagnostics et actions (corrections, critères d’acceptation, monitoring).

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented likelihood-based models and joint fits to estimate latent parameters under mismatch, finite resolution, and biased observations.
3. Developed calibration/correction workflows to reduce structured bias; quantified before/after across operating conditions.
4. Built monitoring/validation pipelines comparing expected vs observed behaviour; surfaced anomalies and supported root-cause diagnosis.
5. Aligned simulated and observed datasets through reweighting and control-sample calibration before downstream acceptance decisions.
6. Ran sensitivity/robustness checks and communicated uncertainty clearly to keep acceptance decisions aligned with evidence.

### A2. Fairmat — Software Engineer - Robotics (Bouguenais/Paris, Hybrid)

- Liens (vérifiés le `2026-04-26`):
  - Offre (Lever): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091/apply
- Pourquoi c’est un fit:
  - Dév `C++/Python` sur cellules robotisées + **tests/validation/non-régression** + analyse de données prod → très aligné avec ton axe “validation + diagnostic + boucle corrective”.
  - Rôle “terrain + mesures + anomalies” cohérent avec ton background sur systèmes instrumentés.
- Risque/gap principal:
  - Stack `ROS`/robotique + support production: à assumer comme gap partiel; se positionner sur validation, robustesse, triage, et apprentissage `ROS` ciblé.

#### CV title (tailored)

`Scientific software / validation engineer (C++/Python) — tests, diagnostic, systèmes industriels`

#### Summary (tailored)

Scientific software engineer orientée fiabilité: je construis des workflows `C++/Python` robustes et traçables pour relier logiciels/modèles et comportements observés via mesures, puis transformer les écarts en actions (correctifs, tests, monitoring).
Je peux contribuer fortement sur la partie validation/diagnostic et outillage de non-régression, tout en restant factuelle sur un gap `ROS`.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that surfaced anomalies and supported root-cause diagnosis (system vs software vs data).
2. Delivered reproducible pipelines with traceable outputs and documented checks enabling reliable reruns and comparisons.
3. Developed calibration/correction tooling to reduce structured bias and compare performance before/after across operating conditions.
4. Implemented robustness checks under mismatch/shift; quantified sensitivity to assumptions and failure modes.
5. Worked in shared codebases with review discipline; shipped reusable components used for validation and diagnostics.
6. Modelled measurement-chain behaviour (signal chain / sensor response) to interpret test data and guide corrective actions.

---

## Bucket B — bon fit avec gap réel

### B1. Kontron Transportation — Ingénieur Intégration/Validation Réseaux Télécoms (Montigny-le-Bretonneux, Hybride)

- Liens (vérifiés le `2026-04-26`):
  - Offre + candidature (formulaire “Envoyer” visible sur la page): https://kontrontransportation.recruitee.com/o/ingenieur-integrationvalidation-reseaux-telecoms
- Pourquoi c’est un fit:
  - Rôle **intégration + validation système**: stratégie de tests, exécution, analyse d’anomalies, suivi correction, rapports → transfert direct de ton axe “validation + root-cause + rigueur de preuves”.
  - Environnement “systèmes critiques” où la discipline de reproductibilité et de diagnostic est centrale.
- Risque/gap principal:
  - Domaine télécom (2G/4G/5G/3GPP) + outillage réseau = vrai gap domaine; candidater en cadrant le transfert “méthode de validation/diagnostic” + montée en compétence.

#### CV title (tailored)

`Ingénieure intégration & validation — tests, diagnostic, workflows reproductibles (Python/C++)`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la **validation** sous bruit/biais et le diagnostic d’écarts “attendu vs observé”, via des workflows reproductibles en `Python/C++`.
Je structure des campagnes de validation (métriques, stress tests, reporting) et j’investigue les anomalies jusqu’à des actions correctives.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that exposed anomalies and supported root-cause diagnosis (system vs software vs data).
2. Ran sensitivity/robustness checks by varying assumptions and quantifying impact on outputs; documented limitations clearly.
3. Delivered reproducible pipelines with traceable outputs and documented checks enabling reliable reruns and comparisons.
4. Implemented calibration/correction workflows to reduce structured bias; quantified before/after across operating conditions.
5. Communicated results in decision-ready form (metrics, trade-offs, risk framing) and wrote structured technical reports.
6. Worked in shared codebases with version control and review discipline; maintained reusable validation components.

### B2. Alice & Bob — Workflow Engineer - Calibration (H/F) (Paris, Hybrid)

- Liens (vérifiés le `2026-04-26`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070/apply
- Pourquoi c’est un fit:
  - Sujet “calibration workflow credibility” (checks, recovery, auditabilité) = ton axe **calibration/validation sous incertitude** + diagnostics reproductibles.
  - Forte composante “transformer des écarts en actions correctives” dans un contexte hardware.
- Risque/gap principal:
  - Pré-requis affichés “5+ ans” + expérience orchestrateurs/DAG/hardware control: à cadrer honnêtement comme **stretch** (mais transfert méthode validation très fort).

#### CV title (tailored)

`Scientific software engineer — calibration/validation workflows & monitoring (Python/C++)`

#### Summary (tailored)

Ingénieure issue de la physique expérimentale, spécialisée dans la **calibration** et la **validation** de pipelines sur systèmes de mesure bruités, avec une approche “workflow credibility” (checks, monitoring, diagnostics, corrections).
Je rends des procédures de calibration plus fiables et actionnables en fermant la boucle entre écarts observés et actions correctives.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` workflows for validation and inference under noisy measurements with limited ground truth.
2. Developed calibration/correction workflows that reduced structured bias; quantified before/after improvements across regimes.
3. Built monitoring pipelines that exposed anomalies; traced issues to system behaviour vs software and triggered follow-up fixes.
4. Implemented robustness/stress checks under mismatch/shift to prevent overconfident conclusions.
5. Delivered reproducible workflows with traceability (versioned code, documented checks) enabling auditability.
6. Aligned simulation constraints and measurement constraints to improve model credibility (simulation-to-data alignment, correction workflows).

---

## Bucket C — stretch assumé

### C1. MaiaSpace — Flight Engineering Software Development and Validation Engineer (Paris - La Défense, On-site)

- Liens (vérifiés le `2026-04-26`):
  - Offre + candidature (formulaire “Send” visible sur la page): https://careers.maia-space.com/o/flight-engineering-software-development-and-validation-engineer?lang=en
- Pourquoi c’est un fit “technique”:
  - 6DoF simulation + campagnes de simulation + validation d’algos → cœur “simulation & validation”.
  - Stack affichée `Matlab`, `C/C++`, `Python`: ton angle “scientific software + validation” reste crédible.
- Risque/gap principal:
  - Domaine spatial/GNC + niveau d’expérience affiché (“5–7 years”) → vrai gap domaine/seniority; candidater seulement si tu acceptes un stretch.

#### CV title (tailored)

`Ingénieure simulation & validation (Python/C++) — corrélation modèle↔mesure, diagnostics`

#### Summary (tailored)

Ingénieure simulation/validation issue de la physique expérimentale: je construis des workflows `Python/C++` qui relient simulation et données de mesure via calibration/correction, stress tests et diagnostics reproductibles.
Je peux contribuer à structurer des campagnes de simulation/validation (critères, métriques, exploitation des écarts), tout en restant factuelle sur un gap GNC.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built and maintained simulation-to-analysis pipelines in `C++/Python`, designed for large-scale data and reproducible comparisons.
2. Modelled measurement-chain behaviour and calibrated parameters using simulation and experimental/control datasets.
3. Implemented likelihood-based models and joint fits to estimate latent parameters under finite resolution and biased observations.
4. Developed calibration/correction workflows to reduce structured bias; compared before/after across operating conditions.
5. Ran sensitivity/robustness studies by varying model assumptions and quantifying impact on outputs.
6. Built monitoring workflows to validate calibration/reconstruction quality; traced anomalies to root causes and drove corrective actions.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — hors-cible (domaine trop spécialisé vs profil actuel)

- Verkor — Battery validation Engineer (Grenoble): validation très orientée **Li-ion / matériaux / électrochimie** + prérequis explicitement batteries → gap domaine trop grand malgré “validation/root-cause” intéressant.
  - Offre (Lever): https://jobs.lever.co/verkor/f8185056-463c-486e-a562-45a7f10d6b4b
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/verkor/f8185056-463c-486e-a562-45a7f10d6b4b/apply

### Exclus — seniorité / stack trop exigeante

- MaiaSpace — Modeling, Simulation, HIL & Embedded Code Generation Engineer – MATLAB/Simulink Expert: très orienté `MATLAB/Simulink/Stateflow` expert + HIL + 5–10 ans → stretch trop fort.
  - Offre + candidature: https://careers.maia-space.com/o/modeling-simulation-hil-embedded-code-generation-engineer-matlabsimulink-expert?lang=fr

- Alice & Bob — Senior Software Engineer - Calibration Software: fit thématique (calibration) mais rôle “Senior” (5+ ans + architecture/CI/CD) → à garder seulement si tu assumes un stretch seniorité.
  - Offre (Lever): https://jobs.lever.co/alice-bob/b7386caa-70dd-4670-bb69-a5c97322332f
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/alice-bob/b7386caa-70dd-4670-bb69-a5c97322332f/apply

