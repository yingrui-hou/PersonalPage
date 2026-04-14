### Inférence, validation et workflows d'analyse
CNRS / CERN / LHCb Collaboration + GRAiNITA Collaboration
- Développement de workflows réutilisables en C++/Python/ROOT pour l'extraction de signaux faibles, l'inférence dépendante du temps et la validation sur données bruitées sans vérité terrain directe au niveau événement.
- Mise en oeuvre de modèles de vraisemblance et de fits conjoints pour estimer des paramètres latents sous effets de biais, de résolution finie et de désaccord entre échantillons.
- Développement de pipelines CatBoost pour la sélection et la validation, avec diagnostics train/test, études de scan et application reproductible des modèles.
- Alignement simulation-données par repondération et calibration sur échantillons de contrôle avant les décisions d'inférence et de sélection aval.
- Contribution à des composants de fit réutilisables et à des tests de robustesse pour des workflows d'inférence pondérée et non binée.
- Travail dans de grandes collaborations techniques avec bases de code partagées et discipline de revue, avec des résultats de validation réinjectés dans des décisions de calibration et de modélisation.

### Simulation, calibration et interprétation des données d'essai
CNRS / CERN / LHCb Collaboration + GRAiNITA Collaboration
- Développement et adaptation de code Geant4/C++ pour des études de réponse optique et détecteur, incluant géométrie, stepping et sorties d'analyse.
- Combinaison de données de test-beam, de simulation et de cartes de réponse pour modéliser la chaîne de mesure et quantifier l'effet des non-uniformités sur la résolution, avec une contribution au terme constant inférieure à `1%`.
- Développement de workflows d'analyse temporelle du signal permettant de récupérer des fractions de composantes à partir de la scintillation et d'améliorer la résolution en énergie d'environ un facteur `2` dans des études PSD représentatives.
- Développement de workflows ROOT/C++ de calibration et de correction pour réduire les biais structurés et comparer les performances avant/après correction selon les conditions de fonctionnement.
- Mise en place de workflows de monitoring par canaux de référence afin de valider la reconstruction et la calibration, puis de remonter les anomalies à des causes détecteur ou logicielles au lieu de s'arrêter à une analyse descriptive.
- Identification d'anomalies concrètes menant à des actions correctives, dont un problème logiciel d'énergie manquante ensuite corrigé dans la reconstruction.
- Implémentation d'outils de correction événement par événement dans des frameworks de collaboration afin d'améliorer le réalisme de modèles rapides à partir de contraintes mesurées.
