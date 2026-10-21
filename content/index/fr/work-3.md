---
number: 03
homepage_order: 1
collapsible: true
title: Validation ML et adaptation de domaine
tags: CatBoost | Validation à cinq plis | Repondération | Seuil de décision
methods: échantillons de contrôle, corrélations, repondération par gradient boosting, ROC/AUC et optimisation du seuil
impact: Relier la qualité des données, le choix du modèle et le seuil à la précision d’une mesure de signal rare.
industry: ML appliqué | Décalage de distribution | Optimisation de décision
---
**Construction d’une sélection CatBoost du signal rare Bs → phi gamma : contrôles simulation-données, sélection de variables, entraînement/test à cinq plis et choix du seuil selon la précision attendue de la mesure.**

### Objectif et contribution personnelle
L’objectif était de sélectionner un signal rare parmi le bruit de fond combinatoire pour une mesure physique. J’ai développé la chaîne de sélection et de validation. J’ai utilisé des échantillons Monte-Carlo existants, avec simulation du détecteur et reconstruction cohérente avec les données. Je n’ai pas développé le logiciel de simulation d’origine de ces échantillons, mais j’ai étudié le code de simulation du calorimètre.

### Préparation et contrôles des distributions
- Présélection pour réduire le bruit de fond, puis utilisation de sWeights issus d’un ajustement pour étudier statistiquement les distributions du signal dans les données mixtes. Ces poids ne donnent pas des étiquettes de signal pur à chaque événement.
- Proposition de variables à partir de la physique, des performances instrumentales et des observables des sous-détecteurs. Comparaison simulation-données à l’aide d’un échantillon de contrôle de topologie proche ; apprentissage d’une repondération par gradient boosting avec hep_ml si nécessaire.
- Vérification des corrélations entre variables et avec l’observable cible ; exclusion des variables fortement corrélées pour limiter le risque de distorsion de la mesure.

### Entraînement et seuil de fonctionnement
- Signal d’entraînement simulé dans la région du signal ; bruit de fond issu des données réelles loin de cette région. Utilisation de cinq plis compte tenu de la statistique limitée.
- Étude de l’importance des variables et des courbes ROC/AUC, retrait des variables peu contributives, puis réglage des hyperparamètres. Comparaison entraînement/test pour diagnostiquer le surapprentissage.
- Balayage d’un critère lié à la précision statistique attendue, tenant compte des efficacités et des effectifs du signal et du fond. Application du seuil retenu aux données réelles.

### Effectifs attendus et rôle des échantillons
À chaque seuil, estimation des effectifs de signal et de fond combinatoire par `S = S0 × effs` et `B = B0 × effb`, avec `S0` et `B0` issus de l’ajustement des données présélectionnées. Ces estimations ont été comparées aux attentes fondées sur la luminosité et les sections efficaces.

La repondération précédait l’entraînement du classifieur. Chaque cycle utilisait cinq plis avec des partitions distinctes pour l’entraînement et le test ; les premiers cycles fixaient les variables, puis les hyperparamètres étaient optimisés. L’échantillon final d’application n’a participé ni à l’entraînement du classifieur ni au réglage des hyperparamètres.

![Performance de sélection](assets/selected-work/work-3/bkg_veto_performance.png "La comparaison Run 1 montre une réduction du fond après sélection BDT, avec maintien du pic de signal. Figure d’étude LHCb unofficial ; aucun gain chiffré n’est déduit de l’image.")
![Validation entraînement/test](assets/selected-work/work-3/train-test.png "Accord global des distributions de réponse entraînement/test pour les deux classes ; diagnostic de surapprentissage, sans garantie d’évaluation indépendante.")
![Importance des variables](assets/selected-work/work-3/feature_importance.png "L’importance et les diagnostics de séparation ont guidé la simplification du modèle.")

### Résultat et transfert
Le point de fonctionnement a été appliqué aux données. La comparaison présentée illustre la réduction du fond et la distribution des scores étaye l’étude de validation. L’apport transférable est une démarche reliant connaissance métier, décalage des échantillons, complexité du modèle et seuil de décision à l’objectif final.

### Rapport associé
Note interne : *Measurement of the branching fraction ratio between B0 → K∗0γ and Bs0 → ϕγ decays using the full LHCb dataset*.
