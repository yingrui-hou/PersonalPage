# Shortlist de postes ciblés: Simulation / Validation / R&D systèmes physiques

Date de vérification (Europe/Paris): `2026-04-25` (dernière vérification: `09:36` CEST)

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
- `C` = stretch assumé (domaine très différent / prérequis manquants)

---

## Bucket A — priorité haute

### A1. Outsight — Customer Validation Engineer (Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre (Lever): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/outsight/d54de068-6441-468e-9e4f-1131e7a6adf3/apply
- Pourquoi c’est un fit:
  - Validation/acceptance sur systèmes déployés (mesures + critères d’acceptation) avec outillage `Python` → mapping direct vers ton axe `validation/calibration/diagnostic`.
  - Problème “systèmes physiques + données bruitées + décision” (écarts attendu↔observé + boucle corrective).
- Risque/gap principal:
  - Contexte delivery/client + déplacements; à cadrer comme “validation strategy + tooling + reporting + boucle corrective”.

#### CV title (tailored)

`Ingénieure validation & calibration (Python/C++) — systèmes physiques / capteurs`

#### Summary (tailored)

Ingénieure R&D issue de la physique expérimentale, spécialisée dans la **validation** et la **calibration/correction** de modèles et pipelines sur données de mesure bruitées, via des workflows reproductibles en `Python/C++`.
J’identifie et quantifie les écarts “attendu vs observé”, puis je les transforme en diagnostics et actions (corrections, critères d’acceptation, monitoring).

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented likelihood-based models and joint fits to estimate latent parameters under mismatch, finite resolution, and biased observations.
3. Developed calibration/correction workflows to reduce structured bias; quantified before/after across operating conditions.
4. Built monitoring/validation pipelines comparing expected vs observed behaviour; surfaced anomalies and supported root-cause diagnosis.
5. Aligned simulated and observed datasets through reweighting and control-sample calibration before downstream acceptance decisions.
6. Ran sensitivity/robustness checks and communicated uncertainty clearly to keep acceptance decisions aligned with evidence.

### A2. Fairmat — Software Engineer - Robotics (Bouguenais/Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre (Lever): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091
  - Candidature (formulaire “Submit your application”): https://jobs.lever.co/Fairmat/674d5a79-e612-44dc-9e93-5efa5997e091/apply
- Pourquoi c’est un fit:
  - Dév `C++/Python` sur cellules robotisées industrielles + **tests/validation/non-régression** + analyse de données prod → très cohérent avec ton axe “validation + diagnostic + boucle corrective”.
  - Forte composante “terrain + mesures + anomalies” : transfert naturel de ton expérience sur systèmes de mesure bruités.
- Risque/gap principal:
  - Stack `ROS`/robotique et support production (rythme ticket) → gap probable; se positionner sur “validation, tests, robustesse, triage” et apprendre `ROS` de façon ciblée.

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
5. Worked in shared codebases with review discipline; shipped reusable components used for validation and diagnostics.
6. Modelled measurement-chain behaviour (signal chain / sensor response) to interpret test data and guide corrective actions.

---

## Bucket B — bon fit avec gap réel

### B1. Kontron Transportation — Ingénieur Intégration/Validation Réseaux Télécoms (Montigny-le-Bretonneux, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre + candidature (formulaire “Envoyer” visible sur la page): https://kontrontransportation.recruitee.com/o/ingenieur-integrationvalidation-reseaux-telecoms
- Pourquoi c’est un fit:
  - Rôle **intégration + validation système** (stratégie de tests, exécution, analyse d’écarts, documentation) → transfert direct de ton axe “validation, diagnostic, robustesse”.
  - Contexte “systèmes critiques / exigences / conformité” où ta rigueur de validation et traçabilité est un avantage.
- Risque/gap principal:
  - Domaine télécom (2G/4G/5G/IMS/3GPP, virtualisation réseau) → gap domaine/stack; candidature uniquement si tu acceptes un repositionnement “validation engineering” + montée en compétence ciblée.

#### CV title (tailored)

`Ingénieure validation système (Python/C++) — tests, diagnostic, traçabilité, exigences`

#### Summary (tailored)

Ingénieure issue de la physique expérimentale, spécialisée dans la validation et la calibration/correction de systèmes où le comportement réel n’est observable qu’indirectement via des mesures bruitées.
Je construis des workflows `Python/C++` reproductibles pour définir des critères, comparer attendu↔observé, diagnostiquer les écarts et fermer la boucle par des actions correctives — tout en assumant un gap “télécom/3GPP”.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Designed validation approaches under imperfect observations (noise/bias) and quantified uncertainties to avoid overconfident conclusions.
2. Built monitoring pipelines comparing expected vs observed behaviour; traced anomalies to root causes and drove follow-up actions.
3. Developed calibration/correction workflows with before/after comparisons across operating conditions.
4. Delivered reproducible analysis tooling (`C++/Python`, versioned code) enabling reliable reruns and auditability.
5. Ran sensitivity analyses by varying assumptions and measuring impact on outputs; documented limitations clearly.
6. Communicated results in decision-ready form (metrics, trade-offs, risk framing) for stakeholders.

### B2. Alice & Bob — Workflow Engineer - Calibration (Paris, Hybrid)

- Liens (vérifiés le `2026-04-25`):
  - Offre (Lever): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/alice-bob/f4349231-2406-4892-a646-5f6942e71070/apply
- Pourquoi c’est un fit:
  - Sujet “workflows fiables + contrôles qualité + auditabilité + (hardware-in-the-loop)” = ton axe “validation/calibration sous bruit/biais + monitoring/diagnostic”.
  - Forte composante “orchestration + checks + recovery” où ton approche “stress tests + validation” est transférable.
- Risque/gap principal:
  - Attentes seniorité (5+ ans) + expérience orchestration/DAG/hardware control; cadrer l’impact sur “validation, monitoring, robustness, tooling”.

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

### C1. MaiaSpace — Flight Engineering Software Development and Validation Engineer (Paris — La Défense, On-site)

- Liens (vérifiés le `2026-04-25`):
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

1. Built and maintained simulation-to-analysis pipelines in `C++/Python`, designed for large-scale data and reproducible comparisons.
2. Modelled measurement-chain behaviour and calibrated parameters using simulation and experimental/control datasets.
3. Implemented likelihood-based models and joint fits to estimate latent parameters under finite resolution and biased observations.
4. Developed calibration/correction workflows to reduce structured bias; compared before/after across operating conditions.
5. Ran sensitivity/robustness studies by varying model assumptions and quantifying impact on outputs.
6. Built monitoring workflows to validate calibration/reconstruction quality; traced anomalies to root causes and drove corrective actions.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — statut “apply” non vérifiable

- Verkor — Aging Modelling Engineer M/F (Grenoble): page offre accessible mais le chemin officiel “Apply” n’a pas pu être vérifié au moment du check (`2026-04-25`) à cause d’une erreur de récupération côté outil → **exclu**.
  - Offre repérée: https://jobs.lever.co/verkor/c0ef67db-8ffd-4078-b30d-63e1f1c78ccb

### Exclus — hors-cible / FEA/meshing dominant

- NAAREA — Ingénieur calcul / simulation mécanique expérimenté (Abaqus, Nanterre): rôle très orienté FEA/mécanique + seniorité élevée → dépriorisé/hors-track.
  - Offre (formulaire “Postuler” visible sur la page au crawl): https://naarea.recruitee.com/o/ingenieur-en-simulation-mecanique-experimente-hf?lang=fr

### Exclus — senior/management dominant

- Outsight — Simulation Unity Engineering Manager (Paris): rôle `Engineering Manager` + Unity/C# 3D simulation; intéressant mais trop senior/management pour ce track de candidatures ciblées.
  - Offre: https://jobs.lever.co/outsight/a48fa3c1-28f9-4589-9158-d2f2dfa2db3a

