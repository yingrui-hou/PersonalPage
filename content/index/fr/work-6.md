---
number: 06
homepage_order: 3
collapsible: true
title: Diagnostic de performance et correction logicielle
tags: Recherche de causes | Validation de modèles | Revue de code
methods: Canaux de référence, comparaison données-simulation, analyse instrumentale
impact: Transformation d’écarts de validation en actions de calibration et de correction.
industry: Qualité des données | Validation de modèles | Diagnostic
---
Analyse des performances de reconstruction et de reconnaissance d’images, puis livraison d’une correction d’algorithme utilisée dans les analyses suivantes.

### Problème
Des résultats inattendus pouvaient provenir des données, de la calibration, des étiquettes de référence simulées ou du logiciel. Il fallait isoler la cause avant de modifier le modèle.

### Ma contribution
- Évaluation sur données réelles d’un modèle de regroupement par reconnaissance d’images. Mon rôle portait sur sa validation, sans entraîner ce modèle.
- Identification d’associations de référence erronées à l’origine d’une résolution anormale dans des données simulées à forte occupation.
- Modification de l’association pour sélectionner le contributeur individuel d’énergie dominant dans le cluster reconstruit, avec normalisation par l’énergie simulée totale déposée dans ce cluster.
- Amélioration de la sécurité en exécution multithread lors de la revue de code.

### Validation et résultat
Contrôle des identités de référence, des énergies reconstruites et d’événements individuels sur plusieurs processus simulés. La merge request a été intégrée et utilisée pour les analyses LHCb Run 3 et les contrôles de performance. Les diagnostics sur données réelles ont aussi alimenté des corrections de calibration et de logiciel.

### Illustrations

![Validation des données](assets/selected-work/work-6/data_validation.png "Mise en évidence d’un défaut de calibration en énergie et suivi après correction.")

### Publications

*Monitoring reconstruction software in LHCb*, [DOI](https://doi.org/10.1051/epjconf/202125103044).
