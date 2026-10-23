---
number: 03
homepage_order: 1
collapsible: true
title: ML et écarts entre jeux de données
tags: CatBoost | Repondération | Validation croisée
methods: échantillons de contrôle, corrélations, repondération par gradient boosting, ROC/AUC et optimisation du seuil
impact: Relier la qualité des données, le choix du modèle et le seuil à la précision d’une mesure de signal rare.
industry: ML appliqué | Décalage de distribution | Optimisation de décision
---
Entraînement d’un classificateur CatBoost pour sélectionner des signaux rares, avec alignement simulation–mesures et choix du seuil selon l’objectif de mesure.

### Problème
L’entraînement associait des signaux simulés et du bruit de fond issu de mesures. Les écarts de distribution et le nombre limité d’exemples étiquetés imposaient une validation attentive.

### Ma contribution
- Sélection des variables à partir de la connaissance du système, des corrélations et de leur importance dans le modèle.
- Comparaison avec des mesures de référence et repondération hep_ml avant l’entraînement.
- Validation croisée à cinq plis pour sélectionner les variables et régler les hyperparamètres ; diagnostics KS entre apprentissage et test.
- Recherche du seuil avec `S / sqrt(S + B)`, à partir des effectifs attendus de signal et de bruit de fond et des efficacités de sélection.

### Validation et résultat
Application du seuil aux données de l’analyse et contrôle de la réduction du bruit de fond. Les performances proviennent de la validation croisée utilisée pendant le développement, sans échantillon étiqueté final indépendant. Les efficacités du seuil utilisent les événements d’apprentissage et de test réunis après des contrôles KS compatibles. Cela ne constitue pas une estimation finale indépendante de la généralisation.

### Illustrations

![Performance de sélection](assets/selected-work/work-3/bkg_veto_performance.png "La comparaison Run 1 montre une réduction du fond après sélection BDT, avec maintien du pic de signal. Figure d’étude LHCb unofficial ; aucun gain chiffré n’est déduit de l’image.")
![Validation entraînement/test](assets/selected-work/work-3/train-test.png "Accord global des distributions de réponse entraînement/test pour les deux classes ; diagnostic de surapprentissage, sans garantie d’évaluation indépendante.")
![Importance des variables](assets/selected-work/work-3/feature_importance.png "L’importance et les diagnostics de séparation ont guidé la simplification du modèle.")
