# Shortlist de postes ciblés: Data Scientist (industrie / R&D)

Date de vérification (Europe/Paris): `2026-04-27` (dernière vérification: `12:05` CEST)

Cette shortlist ne conserve **que** des offres pour lesquelles j’ai pu:
1) ouvrir la page de l’offre, puis
2) ouvrir le chemin officiel de candidature (ATS / “Apply”) et constater qu’un dépôt est possible (formulaire + bouton “Submit/Send/Envoyer” visible).

## Positionnement & logique de tri (rappel)

- Angle candidat (preuves dans ce repo, notamment `cv.md` / `resume.html`): `modélisation probabiliste`, `calibration/correction`, `validation sous bruit/biais`, `domain shift`, pipelines `Python/C++` + discipline de reproductibilité.
- Cible: Data Scientist *industrial/R&D ou physical-systems-adjacent* quand possible (énergie, monitoring, séries temporelles, optimisation, capteurs), en évitant BI/reporting pur.
- Déprioriser: BI/dashboards sans contenu modèle/validation; DS “marketing/CRM”; rôles purement consulting génériques sans ownership technique.

### Priorités

- `A` = DS orienté systèmes/monitoring/industrial + transfert direct
- `B` = DS intéressant mais plus éloigné / plus produit / moins “physical systems”
- `C` = stretch (niveau/seniority/management) ou contexte moins aligné

---

## Bucket A — priorité haute

### A1. Kayrros — Senior Data Scientist F/H (Paris, Hybrid)

- Liens (vérifiés le `2026-04-27`):
  - Offre + candidature (Recruitee, formulaire “Send” visible sur la page): https://kayrros1.recruitee.com/o/senior-data-scientist-fh
- Pourquoi c’est un fit:
  - Monitoring/risque environnemental sur mesures indirectes + incertitude + peu de vérité terrain → très compatible avec ton axe `validation/calibration/robustesse`.
  - Place pour une posture “modèle crédible” (stress tests, diagnostics, garde-fous) plutôt que dashboarding.
- Risque/gap principal:
  - Domaine remote-sensing / vision possible + étiquette “Senior”: cadrer honnêtement et mettre en avant la rigueur de validation sur signaux bruités.

#### CV title (tailored)

`Data Scientist — Validation & calibration under uncertainty (monitoring, Python/C++)`

#### Summary (tailored)

Data scientist orientée crédibilité modèle, avec un background en physique expérimentale: je construis et valide des modèles sur des données bruitées/biaisées (peu de vérité terrain), via calibration/correction, stress tests et diagnostics reproductibles.
Je vise des sujets monitoring/risque/environnement où l’incertitude et la qualité des mesures sont centrales.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built reusable `C++/Python` workflows for inference and validation on noisy datasets where direct event-level truth was unavailable.
2. Implemented likelihood-based models and joint fits to estimate latent parameters under mismatch, finite resolution, and biased observations.
3. Developed calibration/correction workflows to reduce structured bias and compare before/after performance across operating conditions.
4. Built monitoring/validation pipelines that surfaced anomalies and supported root-cause diagnosis; drove concrete follow-up actions.
5. Aligned simulated and observed datasets through reweighting / control-sample calibration to mitigate dataset shift before decisions.
6. Ran sensitivity analyses and robustness checks; communicated uncertainty and limitations clearly to stakeholders.

### A2. Bigblue — Senior Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-27`):
  - Offre (Lever): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/bigblue/9151cdb5-d6aa-41c7-a06e-c8236c247f8a/apply
- Pourquoi c’est un fit:
  - Problèmes “ops / décision sous contraintes” (ETA, optimisation, expérimentation) → valorise ton axe “validation robuste + monitoring + biais/shift”.
  - Rôle orienté ownership (problème→solution→expérimentation), pas BI pur.
- Risque/gap principal:
  - Poste affiché “5–10y”: à cadrer franchement; se positionner sur rigueur validation + ownership technique.

#### CV title (tailored)

`Data Scientist — Robust validation & monitoring for real-world ops (Python/C++)`

#### Summary (tailored)

Data scientist orientée production/ops, spécialisée dans la validation et la calibration de modèles sur données réelles imparfaites (bruit, biais, shift), avec des workflows `Python/C++` reproductibles.
Je transforme des écarts observés en diagnostics et garde-fous (monitoring, stress tests, corrections) pour des décisions fiables.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Implemented robustness checks under bias and dataset shift; quantified sensitivity to assumptions and failure modes.
2. Built monitoring/validation workflows that exposed anomalies and supported root-cause diagnosis (system vs software vs data).
3. Developed calibration/correction workflows to reduce structured bias; quantified before/after improvements.
4. Delivered reproducible pipelines with traceable outputs and documented checks for reliable comparisons across iterations.
5. Designed feature selection / stability strategies to improve signal-to-noise ratio and prevent brittle models.
6. Communicated uncertainty and trade-offs clearly to keep operational decisions aligned with evidence.

---

## Bucket B — bon fit avec gap réel

### B1. BlaBlaCar — Data Scientist - Entry Level (Paris, Hybrid)

- Liens (vérifiés le `2026-04-27`):
  - Offre (Lever): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/blablacar/6f33bec1-681f-4eaa-8e68-e894cd6fb37d/apply
- Pourquoi c’est potentiellement intéressant:
  - DS “production” (ML en prod + automatisation) où ton axe **validation/robustesse/monitoring** peut être différenciant.
- Risque/gap principal:
  - Domaine plutôt trust/fraud/modération/GenAI (moins industrial/physical-systems-adjacent).

#### CV title (tailored)

`Data Scientist — Robust validation & monitoring for real-world ML (Python/C++)`

#### Summary (tailored)

Data scientist issue de la physique expérimentale: j’apporte une rigueur de validation et de calibration sur données imparfaites, avec monitoring et diagnostics reproductibles pour réduire les erreurs silencieuses en production.
Je peux contribuer sur la partie “model credibility” et la boucle d’amélioration continue.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Built monitoring/validation workflows that surfaced anomalies and supported root-cause diagnosis (system vs software vs data).
2. Implemented robustness checks under bias and dataset shift; quantified failure modes and limitations.
3. Developed calibration/correction workflows to reduce structured bias and compare before/after performance.
4. Delivered reproducible pipelines (versioned code, documented checks) enabling reliable comparisons across iterations.
5. Implemented probabilistic modeling (likelihood-based inference) when uncertainty and imperfect observation dominated.
6. Communicated uncertainty and trade-offs clearly to prevent overconfident decisions.

### B2. Mistral AI — Data Scientist (Paris, On-site)

- Liens (vérifiés le `2026-04-27`):
  - Offre (Lever): https://jobs.lever.co/mistral/bf5bcae2-839b-492e-a5bc-11d4427ee843
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/mistral/bf5bcae2-839b-492e-a5bc-11d4427ee843/apply
- Pourquoi c’est potentiellement intéressant:
  - Forte composante stats/expérimentation/évaluation: ton axe “validation robuste + diagnostics” peut apporter de la valeur.
- Risque/gap principal:
  - Contexte “product/AI” (moins industriel/physical-systems); garder le discours centré sur rigueur d’évaluation et limitations.

#### CV title (tailored)

`Data Scientist — Robust evaluation & validation under uncertainty (Python/C++)`

#### Summary (tailored)

Profil data issu de la physique expérimentale: je construis des méthodes d’évaluation et de validation robustes sur données réelles imparfaites (bruit, biais, shift), avec des workflows `Python/C++` reproductibles.
Je peux contribuer sur le cadrage des métriques, stress tests, diagnostics et la crédibilité des conclusions.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Implemented likelihood-based inference and sensitivity studies to quantify uncertainty and avoid overconfident conclusions.
2. Built monitoring/validation pipelines that exposed anomalies and supported root-cause diagnosis.
3. Corrected measurement bias and resolution effects through calibration using simulation and control datasets.
4. Mitigated dataset shift by aligning simulated and observed distributions (reweighting) before downstream evaluation.
5. Delivered reproducible `Python/C++` pipelines with versioned code and documented checks.
6. Communicated limitations and trade-offs clearly to keep decisions aligned with evidence.

---

## Bucket C — stretch assumé

### C1. Octopus Energy France — Lead Data Scientist (Paris, Hybrid)

- Liens (vérifiés le `2026-04-27`):
  - Offre (Lever): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429
  - Candidature (formulaire “Submit application”): https://jobs.lever.co/octoenergy/3735b846-263a-4d61-9f1d-cacd1b682429/apply
- Pourquoi c’est intéressant:
  - Secteur énergie + sujets data → possibilité de valoriser validation, expérimentation, et “impact mesuré”.
- Risque/gap principal:
  - Poste “Lead” (management + forte orientation commerciale/BI + prérequis management) → candidature seulement si tu acceptes un stretch management/seniority.

#### CV title (tailored)

`Data Scientist — Model credibility & validation under uncertainty (energy context)`

#### Summary (tailored)

Profil data orienté crédibilité: je rends des modèles exploitables sur données réelles via calibration/correction, validation robuste, diagnostics et monitoring.
Je vise des équipes où la rigueur de validation compte autant que la performance nominale — tout en assumant que ce rôle est un stretch “Lead/management”.

#### Top 6 bullets à mettre en tête (à réécrire/mettre en avant)

1. Designed robust validation under mismatch/shift; prevented overconfident conclusions in noisy regimes.
2. Developed calibration/correction workflows with quantified before/after improvements across operating conditions.
3. Built monitoring pipelines that surfaced anomalies and drove corrective actions (data, model, or software fixes).
4. Implemented probabilistic inference (likelihood-based models, joint fits) under imperfect observations.
5. Delivered reproducible workflows in shared codebases with review discipline and documented checks.
6. Communicated uncertainty and trade-offs clearly to keep decisions aligned with evidence.

---

## Postes vérifiés mais exclus (fermés / hors-cible / statut “apply” non vérifiable)

### Exclus — statut “apply” non vérifiable (malgré intérêt)

- Safran — Data Scientist Health Monitoring F/H (France/Châteaufort): page offre accessible mais impossible de confirmer le chemin officiel de candidature (erreur “cache miss” côté outil lors de l’ouverture du lien “Apply” le `2026-04-27`) → **exclu** (“apply” non vérifiable).
  - Offre repérée: https://www.safran-group.com/jobs/france/chateaufort/data-scientist-health-monitoring-fh-164168

### Exclus — repérés via LinkedIn mais non vérifiables (login wall)

- Exemples: offres LinkedIn “Data Scientist (Paris)” repérées mais impossibles à vérifier côté chemin officiel de candidature sans connexion LinkedIn → **exclues** (“apply” non vérifiable).

### Exclus — hors-cible (exemples)

- Valeuriad — Data Scientist (Paris): contexte ESN/consulting multi-clients, moins “industrial/R&D ownership” → dépriorisé pour cette track.
  - Offre repérée: https://jobs.lever.co/valeuriad/590780ba-bbf9-4fca-ab68-2f87be44ebd0
