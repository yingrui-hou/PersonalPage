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
### Vérification et contribution personnelle
J’ai réalisé le portage des modèles d’amplitude vers TensorFlow, ajouté les modèles d’effets de mesure et effectué les tests associés. Un collaborateur a développé le fitter ; j’ai également participé à ses tests.

- Exécution d’un petit échantillon simulé, puis d’un grand échantillon pour comparer les amplitudes à un code C++ éprouvé aux mêmes points d’échantillonnage.
- Identification de types de variables incohérents à l’origine de faibles écarts. Après harmonisation, accord à la précision décimale requise. Les grands échantillons ont également servi à rechercher des risques de fuite mémoire et d’arrêt du programme.
- Comparaison des distributions d’observables simulées et des signaux de données réelles par tests KS. Les amplitudes des données réelles ne peuvent pas être comparées directement point par point.

### Comparaison contrôlée des méthodes d’inférence
Avant la mesure formelle, génération de pseudo-expériences B → D(→ K⁰KK)h avec la statistique du jeu de données réel. Application des méthodes de Fourier et BPGGSZ par bins aux **mêmes échantillons, sans changer leur taille**. La précision correspond à la largeur de la distribution des valeurs de gamma ajustées sur les expériences répétées. Les faibles biais observés n’étaient pas statistiquement significatifs au niveau de 2 sigma rapporté. Cette étude n’établit pas une tendance avec la taille des échantillons.

### Développement logiciel collaboratif
Définitions des variables et interfaces amplitude/fitter convenues avant le développement. Développement de composants sur GitLab et revues croisées de merge requests, avec points hebdomadaires et échanges rapides face aux problèmes techniques. En revue, détection d’un signe inversé dans le fitter : vérification collective de la dérivation, confirmation et correction de l’erreur, puis réexamen des autres dérivations. Face aux difficultés nouvelles du traitement des données, révision collective des priorités et délais selon leur nécessité et leur impact.

### Résultat collectif
Le logiciel a servi à la mesure conjointe de gamma BESIII–LHCb. Les articles rapportent une réduction d’environ **5 % de l’incertitude statistique LHCb** par rapport à une analyse par bins des mêmes données. Il s’agit d’un résultat collectif de méthode, sans lien établi avec un gain de vitesse TensorFlow ou une attribution individuelle. Le résultat combiné final est gamma = 71,3 ± 5,0 degrés, incertitudes statistiques et systématiques comprises.

### Publications
- *Measurement of the CKM angle γ … with a novel approach*, [DOI](https://doi.org/10.48550/arXiv.2604.05701).
- *Precise measurement of the CKM angle γ with a novel approach*, [DOI](https://doi.org/10.48550/arXiv.2604.05712).
