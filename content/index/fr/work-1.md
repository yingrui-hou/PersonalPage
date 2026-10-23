---
number: 01
homepage_order: 8
homepage_group: secondary
collapsible: true
title: Inférence de signaux faibles
tags: Modèles de mélange | Maximum de vraisemblance | Validation statistique
methods: Ajustements de vraisemblance, échantillons de contrôle, extraction automatisée
impact: Chaîne reproductible d’extraction de signaux rares avec contrôles de stabilité.
industry: Analyse d’événements rares | Données faiblement étiquetées
---
**Développement d’une chaîne C++/Python/ROOT pour extraire un signal faible dans des données dominées par le bruit de fond, sans vérité terrain par événement.**

![Ajustement du signal et du bruit de fond](assets/selected-work/work-1/BToVG.png "Extraction d’un pic de signal par un ajustement explicite signal-bruit de fond.")

### Problème
Séparer un signal rare du bruit combinatoire tout en contrôlant la stabilité de l’estimation.
### Réalisation personnelle
- Implémentation d’ajustements de vraisemblance signal-bruit de fond et extraction des rendements.
- Automatisation de la présélection, des ajustements et des vérifications de rapports de branchement dans des scripts d’analyse.
- Validation sur un canal de contrôle plus abondant et suivi des rendements, largeurs et ajustements selon les sélections.
### Pratique personnelle de validation
Démarche progressive, en commençant généralement par le contrôle le plus simple :
1. Examen des coefficients de corrélation entre variables pour repérer les associations visibles.
2. Inspection des matrices de corrélation des ajustements pour étudier les relations entre paramètres et composantes du modèle.
3. Pseudo-expériences pour étudier les variations du biais des distributions de pull selon le modèle et les conditions de sélection.

Cette démarche associe des diagnostics simples à des études de sensibilité par simulation pour examiner la fiabilité du résultat inféré.

Ces contrôles n’ont pas mis en évidence de problème dans les analyses décrites. Je les ai inclus dans l’évaluation des incertitudes systématiques de chaque analyse.

### Résultat
Une méthode réutilisable et vérifiable, employée dans une mesure de rapport de branchement. Les détails de la note de collaboration restent internes.
