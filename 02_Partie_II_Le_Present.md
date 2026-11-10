# PARTIE I : Le présent comme épaisseur

## Chapitre 1 — Le mythe de l'instant

### 1. De l'instant à la structure
Le présent ne peut pas être pensé comme un point mathématique isolé. Si le présent était un instant sans durée, il serait impossible d'expliquer comment nous pouvons entendre une mélodie, comprendre une phrase ou percevoir un mouvement. Pour qu'une succession soit perçue *comme* une succession, il faut que l'instant présent contienne en lui-même la trace de ce qui vient de s'écouler.

### 2. La dynamique du retour d'information
Le modèle markovien (V77) illustre un présent sans épaisseur : l'information fuit instantanément dans l'environnement. À l'inverse, le modèle non-markovien (V78) montre un *information backflow*. L'environnement retient l'information qui a fui, puis la réinjecte. La pureté chute, puis remonte. Le présent est constitué par la trace structurée de son histoire.

### 3. Holonomie et parcours : une illustration géométrique
Le script `v_berry_monodromy.py` construit une famille de matrices évoluant selon un flot de Toda. Il suit l'espace propre le long d'une boucle fermée. Pour les paramètres étudiés, le contrôle numérique donne un recouvrement final voisin de \(-1\), compatible avec une holonomie réelle non triviale (phase de \(\pi\)). 

Un audit de convergence (de 50 à 200 points, pas de temps de \(10^{-3}\) à \(0.25 \times 10^{-3}\)) a confirmé que la monodromie est stable et l'écart spectral négligeable. Cela montre qu'un retour aux mêmes paramètres n'impose pas la trivialité du parcours. Le temps vécu laisse une signature topologique.

## Chapitre 2 — La rétention : le passé qui ne passe pas

### 1. La rétention selon Husserl
La rétention n'est pas le souvenir (acte volontaire). C'est le maintien du passé immédiat dans le présent vivant. Prenons l'exemple d'une mélodie : le *do* qui vient de résonner n'est plus là physiquement, mais il est retenu dans mon expérience du *ré*. Sans cette rétention, chaque note serait un choc isolé. La rétention est l'invariance structurelle du flux temporel.

### 2. L'impression primordiale et la protention
Husserl décompose le présent en trois moments : l'impression primordiale (le noyau), la rétention (la queue de comète du passé) et la protention (l'anticipation de l'instant suivant). La protention est une attente structurée par le passé.

### 3. De Husserl à Bergson : la durée physique de l'environnement
Le script `v79_bergson_test.py` simule l'évolution d'un système quantique avec un environnement qui garde une mémoire. Deux environnements avec des histoires différentes (chaud/froid) sont comparés. Même si les états présents se ressemblent, leurs trajectoires ont divergé à cause du passé de l'environnement. C'est la traduction physique de la durée bergsonienne : le présent est l'épaississement de tout ce qui l'a précédé.

### 4. Contrôle méthodologique : l'absence de mémoire historique
Le script `v82_test_memoire_historique.py` applique un test de permutation à une série purement markovienne. Le résultat est un négatif propre (p-valeur élevée). Ce test confirme que nos simulations ne produisent pas d'artefacts : la mémoire observée dans V78 et V79 est un phénomène physique réel.

## Chapitre 3 — L'impression primordiale : le présent comme intrication

### 1. Le maintenant n'est pas un point isolé
La physique quantique interdit de penser le "maintenant" comme une entité isolée. Un système local ne possède pas d'état défini indépendamment de son environnement. 

### 2. La dissolution du soi dans le fond onirique
Le script `v90_dissolution_soi.py` simule un système "Soi" (S) intriqué avec un environnement "Fond onirique" (E). À intrication maximale (\(\theta = \pi/4\)), la pureté locale du Soi chute à 0.5 (mélange maximal), tandis que la pureté globale (S+E) reste à 1.0. L'information n'est pas détruite, elle est délocalisée dans la relation. 

Le "je" du présent n'est jamais une substance pure. Il est toujours dissous dans un champ plus vaste. L'impression primordiale est l'expérience d'un nœud de relations, pas d'un sujet clos.
