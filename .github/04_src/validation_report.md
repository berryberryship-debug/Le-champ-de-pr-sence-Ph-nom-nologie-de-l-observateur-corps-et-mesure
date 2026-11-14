# Rapport de validation algorithmique (V8)

## 1. Objet et méthode
Ce rapport atteste de la validité du module `topology/` utilisé pour mesurer le rang d'enroulement (winding) topologique des champs binaires générés par la dynamique F-I-B.

Deux implémentations indépendantes ont été développées :
- **Implémentation A** (`src/topology/winding.py`) : Parcours en largeur (BFS) avec suivi des coordonnées dans le revêtement universel du tore.
- **Implémentation B** (`src/topology/bcs_independent.py`) : Théorie des graphes via la bibliothèque `networkx`, utilisant `cycle_basis` et le calcul d'images minimales.

La convention d'analyse est mixte : état majoritaire en 4-connexité, état minoritaire en 8-connexité.

## 2. Résultats sur les données réelles (179 graines de V7.19)
- **Divergences A vs B** : 0 (sur 179 graines).
- **Incohérences avec l'archive V7.19** : 0.
- **Distribution des classes** : 130 graines en (2,0) et 49 graines en (1,1).

Le recalcul exact des 179 graines valides démontre une reproductibilité parfaite du protocole V7.

## 3. Résultats sur les contrôles négatifs (Champs de Bernoulli)
Les champs aléatoires ont été testés sur les tailles `L=41` et `L=61`.
- **Divergences A vs B** : 0 sur 1400 comparaisons.
- **Cas (1,4)** : 0 percolation en dessous de p=0.55, transition autour de p=0.58-0.59, 100% de percolation à p=0.7.
- **Effet de taille finie** : la proportion de champs percolants sous le seuil (p=0.58) baisse de 50% (L=41) à 32% (L=61), confirmant le resserrement de la transition autour du seuil théorique p_c ≈ 0.593.

## 4. Limites
- Les deux implémentations partagent la même définition du rang, validant l'implémentation mais pas la définition elle-même.
- L'analyse de taille finie reste qualitative (50 champs par point). Une mesure précise de l'exposant critique nécessiterait 300 à 500 champs par point et une taille L=81.
- Les 21 graines dégénérées (champs quasi uniformes) ont été exclues de l'analyse par convention.

## 5. Conclusion
Le module topologique est **validé**. Les deux algorithmes concordent parfaitement sur les données réelles et sur les contrôles négatifs. La transition topologique observée dans les simulations F-I-B est une propriété intrinsèque des champs, et non un artefact algorithmique.
