---
number: 01
homepage_order: 8
homepage_group: secondary
collapsible: true
title: Analyse de signaux faibles
tags: Modélisation statistique | Incertitudes | Validation
methods: Ajustements de vraisemblance, échantillons de contrôle, extraction automatisée
impact: Chaîne reproductible d’extraction de signaux rares avec contrôles de stabilité.
industry: Analyse d’événements rares | Données faiblement étiquetées
---
Développement d’un logiciel d’analyse Python/C++ réutilisable pour estimer un signal faible dans des données bruitées et mélangées.

### Problème
Le signal ne pouvait pas être identifié avec certitude pour chaque observation. Il fallait estimer sa contribution en tenant compte du bruit de fond et des incertitudes de mesure.

### Ma contribution
- Construction de modèles de vraisemblance pour séparer statistiquement signal et bruit de fond.
- Automatisation de la sélection, de l’estimation du signal et des comparaisons avec des échantillons de référence en Python/C++/ROOT.
- Vérification des corrélations entre variables et paramètres ajustés, puis des biais dans des expériences simulées répétées, pour l’évaluation des incertitudes.

### Validation et résultat
Étude de la stabilité des ajustements entre jeux de données et critères de sélection. Les contrôles effectués n’ont révélé ni dépendance problématique ni biais ; le workflow a servi à une mesure dédiée. Leur portée reste limitée aux effets effectivement testés.

### Illustrations

![Ajustement du signal et du bruit de fond](assets/selected-work/work-1/BToVG.png "Extraction d’un pic de signal par un ajustement explicite signal-bruit de fond.")
