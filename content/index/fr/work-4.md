---
number: 04
homepage_order: 2
collapsible: true
title: Simulation de capteurs et automatisation des essais
tags: Geant4 | Mesures | Automatisation Shell
methods: Simulation C++, cartes de réponse, ajustement des courbes de résolution
impact: Contribution des non-uniformités au terme constant inférieure à 1 % dans l’étude du petit prototype.
industry: Jumeaux numériques | Validation simulation-essais | Analyse capteur
---
Intégration de mesures de prototype dans une simulation et automatisation de l’acquisition, de la calibration et des premiers contrôles qualité.

### Problème
Les variations spatiales de réponse du capteur affectaient la résolution. La simulation devait intégrer une carte de réponse mesurée pour représenter le prototype.

### Ma contribution
- Implémentation de la géométrie et de la réponse du capteur en Geant4/C++, avec intégration des cartes issues des essais sous faisceau.
- Développement d’un pipeline Shell reliant des algorithmes existants de lecture, de suivi des trajectoires et de calibration temporelle au stockage et aux contrôles qualité.
- Participation à l’installation et à l’acquisition sur site ; contribution aux ajustements et aux corrections des effets de mesure.

### Validation et résultat
Comparaison de la résolution simulée avec une réponse mesurée et une réponse uniforme. L’étude du prototype a quantifié une contribution de la non-uniformité inférieure à 1 % au terme constant de la résolution. Le workflow relie essais physiques, simulation et évaluation de conception.

### Illustrations

![Comparaison de résolution](assets/selected-work/work-4/resolution.png "Comparaison entre réponse mesurée et réponse uniforme idéalisée.")
![Banc d’essai](assets/selected-work/work-4/tbArch.png "Chaîne de mesure du prototype.")
![Prototype](assets/selected-work/work-4/troll_2.png "Petit prototype GRAiNITA.")
![Construction de la carte de réponse](assets/selected-work/work-4/to_have_nPE_map.png "Des mesures spatialisées à l’entrée du modèle.")

### Publications

Étude collective : *Studying the GRAiNITA concept: first test beam results*, [DOI](https://doi.org/10.1088/1748-0221/21/03/P03048).
