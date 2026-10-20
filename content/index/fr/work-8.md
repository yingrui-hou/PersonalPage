---
number: 08
homepage_order: 7
homepage_group: secondary
collapsible: true
title: Adaptation TensorFlow/GPU et validation d’inférence
tags: TensorFlow | Calcul GPU | Modélisation statistique | R&D collaborative
methods: Décomposition sur une base, covariance, pseudo-expériences
impact: Validation de robustesse et préparation de données pour une méthode d’inférence collective.
industry: Problèmes inverses | Analyse de signaux | Développement de méthodes
---
**Partant de zéro sur TensorFlow, adaptation d’un code de recherche avec de nouveaux modèles, vérification sur simulations et transfert du calcul vers une station GPU partagée. Le travail sur la mesure conjointe de gamma comprend aussi la validation de la méthode d’inférence en conditions réalistes.**

![Cartes de sensibilité](assets/selected-work/work-8/fourier-weights.png "Pondérations tenant compte de la sensibilité statistique et des effets expérimentaux.")

### Réalisation personnelle
- Évaluation des effets du bruit de fond, de l’efficacité et de la résolution sur l’inférence non binée.
- Préparation d’un échantillon de données : reconstruction, sélection et soustraction statistique du bruit de fond.
- Contribution aux entrées d’ajustement, à la validation tenant compte des covariances et aux pseudo-expériences dans un effort méthodologique collectif.
### Apprendre TensorFlow en adaptant un code existant
- Sans connaissance préalable de TensorFlow, étude du code fourni par un projet connexe pour le comprendre et l’adapter à la mesure conjointe de gamma.
- Ajout de nouveaux modèles d’amplitude physique et de composantes numériques d’efficacité, de résolution et de biais de mesure pour décrire les effets de mesure sur les données réelles.
- Génération de données simulées avec le nouveau modèle et utilisation de ces données pour vérifier le code adapté.

### Prise en charge d’une station GPU partagée
- Mon expérience antérieure de Linux était celle d’une utilisatrice individuelle ; le calcul GPU et l’administration multi-utilisateur étaient nouveaux pour moi.
- L’équipe m’a confié l’utilisation et la gestion d’une station GPU partagée. Sa configuration a pris **une demi-journée**.
- La migration du code TensorFlow et sa première exécution réussie sur GPU ont pris **une demi-journée supplémentaire**.
- Ces deux durées concernent la configuration et la migration. L’apprentissage de TensorFlow, le développement des modèles et la vérification du code constituent une autre partie du projet.

### Compétences transférables
Comprendre un logiciel inconnu, l’étendre avec des modèles métier, vérifier les modifications sur des données simulées et prendre en charge un environnement de calcul partagé utilisable.

### Résultat
Une proposition théorique confrontée à des variations expérimentales et de modélisation, avec attribution de la contribution à la validation et à la préparation des données.
### Publications
- *Measurement of the CKM angle γ … with a novel approach*, [DOI](https://doi.org/10.48550/arXiv.2604.05701).
- *Precise measurement of the CKM angle γ with a novel approach*, [DOI](https://doi.org/10.48550/arXiv.2604.05712).
