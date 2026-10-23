---
number: 08
homepage_order: 7
homepage_group: secondary
collapsible: true
title: Portage TensorFlow et vérification numérique
tags: TensorFlow | GPU | Tests numériques
methods: Décomposition sur une base, covariance, pseudo-expériences
impact: Validation de robustesse et préparation de données pour une méthode d’inférence collective.
industry: Problèmes inverses | Analyse de signaux | Développement de méthodes
---
Apprentissage de TensorFlow à partir d’un projet existant, ajout de modèles numériques et vérification face à une implémentation C++ de référence.

### Problème
Une mesure collaborative nécessitait de nouveaux modèles, la prise en compte des effets de mesure et un environnement GPU partagé fonctionnel.

### Ma contribution
- Sans connaissance préalable de TensorFlow, étude du code reçu puis implémentation de modèles d’amplitude et de composantes d’efficacité, de résolution et de biais de mesure.
- Configuration d’une station GPU partagée en une demi-journée ; portage du code jusqu’à une exécution GPU fonctionnelle en une demi-journée supplémentaire. Ces durées concernent uniquement l’installation et le portage.
- Définition des interfaces, revue de merge requests GitLab et adaptation des priorités hebdomadaires. Un collaborateur développait l’outil d’ajustement ; j’ai contribué à ses tests.

### Validation et résultat
Comparaison aux mêmes entrées avec le code C++, identification d’écarts de types numériques et accord à la précision décimale requise. Tests de stabilité sur de grands échantillons simulés et comparaison des distributions observables aux données. Identification, en revue, d’une erreur de signe dans la définition mathématique de l’ajustement, vérifiée et corrigée ensemble.

Le logiciel a servi à une mesure conjointe BESIII–LHCb. Des expériences simulées répétées ont comparé les méthodes sur les mêmes échantillons de taille fixe. Les publications rapportent environ 5 % d’incertitude statistique en moins pour le résultat LHCb : un résultat méthodologique collectif, sans mesure de gain de vitesse du logiciel.

### Illustrations

![Cartes de sensibilité](assets/selected-work/work-8/fourier-weights.png "Pondérations tenant compte de la sensibilité statistique et des effets expérimentaux.")

### Publications

- *Measurement of the CKM angle γ … with a novel approach*, [DOI](https://doi.org/10.48550/arXiv.2604.05701).
- *Precise measurement of the CKM angle γ with a novel approach*, [DOI](https://doi.org/10.48550/arXiv.2604.05712).
