# Topologie hybride et variété d'ombre (Implicate Order)

## L'intuition de départ
Ce projet est né d'une question sur le **champ linguistique** et les systèmes complexes : 
*L'information est-elle stockée de manière locale (mot par mot), ou de manière "holographique", c'est-à-dire distribuée de telle sorte que chaque fragment contient l'empreinte du tout ?*

Pour tester cette hypothèse de manière rigoureuse, nous avons construit un banc d'essai mathématique : un système dynamique hybride continu-discret (modèle **F-I-B**), inspiré des travaux sur l'ordre implié (David Bohm et Basil Hiley).

## Ce que le code démontre
- **Aveuglement euclidien** : La proximité physique sur la grille ne suffit pas à expliquer la dynamique.
- **Déformation de l'espace** : L'analyse du Jacobien prouve que l'espace des phases se déforme et se contracte (squeezing).
- **Signature holographique (Preuve ML)** : Un modèle d'Intelligence Artificielle (SVM) entraîné sur un patch local de 7x7 pixels parvient à prédire l'état topologique global avec **81% de précision**, alors qu'un contrôle "aveugle" (substitut de Fourier) échoue.

## Contenu du dépôt
- `fib_core.py` : Noyau de la dynamique F-I-B.
- `v9_metaplectic_dynamo.py` : Test du transfert d'information spatial (le "dynamo").
- `v11_full_audit.py` : Analyse du Jacobien global et balayage de la diffusion (D_F).
- `v12_convergence_relative.py` : Validation numérique de la convergence du Jacobien.
- `v13_2_holographie_PR.py` : Analyse du Rapport de Participation (PR) des modes propres et contrôles spectraux.
- `redundancy.py` : Le test final : prédiction locale de l'état global via Machine Learning (SVM).

## Statut
Le pipeline d'analyse est complet. Les résultats numériques valident l'hypothèse d'une redondance spatiale forte (holographie). 
La prudence reste de mise : ceci est un modèle mathématique abstrait, pas une preuve directe sur le cerveau humain.
