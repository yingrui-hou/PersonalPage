### Des compétences étayées par les projets
- **Vérifier la fiabilité :** calibration et validation sur données réelles d’un modèle de marquage de saveur par apprentissage profond. Méthodes applicables à l’évaluation des sorties d’un modèle avant leur utilisation dans une nouvelle analyse. [Cas de calibration](index-fr.html#work-9).
- **Diagnostiquer la performance :** évaluation sur données réelles d’un modèle de reconnaissance d’images pour l’ECAL et recherche de causes liées à la calibration, au détecteur ou au logiciel. Méthodes transférables à l’évaluation de modèles et au diagnostic des causes. [Cas de diagnostic](index-fr.html#work-6).
- **Traiter les écarts entre échantillons :** entraînement de classifieurs CatBoost, contrôles entraînement/test et repondération des données de contrôle et cibles. Application possible à l’évaluation de modèles lorsque les distributions diffèrent. [Décalage de distribution](index-fr.html#work-3).
- **Apprendre et appliquer :** sans connaissance préalable de TensorFlow, adaptation d’un code existant avec de nouveaux modèles d’amplitude et d’effets de mesure, puis vérification sur données simulées. Sans expérience GPU ni d’administration multi-utilisateur, configuration d’une station partagée en une demi-journée et migration vers une exécution GPU réussie en une demi-journée supplémentaire. Ces durées concernent la configuration et la migration. [Apprentissage et réalisation](index-fr.html#work-8).
- **Coordonner et communiquer :** organisation de tâches liées de mesure, d’analyse et de validation ; contributions au code partagé et aux revues. Présentations au GDR-InF 2022 et à FCC/DRD France 2025, dont au nom de GRAiNITA.

- **Fiabilité du logiciel scientifique :** comparaison des amplitudes TensorFlow à une référence C++, harmonisation des types et détection d’une erreur de signe du fitter en revue GitLab. Ajustement collectif des priorités lors des points hebdomadaires. [Vérification et collaboration](index-fr.html#work-8).

### Ma démarche face à un nouveau problème métier
Une proposition pour le premier mois, dont le périmètre et le calendrier seraient convenus avec l’équipe après accès aux données et à l’environnement :
- **Comprendre la décision :** identifier les utilisateurs, le processus existant, les critères de réussite et le coût des différentes erreurs.
- **Établir une référence :** examiner la qualité des données et reproduire un résultat existant ou une analyse simple.
- **Étudier une priorité :** analyser un biais d’échantillon, une calibration ou un écart de performance précis, avec des contrôles convenus avec les experts métier.
- **Livrer un résultat vérifiable :** partager une analyse reproductible, ses conclusions, ses limites et une proposition d’actions prioritaires.

- **Automatisation de l’acquisition et de la qualité :** Développement d’une chaîne Shell pour l’acquisition sous faisceau, le stockage, la calibration rapide et les premiers contrôles qualité, reliant lecture du détecteur, tracking et calibration temporelle. Participation au montage et à la prise de données ; appui aux ajustements et corrections des effets de mesure.

- **Du diagnostic à la revue de code:** Diagnostic d’associations erronées des photons ECAL ; modification du matching par énergie déposée dans le cluster, tests sur plusieurs canaux simulés et amélioration de la sûreté multithread après revue. Modification intégrée et utilisée pour les analyses Run 3 et les contrôles de reconstruction.

- **ML relié à l’objectif de mesure:** Sélection de signal rare avec CatBoost : repondération par échantillon de contrôle, corrélations, entraînement/test à cinq plis et réduction des variables ; seuil choisi selon la précision attendue.
