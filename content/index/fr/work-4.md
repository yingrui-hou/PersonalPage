---
number: 04
homepage_order: 2
collapsible: true
title: Simulation de capteur contrainte par les mesures
tags: Geant4 | Essais sous faisceau | Calibration
methods: Simulation C++, cartes de réponse, ajustement des courbes de résolution
impact: Contribution des non-uniformités au terme constant inférieure à 1 % dans l’étude du petit prototype.
industry: Jumeaux numériques | Validation simulation-essais | Analyse capteur
---
**Construction d’une chaîne reliant essais sous faisceau et simulation pour quantifier l’effet de la non-uniformité d’un détecteur sur sa résolution.**

![Comparaison de résolution](assets/selected-work/work-4/resolution.png "Comparaison entre réponse mesurée et réponse uniforme idéalisée.")

### Réalisation personnelle
- Exploitation des mesures du faisceau de juin 2024 et du suivi de position pour construire une carte effective du rendement lumineux.
- Injection de cette carte dans la simulation Geant4 de dépôt d’énergie, avec calcul de la réponse événement par événement.
- Implémentation de la géométrie, du suivi des interactions et de la logique de réponse en C++ ; ajustement des courbes de résolution.

![Banc d’essai](assets/selected-work/work-4/tbArch.png "Chaîne de mesure du prototype.")
![Prototype](assets/selected-work/work-4/troll_2.png "Petit prototype GRAiNITA.")
![Construction de la carte de réponse](assets/selected-work/work-4/to_have_nPE_map.png "Des mesures spatialisées à l’entrée du modèle.")

### Résultat et transfert
Contribution des non-uniformités au terme constant inférieure à 1 % dans cette étude du premier prototype. La démarche mesure → modèle → validation est transférable au développement de jumeaux numériques ; elle n’établit pas un déploiement industriel connecté en temps réel.
### Publication
Étude collective : *Studying the GRAiNITA concept: first test beam results*, [DOI](https://doi.org/10.1088/1748-0221/21/03/P03048).
