# PARTIE I : Le présent comme épaisseur

Rétention husserlienne et héritage relationnel whiteheadien
Préhension et constitution relationnelle de l'actualité Relier impression et processus
Temporalité vécue, durée et horizon des possibles Distinguer temps de l'expérience et temps de son contenu
Rétention, protention et concrescence Comparer les structures sans les confondre
Géométrisation de la mémoire et statut des hypothèses Délimiter le formalisme
Husserl, Bergson et Whitehead Établir le dialogue philosophique
Analyse physique de V78 et contrôles méthodologiques Séparer résultats numériques et interprétation philosophique

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

## Chapitre 4 — Le temps de l'esprit et l'articulation du présent

Cette analyse redéfinit notre rapport au temps en distinguant **le moment où nous vivons** de **l'horizon dans lequel nous vivons**. Nous sommes toujours engagés dans une situation présente, mais ce qui nous occupe peut provenir de loin, viser demain ou explorer une possibilité qui ne se réalisera jamais. L'esprit ne sort donc pas du temps : il n'est simplement pas enfermé dans le contenu de l'instant.

### 1. Le présent comme articulation, et non comme simple captation
La perception de ce qui est immédiatement là suppose déjà une relation temporelle. Lorsque nous écoutons une phrase, nous ne recevons pas seulement le mot actuel. Les mots précédents demeurent accessibles comme venant de passer, et la phrase ouvre une attente de continuation. C'est la structure que Husserl distingue par la rétention, l'impression présente et la protention. Sans cette articulation, une phrase ou une mélodie ne pourraient être perçues comme des ensembles en train de se dérouler.

Le présent n'est donc pas un point nu auquel l'esprit ajouterait ensuite du passé et de l'avenir. Dans cette description phénoménologique, il est déjà structuré par eux, sans que le passé soit confondu avec l'actuel ni l'avenir avec l'accompli.

### 2. Le temps de l'exploration et le temps de ce qui est exploré
L'activité de l'esprit se déroule maintenant, pendant une durée réelle. Cependant, son contenu peut viser une conversation ancienne, un projet pour les prochaines années, une possibilité écartée ou une scène imaginaire sans date déterminée.

Il faut donc rigoureusement distinguer le déroulement de l'expérience et les temporalités qu'elle vise. Les propriétés temporelles d'un contenu ne sont pas nécessairement celles de l'expérience qui le présente.

L'esprit est temporel dans son activité, mais il peut viser autre chose que le moment dans lequel cette activité se déroule. Il ne s'agit pas d'une indépendance à l'égard du corps ou du temps physique, mais d'une liberté relative quant à ce qui peut devenir l'objet de l'attention.

### 3. Provenance, horizon et ancrage
Cette structure permet de distinguer trois dimensions fondamentales de l'expérience temporelle :

| Dimension | Question |
|---|---|
| Provenance | D'où vient cette préoccupation, ce souvenir ou cette possibilité ? |
| Horizon | Vers quoi m'oriente-t-elle ? |
| Ancrage | Pourquoi prend-elle de l'importance maintenant ? |

Une question ancienne peut ainsi devenir actuelle sans que son événement d'origine se reproduise. Ce qui change, c'est sa place dans la situation présente : elle devient pertinente, intelligible ou susceptible d'orienter une action.

Il convient de maintenir une distinction stricte : le retour d'une préoccupation vieille de plusieurs années relève du souvenir et de la reprise de sens, et non de la rétention immédiate au sens husserlien. La rétention concerne le tout-juste-passé et se distingue du souvenir ordinaire.

### 4. L'ouverture des possibles
La structure des possibilités devient alors une manière de penser l'ouverture du vécu : le présent ne contient pas seulement ce qui se manifeste, il comporte aussi une orientation vers ce qui pourrait venir. Cette ouverture n'exige pas que l'avenir existe déjà comme un ensemble d'événements accomplis. Chez Husserl, la protention peut être une attente précise, mais aussi simplement l'ouverture à une suite encore indéterminée.

Notre rapport au temps ne consiste donc pas seulement à subir une succession. Il consiste à reprendre ce qui a été, à rencontrer ce qui arrive et à ouvrir ce qui pourrait être, depuis une situation corporelle que nous ne quittons jamais.

Il s'agit d'une redéfinition de notre manière d'habiter le temps, et non d'une nouvelle théorie physique du temps : nous ne choisissons pas librement le moment où nous sommes, mais ce moment n'épuise pas ce à quoi nous pouvons être présents.

## Chapitre 5 — Rétention et Protention : la validation numérique du présent vivant

L'analyse de la conscience intime du temps chez Husserl décompose le présent vivant (*lebendige Gegenwart*) en trois moments indissociables : l'impression originaire, la rétention et la protention.

### 1. La rétention : la queue de comète
La rétention n'est pas un souvenir actif ; c'est une intentionnalité primaire qui retient le juste-passé dans le présent. Elle forme un continuum où chaque nouvelle impression repousse la précédente. L'expérience du SHC (Synthétiseur Holistique de Cohérence) fournit une traduction numérique de cette structure.

Lorsque le flux est statique (aucune modification du fichier), la variance temporelle est nulle (\(Var_{Tps} = 0.0000\)). Le système est dans un présent ponctuel sans mémoire. Lorsque le flux est actif, le SHC utilise une mémoire glissante (un historique de 64 états) pour calculer la variance temporelle. La chute de l'indice de cohérence (de \(1.0000\) à \(0.9970\)) mesure l'épaisseur que la rétention introduit. L'instrument ne capte pas seulement l'instant \(t\), il retient la traîne de son propre écoulement.

### 2. La protention : l'ouverture vers l'à-venir
La protention est le versant futur de cette épaisseur. Elle est une intention vide, une anticipation passive de l'immédiatement à venir, qui peut être remplie ou déçue. Alors que la rétention a un contenu déjà formé (le passé est arrivé), la protention est ouverte et indéterminée.

Si le SHC mesure la rétention par la variance temporelle du passé, il peut également mesurer la protention en calculant une **extrapolation** de la moyenne du champ. Cette anticipation sera confrontée à l'état suivant : si l'état réel correspond à la prédiction, la protention est remplie ; s'il diverge, la protention est déçue (c'est la surprise).

Ainsi, le présent n'est pas une ligne de points, il est un champ de présence où la trace du passé (rétention) et la tension vers le futur (protention) se co-constituent. L'instrument SHC, en mesurant ces deux dimensions, devient une véritable prothèse phénoménologique.

## Chapitre 6 — La métrique de la rétention et la compression holographique

Pour formaliser l'épaisseur du présent et l'enfoncement du passé dans la mémoire, nous proposons de mobiliser une géométrie inspirée de la métrique de Randall-Sundrum (AdS\(_5\)). Soit \(\mathcal{M}_4\) l'espace-temps perçu (l'ordre explicite) et \(\mathcal{B}_5\) l'hyper-espace de l'ordre implicite défini par une coordonnée de profondeur topologique \(z\).

### 1. La métrique de l'environnement (La résistance de la matrice)
L'espace obéit à une géométrie avec un facteur de déformation (*Warp factor*) :
\[
 ds^2 = e^{-2k|z|} \eta_{\mu\nu} dx^\mu dx^\nu + dz^2
\]
où \(k\) est la tension du gradient de l'univers. Plus l'événement (le circonstanciel) s'enfonce dans la mémoire (\(z\) augmente), plus l'intervalle d'espace-temps \(ds^2\) se contracte de manière exponentielle. L'enjambée du géant est géométriquement réduite.

### 2. L'équation cinématique de Zénon (Le ralentissement asymptotique)
La vélocité de l'information s'enfonçant dans la matrice est \(v = \frac{dz}{d\tau}\). Face à la densité du champ, elle subit une friction de phase quantique \(\gamma\). L'équation différentielle de son mouvement est :
\[
 \frac{dv}{d\tau} + \gamma v = 0
\]
La solution donne une décroissance exponentielle : \(v(\tau) \propto v_0 e^{-\gamma \tau}\). La vélocité s'effondre en divisant sa course sans fin vers une limite qu'elle ne touche jamais (c'est la limite lilliputienne de Zénon).

### 3. La compression holographique (Le micro-hologramme stationnaire)
Le souvenir n'est pas détruit par ce freinage, il est modélisé comme un paquet d'ondes \(\Psi(x, z)\). Sous l'écrasement de la métrique \(e^{-2k|z|}\), sa longueur d'onde causale \(\lambda\) se compresse :
\[
 \lambda(z) = \lambda_0 e^{-k|z|}
\]
Par conservation de l'information (transformée de Fourier), si l'espace occupé diminue, la fréquence vibratoire \(f\) s'amplifie :
\[
 f(z) = f_0 e^{k|z|}
\]
L'événement quitte la ligne de cause à effet. Sa dimension spatiale est asymptotiquement nulle, mais sa tension vibratoire est maximale. Il devient un état propre stationnaire \(|\psi\rangle\), une singularité autopoïétique.

C'est la traduction mathématique de la rétention husserlienne : le passé ne cesse pas d'exister (conservation de l'information), il cesse simplement d'agir (vélocité nulle), pour devenir une fréquence pure dans l'épaisseur du présent.

*Statut : hypothèse spéculative, non une description physique établie.*

## Chapitre 7 — L'exégèse de la rétention : Husserl et le paradoxe du temps

### 1. La critique de la conception ponctuelle du temps
Pour comprendre l'apport de Husserl, il faut d'abord mesurer l'ampleur de la rupture qu'il opère avec la tradition. Aristote, dans sa *Physique*, définissait le temps comme le nombre du mouvement selon l'avant et l'après. Cette conception, reprise et mathématisée par Newton, fait du temps une ligne composée d'instants ponctuels. Dans cette vision, le passé n'est plus, le futur n'est pas encore, et seul le présent est. Mais si le présent est un point sans épaisseur, comment expliquer que nous percevions une mélodie ?

Husserl, dans ses *Leçons pour une phénoménologie de la conscience intime du temps* (1905), pose le problème avec une acuité radicale : si la conscience ne saisissait que l'instant présent, elle serait incapable de percevoir un objet temporel (une mélodie, une phrase, un mouvement). Elle n'entendrait que des notes isolées, sans lien. Or, l'expérience nous montre le contraire. Nous entendons la mélodie comme une totalité. Il faut donc que le présent ait une structure interne qui retient ce qui vient de passer et anticipe ce qui vient.

### 2. La structure triadique de la conscience du temps
Husserl décompose le présent vivant (*lebendige Gegenwart*) en trois moments indissociables :
1.  **L'impression originaire (*Urimpression*)** : c'est le noyau de l'expérience actuelle, le "maintenant" strict, le point de source.
2.  **La rétention** : ce n'est pas un souvenir (qui est un acte volontaire de rappel). C'est le maintien du juste-passé dans le présent. La rétention est une intentionnalité primaire. Elle forme une "queue de comète" qui s'étire derrière l'impression originaire.
3.  **La protention** : c'est l'anticipation ouverte du juste-à-venir. Elle est une intention vide qui tend vers le futur immédiat.

Ce qui est crucial ici, c'est que ces trois moments ne sont pas des actes séparés. Ils sont les dimensions d'un seul et même flux. Comme le dit Husserl, chaque phase de la conscience est déjà chargée de rétentions et de protentions. Le présent n'est pas un point, c'est une **épaisseur**.

### 3. La distinction entre rétention et ressouvenance
Husserl insiste sur une distinction fondamentale. La rétention n'est pas la ressouvenance (*Wiedererinnerung*).
La rétention concerne le tout-juste-passé : la note qui vient de sonner. Elle n'est pas encore un objet, elle est encore vécue dans le présent.
La ressouvenance, elle, est un acte actif : je me souviens d'une mélodie entendue hier. Je la re-présente, je la pose comme un objet devant moi.
Cette distinction est vitale pour notre thèse : elle montre que le passé n'est jamais "perdu" de manière absolue. Il y a une continuité rétentionnelle qui rend possible le souvenir. Sans ce flux rétentionnel, aucune mémoire ne pourrait se constituer.

### 4. La solution du paradoxe de Zénon
Cette structure permet de résoudre le paradoxe de Zénon. Pour qu'une flèche se déplace, Zénon soutenait qu'elle devait occuper une position définie à chaque instant. Mais si le temps est fait de points, le mouvement est impossible. Husserl répond que le mouvement n'est pas perçu par une série de positions ponctuelles, mais par la continuité du flux rétentionnel. La flèche n'est pas à un point \(x\) à l'instant \(t\) ; elle est perçue comme ayant parcouru un trajet, parce que sa position passée est retenue dans l'instant présent.

## Chapitre 8 — La physique du présent : analyse du script V78

### 1. Le problème de la décohérence
Pour illustrer cette épaisseur du présent, nous avons eu recours à une simulation quantique : le script `v78_nonmarkov_physical.py`. Ce script ne prétend pas modéliser la conscience. Il modélise un système ouvert, soumis à une interaction avec un environnement.
Le point de départ est l'équation de Lindblad :
\[
 \frac{d\rho}{dt} = \gamma \left( \sigma_z \rho \sigma_z - \rho \right)
\]
Cette équation décrit le déphasage pur d'un qubit. Si le taux \(\gamma\) est constant et positif, l'information fuit vers l'environnement. La pureté chute de manière monotone.

### 2. Le retour d'information (information backflow)
Cependant, si le taux \(\gamma\) oscille dans le temps (ce qui est le cas dans un environnement structuré dit "non-markovien"), il peut devenir négatif.
Le script implémente une modulation sinusoïdale : \(\gamma(t) = a \omega \sin(\omega t)\).
La solution analytique de la cohérence (élément hors-diagonale de la matrice densité) est :
\[
 \rho_{01}(t) = \rho_{01}(0) e^{-\Gamma(t)}
\]
avec \(\Gamma(t) = \int_0^t \gamma(\tau) d\tau = a(1 - \cos(\omega t))\).

> **[Correction — voir Annexe, entrée 2]** Le texte d'origine affirmait ici : « Puisque \(\Gamma(t)\) ne décroît jamais, la cohérence ne remonte pas. » C'est inexact : \(\Gamma(t) = a(1-\cos\omega t)\) oscille entre 0 et \(2a\) et décroît lorsque \(\gamma<0\). C'est précisément cette décroissance de \(\Gamma\) qui fait remonter la cohérence.

Le script calcule la pureté :
\[
 P(t) = \frac{1}{2} \left( 1 + e^{-2\Gamma(t)} \right)
\]
On observe que la pureté chute, puis remonte, quand \(\gamma\) change de signe. L'information revient. C'est la signature mathématique de la non-markovianité.

### 3. Analyse ligne par ligne du code
Voici les éléments clés du script `v78_nonmarkov_physical.py` :
```python
def run_v78_nonmarkov_physical():
    T = 20.0
    N = 1000
    time = np.linspace(0.0, T, N + 1)
    # ... définition de a et omega ...
    gamma = a * omega * np.sin(omega * time)
    Gamma = a * (1.0 - np.cos(omega * time))
    coherence = 0.5 * np.exp(-Gamma)
    # ... construction de rho ...
    purities = np.real(np.einsum("tij,tji->t", rho, rho))
    # ... assertions ...
```

### 4. Contrôle méthodologique : l'absence de mémoire dans un système markovien
Pour valider la robustesse de nos outils de détection, nous avons implémenté un **contrôle négatif** : le script `v82_test_memoire_historique.py`. Ce script génère une série temporelle issue d'une dynamique purement markovienne (un processus autorégressif d'ordre 1, AR(1)) et lui applique un test de permutation.

L'algorithme du test de permutation est le suivant :

```python
def test_permutation_memoire(x, n_permutations=1000):
    lag = 5
    # Statistique observée (autocorrélation)
    obs_stat = np.corrcoef(x[:-lag], x[lag:])[0, 1]

    # Statistiques sous permutations (mélange de l'ordre temporel)
    perm_stats = []
    for _ in range(n_permutations):
        x_perm = np.random.permutation(x)
        perm_stat = np.corrcoef(x_perm[:-lag], x_perm[lag:])[0, 1]
        perm_stats.append(perm_stat)

    perm_stats = np.array(perm_stats)

    # Calcul de la p-valeur (test bilatéral)
    p_value = np.mean(np.abs(perm_stats) >= np.abs(obs_stat))
    return obs_stat, p_value
```

# Approfondissement de la conclusion — Le présent comme épaisseur et l'ouverture philosophique

## I. Le présent n'est pas un instant

La conclusion doit maintenant assumer pleinement le déplacement opéré par la première partie.

Nous ne pouvons plus penser le présent comme un point mathématique isolé.

Si le présent était un instant sans durée, il serait impossible d'expliquer comment nous entendons une mélodie, comprenons une phrase ou percevons un mouvement.

Pour qu'une succession soit perçue *comme* une succession, il faut que l'instant présent contienne en lui-même la trace de ce qui vient de s'écouler.

Le présent n'est donc pas une frontière entre un passé disparu et un futur inexistant.

Il est une épaisseur.

Il est une structure.

Il est un nœud de relations.

$$
\boxed{
\text{Présent}
\neq
\text{Instant ponctuel}.
}
$$

$$
\boxed{
\text{Présent}
=
\text{Épaisseur temporelle}.
}
$$

Cette idée n'est pas une simple métaphore.

Elle est le point de départ d'une ontologie du temps vécu.

***

## II. La rétention : le passé qui ne passe pas

### A. La rétention selon Husserl

La rétention n'est pas le souvenir.

Elle n'est pas un acte volontaire de rappel.

Elle est le maintien du passé immédiat dans le présent vivant.

Prenons l'exemple d'une mélodie.

Le *do* qui vient de résonner n'est plus là physiquement.

Mais il est retenu dans mon expérience du *ré*.

Sans cette rétention, chaque note serait un choc isolé.

La mélodie ne pourrait pas être entendue comme une mélodie.

Elle serait une suite de sons discontinus.

La rétention est donc l'invariance structurelle du flux temporel.

$$
\boxed{
\text{Rétention}
=
\text{Maintien du juste-passé dans le présent}.
}
$$

Chez Husserl, la rétention possède une double intentionnalité : elle vise à la fois l'objet temporel qui se constitue et les phases passées du flux de conscience lui-même.[1]

Elle n'est pas un souvenir.

Elle est une modalité primaire du présent.

### B. La distinction entre rétention et ressouvenance

Il est essentiel de distinguer la rétention de la ressouvenance.

La rétention concerne le tout-juste-passé.

La ressouvenance concerne un passé plus lointain, qui doit être rappelé, re-présenté, reconstruit.

La rétention est passive.

La ressouvenance est active.

La rétention est immédiate.

La ressouvenance est médiatisée.

$$
\boxed{
\text{Rétention}
\neq
\text{Ressouvenance}.
}
$$

Cette distinction est vitale pour notre thèse.

Elle montre que le passé n'est jamais perdu de manière absolue.

Il y a une continuité rétentionnelle qui rend possible le souvenir.

Sans ce flux rétentionnel, aucune mémoire ne pourrait se constituer.

***

## III. La protention : l'ouverture vers l'à-venir

### A. La protention comme anticipation

La protention est le versant futur de l'épaisseur du présent.

Elle est une anticipation passive de l'immédiatement à venir.

Elle est une intention vide, qui peut être remplie ou déçue.

Alors que la rétention a un contenu déjà formé, la protention est ouverte et indéterminée.

$$
\boxed{
\text{Protention}
=
\text{Ouverture vers le juste-à-venir}.
}
$$

Chez Husserl, la structure du présent vivant comprend trois moments inséparables : l'impression originaire, la rétention et la protention.[2][3][4]

Ces trois moments ne sont pas des actes séparés.

Ils sont les dimensions d'un seul et même flux.

### B. La protention comme direction locale

Dans notre modèle, la protention peut être modélisée comme une direction locale de la trajectoire.

Si $$\gamma(t)$$ représente la trajectoire du système, alors sa direction locale peut être représentée par :

$$
\dot{\gamma}(t).
$$

La protention peut être rapprochée de cette direction locale anticipée.

Mais nous devons être prudents.

Il ne faut pas écrire :

$$
\text{Protention} = \text{Tangente}.
$$

Il faut écrire :

$$
\boxed{
\text{Protention phénoménologique}
\widehat{\longrightarrow}
\text{Direction locale anticipée de la trajectoire}.
}
$$

La flèche large indique une correspondance, non une identité.

### C. La déception protentionnelle

La déception protentionnelle peut être rapprochée d'un écart entre la trajectoire attendue et la trajectoire effective :

$$
\varepsilon(t)
=
\dot{\gamma}_{\text{attendue}}(t)
-
\dot{\gamma}_{\text{effective}}(t).
$$

Cette formulation ouvre un pont avec les modèles prédictifs.

Mais elle ne réduit pas la protention phénoménologique à une simple erreur de prédiction.

La protention n'est pas seulement un calcul.

Elle est une structure vécue du temps.

***

## IV. La physique du présent : mémoire et retour d'information

### A. Le modèle markovien et le modèle non-markovien

Le modèle markovien illustre un présent sans épaisseur.

L'information fuit instantanément dans l'environnement.

À l'inverse, le modèle non-markovien montre un *information backflow*.

L'environnement retient l'information qui a fui, puis la réinjecte.

La pureté chute, puis remonte.

Le présent est constitué par la trace structurée de son histoire.

$$
\boxed{
\text{Présent}
=
\text{Trace structurée de l'histoire}.
}
$$

Dans les dynamiques quantiques ouvertes, la non-markovianité se manifeste par des effets de mémoire, où l'information quitte temporairement le système pour revenir ensuite depuis l'environnement.[5][6]

Ce retour d'information constitue une signature opérationnelle de la non-markovianité.[5][6]

### B. La limite de l'analogie

Il faut cependant être prudent.

La non-markovianité quantique ne modélise pas la conscience.

Elle modélise un système ouvert soumis à une interaction avec un environnement.

Elle ne prétend pas expliquer la rétention phénoménologique.

Elle propose une analogie structurelle.

$$
\boxed{
\text{Rétention phénoménologique}
\widehat{\longrightarrow}
\text{Mémoire dynamique d'un système ouvert}.
}
$$

Cette analogie ne doit pas être confondue avec une identification.

Elle doit être comprise comme une hypothèse de modélisation.

### C. La durée bergsonienne

La durée bergsonienne peut être rapprochée de cette structure.

Le présent n'est pas un instant ponctuel.

Il est l'épaississement de tout ce qui l'a précédé.

Deux environnements avec des histoires différentes peuvent présenter des états présents similaires, tout en ayant des trajectoires divergentes.

La différence ne réside pas dans l'état présent.

Elle réside dans la trajectoire.

$$
\boxed{
\text{Durée}
=
\text{Épaisseur de l'histoire dans le présent}.
}
$$

***

## V. L'holonomie : la signature topologique du temps vécu

### A. Le retour n'est jamais identique

Le script `v_berry_monodromy.py` construit une famille de matrices évoluant selon un flot de Toda.

Il suit l'espace propre le long d'une boucle fermée.

Pour les paramètres étudiés, le contrôle numérique donne un recouvrement final voisin de $$-1$$, compatible avec une holonomie réelle non triviale, c'est-à-dire une phase de $$\pi$$.

Un audit de convergence a confirmé que la monodromie est stable et l'écart spectral négligeable.

Cela montre qu'un retour aux mêmes paramètres n'impose pas la trivialité du parcours.

Le temps vécu laisse une signature topologique.

$$
\boxed{
\text{Retour}
\neq
\text{Identité}.
}
$$

### B. L'holonomie comme mémoire géométrique

L'holonomie mesure ce qui a changé après un retour apparent au point de départ.

Elle ne mesure pas seulement où le système est.

Elle mesure comment il y est arrivé.

$$
\boxed{
\text{Holonomie}
\equiv
\text{Trace géométrique d'un cycle de régulation}.
}
$$

Cette idée rejoint directement notre modèle de la mémoire.

La mémoire n'est pas un simple stockage.

Elle est une modification durable de l'espace des trajectoires accessibles.

### C. La limite de l'analogie

Il faut cependant être prudent.

L'holonomie ne doit pas être interprétée comme une observable biologique directement mesurée.

Elle constitue une structure mathématique candidate.

Elle représente la mémoire géométrique d'un cycle de régulation.

Elle ne prétend pas expliquer la rétention phénoménologique.

Elle propose une analogie structurelle.

$$
\boxed{
\text{Rétention phénoménologique}
\widehat{\longrightarrow}
\text{Holonomie géométrique}.
}
$$

***

## VI. L'impression primordiale : le présent comme intrication

### A. Le maintenant n'est pas isolé

La physique quantique interdit de penser le « maintenant » comme une entité isolée.

Un système local ne possède pas d'état défini indépendamment de son environnement.

Le présent n'est pas un point isolé.

Il est un nœud de relations.

$$
\boxed{
\text{Présent}
=
\text{Nœud de relations}.
}
$$

### B. La dissolution du soi

Le script `v90_dissolution_soi.py` simule un système « Soi » intriqué avec un environnement « Fond onirique ».

À intrication maximale, la pureté locale du Soi chute, tandis que la pureté globale reste constante.

L'information n'est pas détruite.

Elle est délocalisée dans la relation.

Le « je » du présent n'est jamais une substance pure.

Il est toujours dissous dans un champ plus vaste.

$$
\boxed{
\text{Soi}
\neq
\text{Substance isolée}.
}
$$

$$
\boxed{
\text{Soi}
=
\text{Nœud de relations}.
}
$$

### C. La limite de l'analogie

Il faut cependant être prudent.

L'intrication quantique ne modélise pas la conscience.

Elle modélise une corrélation entre systèmes.

Elle ne prétend pas expliquer le sentiment de soi.

Elle propose une analogie structurelle.

$$
\boxed{
\text{Soi phénoménologique}
\widehat{\longrightarrow}
\text{Système ouvert intriqué}.
}
$$

Cette analogie ne doit pas être confondue avec une identification.

Elle doit être comprise comme une hypothèse de modélisation.

***

## VII. Le temps de l'esprit et l'articulation du présent

### A. Le moment et l'horizon

Cette analyse redéfinit notre rapport au temps en distinguant le moment où nous vivons de l'horizon dans lequel nous vivons.

Nous sommes toujours engagés dans une situation présente.

Mais ce qui nous occupe peut provenir de loin, viser demain ou explorer une possibilité qui ne se réalisera jamais.

L'esprit ne sort donc pas du temps.

Il n'est simplement pas enfermé dans le contenu de l'instant.

$$
\boxed{
\text{Présent}
\neq
\text{Contenu de l'instant}.
}
$$

$$
\boxed{
\text{Présent}
=
\text{Horizon d'ouverture}.
}
$$

### B. Le présent comme articulation

La perception de ce qui est immédiatement là suppose déjà une relation temporelle.

Lorsque nous écoutons une phrase, nous ne recevons pas seulement le mot actuel.

Les mots précédents demeurent accessibles comme venant de passer.

La phrase ouvre une attente de continuation.

C'est la structure que Husserl distingue par la rétention, l'impression présente et la protention.[2][3][4]

Sans cette articulation, une phrase ou une mélodie ne pourraient être perçues comme des ensembles en train de se dérouler.

$$
\boxed{
\text{Présent}
=
\text{Articulation}.
}
$$

### C. Le temps de l'exploration et le temps de ce qui est exploré

L'activité de l'esprit se déroule maintenant, pendant une durée réelle.

Cependant, son contenu peut viser une conversation ancienne, un projet pour les prochaines années, une possibilité écartée ou une scène imaginaire sans date déterminée.

Il faut donc rigoureusement distinguer le déroulement de l'expérience et les temporalités qu'elle vise.

Les propriétés temporelles d'un contenu ne sont pas nécessairement celles de l'expérience qui le présente.

$$
\boxed{
\text{Temps de l'expérience}
\neq
\text{Temps du contenu}.
}
$$

L'esprit est temporel dans son activité.

Mais il peut viser autre chose que le moment dans lequel cette activité se déroule.

Il ne s'agit pas d'une indépendance à l'égard du corps ou du temps physique.

Il s'agit d'une liberté relative quant à ce qui peut devenir l'objet de l'attention.

***

## VIII. Provenance, horizon et ancrage

### A. Les trois dimensions

Cette structure permet de distinguer trois dimensions fondamentales de l'expérience temporelle.

| Dimension | Question |
|---|---|
| Provenance | D'où vient cette préoccupation, ce souvenir ou cette possibilité ? |
| Horizon | Vers quoi m'oriente-t-elle ? |
| Ancrage | Pourquoi prend-elle de l'importance maintenant ? |

Une question ancienne peut devenir actuelle sans que son événement d'origine se reproduise.

Ce qui change, c'est sa place dans la situation présente.

Elle devient pertinente, intelligible ou susceptible d'orienter une action.

$$
\boxed{
\text{Présent}
=
\text{Provenance}
+
\text{Horizon}
+
\text{Ancrage}.
}
$$

### B. La distinction entre souvenir et rétention

Il convient de maintenir une distinction stricte.

Le retour d'une préoccupation vieille de plusieurs années relève du souvenir et de la reprise de sens.

Il ne relève pas de la rétention immédiate au sens husserlien.

La rétention concerne le tout-juste-passé.

Elle se distingue du souvenir ordinaire.

$$
\boxed{
\text{Rétention}
\neq
\text{Souvenir}.
}
$$

### C. L'ouverture des possibles

La structure des possibilités devient alors une manière de penser l'ouverture du vécu.

Le présent ne contient pas seulement ce qui se manifeste.

Il comporte aussi une orientation vers ce qui pourrait venir.

Cette ouverture n'exige pas que l'avenir existe déjà comme un ensemble d'événements accomplis.

Chez Husserl, la protention peut être une attente précise, mais aussi simplement l'ouverture à une suite encore indéterminée.[2][3][4]

Notre rapport au temps ne consiste donc pas seulement à subir une succession.

Il consiste à reprendre ce qui a été, à rencontrer ce qui arrive et à ouvrir ce qui pourrait être, depuis une situation corporelle que nous ne quittons jamais.

$$
\boxed{
\text{Présent}
=
\text{Ouverture des possibles}.
}
$$

***

## IX. La métrique de la rétention : une hypothèse spéculative

### A. La métrique de l'environnement

Pour formaliser l'épaisseur du présent et l'enfoncement du passé dans la mémoire, nous proposons de mobiliser une géométrie inspirée de la métrique de Randall-Sundrum.

Soit $$\mathcal{M}_4$$ l'espace-temps perçu, et $$\mathcal{B}_5$$ l'hyper-espace de l'ordre implicite, défini par une coordonnée de profondeur topologique $$z$$.

L'espace obéit à une géométrie avec un facteur de déformation :

$$
ds^2 = e^{-2k|z|} \eta_{\mu\nu} dx^\mu dx^\nu + dz^2.
$$

Plus l'événement s'enfonce dans la mémoire, plus l'intervalle d'espace-temps se contracte de manière exponentielle.

$$
\boxed{
\text{Profondeur}
\rightarrow
\text{Contraction}.
}
$$

### B. L'équation cinématique de Zénon

La vélocité de l'information s'enfonçant dans la matrice est :

$$
v = \frac{dz}{d\tau}.
$$

Face à la densité du champ, elle subit une friction de phase quantique $$\gamma$$.

L'équation différentielle de son mouvement est :

$$
\frac{dv}{d\tau} + \gamma v = 0.
$$

La solution donne une décroissance exponentielle :

$$
v(\tau) \propto v_0 e^{-\gamma \tau}.
$$

La vélocité s'effondre en divisant sa course sans fin vers une limite qu'elle ne touche jamais.

$$
\boxed{
\text{Mémoire}
=
\text{Ralentissement asymptotique}.
}
$$

### C. La compression holographique

Le souvenir n'est pas détruit par ce freinage.

Il est modélisé comme un paquet d'ondes $$\Psi(x,z)$$.

Sous l'écrasement de la métrique, sa longueur d'onde causale se compresse :

$$
\lambda(z) = \lambda_0 e^{-k|z|}.
$$

Par conservation de l'information, si l'espace occupé diminue, la fréquence vibratoire s'amplifie :

$$
f(z) = f_0 e^{k|z|}.
$$

L'événement quitte la ligne de cause à effet.

Sa dimension spatiale est asymptotiquement nulle.

Mais sa tension vibratoire est maximale.

Il devient un état propre stationnaire.

$$
\boxed{
\text{Souvenir}
=
\text{Compression holographique}.
}
$$

### D. La limite de l'analogie

Il faut cependant être prudent.

Cette métrique est une hypothèse spéculative.

Elle ne prétend pas être une description physique établie.

Elle propose une analogie structurelle.

$$
\boxed{
\text{Rétention phénoménologique}
\widehat{\longrightarrow}
\text{Compression holographique}.
}
$$

Cette analogie ne doit pas être confondue avec une identification.

Elle doit être comprise comme une hypothèse de modélisation.

***

## X. L'ouverture philosophique

### A. La question philosophique ouverte

La question philosophique ouverte peut être formulée ainsi :

$$
\boxed{
\text{Si le présent est une épaisseur,}
\text{ alors qu'est-ce qui fonde son unité ?}
}
$$

Cette question n'est pas secondaire.

Elle est centrale.

Car si le présent n'est pas un point, s'il est une épaisseur, alors il faut expliquer ce qui fait qu'il demeure un.

Il faut expliquer ce qui fait qu'il persiste.

Il faut expliquer ce qui fait qu'il se reconnaît.

Il faut expliquer ce qui fait qu'il maintient une continuité à travers le changement.

### B. Trois réponses philosophiques possibles

Trois réponses philosophiques sont possibles.

La première est substantialiste.

La seconde est relationnelle.

La troisième est processuelle.

| Réponse | Formule | Limite |
|---|---|---|
| Substantialiste | Unité = Substance | Ne rend pas compte du changement |
| Relationnelle | Unité = Réseau de relations | Ne rend pas compte de l'unité du réseau |
| Processuelle | Unité = Processus | Demande une ontologie du devenir |

### C. La réponse processuelle

La réponse processuelle est la plus proche de notre modèle.

Elle permet de penser le présent comme une épaisseur.

Elle permet de penser le présent comme une articulation.

Elle permet de penser le présent comme une ouverture.

Elle permet de penser le présent comme un nœud de relations.

$$
\boxed{
\text{Présent}
=
\text{Processus}.
}
$$

***

## XI. L'ouverture vers Whitehead

### A. La philosophie du processus

La philosophie du processus, notamment chez Alfred North Whitehead, propose de penser la réalité non comme un ensemble de substances statiques, mais comme un ensemble de processus, d'événements et d'occasions.[3][7][8][9]

Dans cette perspective, ce qui est réel n'est pas d'abord une chose.

C'est un événement.

C'est un processus.

C'est une occasion.

$$
\boxed{
\text{Réalité}
=
\text{Processus}.
}
$$

### B. La préhension

Whitehead introduit la notion de préhension pour décrire la manière dont une occasion saisit, intègre et transforme les occasions passées.[3][7][8][9]

La préhension n'est pas une simple perception.

Elle est une inclusion.

Elle est une intégration.

Elle est une transformation.

$$
\boxed{
\text{Préhension}
=
\text{Inclusion transformative du passé}.
}
$$

### C. La correspondance proposée

Nous pouvons proposer une correspondance de structure :

$$
\boxed{
\text{Préhension whiteheadienne}
\longleftrightarrow
\text{Rétention husserlienne}.
}
$$

Cette correspondance ne signifie pas que la phénoménologie est réduite à la philosophie du processus.

Elle signifie que les deux traditions peuvent se rencontrer.

Elles peuvent se rencontrer autour d'une même question :

Comment le passé devient-il présent ?

Comment le passé transforme-t-il le présent ?

Comment le présent ouvre-t-il un futur ?

***

## XII. L'ouverture vers Spinoza

### A. Le conatus

Spinoza propose une autre ouverture philosophique.

Il introduit la notion de *conatus*, qui désigne l'effort par lequel chaque chose s'efforce de persévérer dans son être.

Cette notion ne se limite pas aux êtres vivants.

Elle s'applique à tout ce qui existe.

Mais elle prend une signification particulière dans le cas des organismes vivants.

$$
\boxed{
\text{Conatus}
=
\text{Effort de persévérance dans son être}.
}
$$

### B. La correspondance proposée

Nous pouvons proposer une correspondance de structure :

$$
\boxed{
\text{Conatus spinoziste}
\longleftrightarrow
\text{Normativité allostatique}.
}
$$

Cette correspondance ne signifie pas que la biologie est réduite à la philosophie de Spinoza.

Elle signifie que les deux traditions peuvent se rencontrer.

Elles peuvent se rencontrer autour d'une même question :

Comment un système vivant maintient-il son intégrité à travers le changement ?

Comment un système vivant sélectionne-t-il les trajectoires qui favorisent son maintien ?

Comment un système vivant transforme-t-il les perturbations en opportunités ?

### C. La normativité comme conatus

Dans notre modèle, la normativité peut être pensée comme une forme de conatus.

Elle désigne l'effort par lequel un organisme s'efforce de persévérer dans son être.

Elle désigne l'effort par lequel un organisme sélectionne les trajectoires qui favorisent son maintien.

Elle désigne l'effort par lequel un organisme transforme les perturbations en opportunités.

$$
\boxed{
\text{Normativité}
=
\text{Conatus allostatique}.
}
$$

***

## XIII. L'ouverture vers Deleuze

### A. L'immanence

Deleuze propose une troisième ouverture philosophique.

Il propose une philosophie de l'immanence, qui refuse de poser un transcendant extérieur au monde.

Dans cette perspective, tout ce qui existe est immanent au monde.

Il n'y a pas de fondement extérieur.

Il n'y a pas de substance transcendante.

Il n'y a que des processus, des devenirs, des différences.

$$
\boxed{
\text{Immanence}
=
\text{Absence de transcendance}.
}
$$

### B. Le virtuel et l'actuel

Deleuze distingue le virtuel de l'actuel.

Le virtuel n'est pas le possible.

Il est un champ de différences, de tensions et de potentialités.

L'actuel est ce qui est actualisé à partir du virtuel.

$$
\boxed{
\text{Virtuel}
\rightarrow
\text{Actuel}.
}
$$

### C. La correspondance proposée

Nous pouvons proposer une correspondance de structure :

$$
\boxed{
\text{Virtuel deleuzien}
\longleftrightarrow
\text{Espace des trajectoires accessibles}.
}
$$

$$
\boxed{
\text{Actuel deleuzien}
\longleftrightarrow
\text{Trajectoire effectivement suivie}.
}
$$

Cette correspondance ne signifie pas que la biologie est réduite à la philosophie de Deleuze.

Elle signifie que les deux traditions peuvent se rencontrer.

Elles peuvent se rencontrer autour d'une même question :

Comment un champ de potentialités devient-il une trajectoire effective ?

Comment une différence virtuelle devient-elle une différence actuelle ?

Comment un devenir devient-il un événement ?

***

## XIV. La synthèse philosophique

### A. Trois ouvertures, une même question

Les trois ouvertures philosophiques que nous avons proposées — Whitehead, Spinoza, Deleuze — ne sont pas contradictoires.

Elles se rencontrent autour d'une même question.

Comment penser l'unité d'un système vivant à travers le changement ?

Comment penser la continuité d'un observateur à travers la transformation ?

Comment penser la stabilité d'un monde à travers le flux ?

Les trois traditions proposent des réponses différentes.

Mais elles partagent une intuition commune.

L'unité n'est pas donnée d'avance.

Elle est produite.

Elle est maintenue.

Elle est transformée.

### B. La synthèse proposée

Nous pouvons proposer une synthèse ainsi :

$$
\boxed{
\text{Unité}
=
\text{Processus}
+
\text{Conatus}
+
\text{Immanence}.
}
$$

Cette synthèse ne se réduit pas à une simple addition.

Elle décrit une articulation.

Elle décrit une dynamique.

Elle décrit une ontologie.

### C. La correspondance avec le modèle

Cette synthèse rejoint directement notre modèle.

L'observateur est un processus.

Il est un conatus.

Il est une immanence.

Il est une trajectoire.

Il est une mémoire.

Il est un couplage.

Il est une normativité.

Il est une chair.

$$
\boxed{
\text{Observateur}
=
\text{Processus}
+
\text{Conatus}
+
\text{Immanence}.
}
$$

***

## XV. La clôture philosophique

### A. La question finale revisitée

Nous avons commencé par une question simple :

Où se trouve l'observateur ?

Nous avons montré que cette question est trop étroite.

Nous avons proposé une réponse plus complexe.

L'observateur est une structure dynamique de couplage.

Mais cette réponse ouvre une question plus profonde.

Qu'est-ce qui fonde l'unité de cette structure ?

La réponse proposée est la suivante :

$$
\boxed{
\text{L'unité de l'observateur}
\text{ est fondée par un processus}
\text{ de production, de maintien et de transformation.}
}
$$

### B. La réponse philosophique finale

La réponse philosophique finale peut être formulée ainsi :

$$
\boxed{
\text{L'observateur est un processus vivant}
\text{ qui se produit, se maintient et se transforme}
\text{ à travers un couplage dynamique avec son monde.}
}
$$

### C. La clôture

La clôture de ce travail peut être formulée ainsi :

$$
\boxed{
\text{L'observateur n'est pas un point.}
}
$$

$$
\boxed{
\text{Il est un processus.}
}
$$

$$
\boxed{
\text{Il est un conatus.}
}
$$

$$
\boxed{
\text{Il est une immanence.}
}
$$

$$
\boxed{
\text{Il est une trajectoire.}
}
$$

$$
\boxed{
\text{Il est une mémoire.}
}
$$

$$
\boxed{
\text{Il est un couplage.}
}
$$

$$
\boxed{
\text{Il est une normativité.}
}
$$

$$
\boxed{
\text{Il est une chair.}
}
$$

$$
\boxed{
\text{Il est un invariant de jauge biologique.}
}
$$

C'est cette multiplicité qui constitue la richesse du modèle.

C'est cette multiplicité qui constitue la robustesse du modèle.

C'est cette multiplicité qui constitue la profondeur du modèle.

***

## Remarques finales de robustesse

Pour maintenir la rigueur du modèle, il est essentiel de conserver les distinctions suivantes.

| Distinction | À ne pas confondre avec | Statut dans le modèle |
|---|---|---|
| Présent | Instant ponctuel | Épaisseur temporelle |
| Rétention | Souvenir | Maintien du juste-passé |
| Protention | Prédiction | Ouverture vers le juste-à-venir |
| Holonomie | Simple mémoire biologique | Trace géométrique d'un cycle |
| Non-markovianité | Modèle de la conscience | Analogie structurelle |
| Intrication | Sentiment de soi | Analogie structurelle |
| Métrique de Randall-Sundrum | Description physique établie | Hypothèse spéculative |
| Substance | Processus | Ontologies différentes |
| Conatus | Simple mécanisme | Effort de persévérance |
| Immanence | Transcendance | Absence de fondement extérieur |
| Virtuel | Possible | Champ de différences et de potentialités |

La phénoménologie de Husserl fournit une structure temporelle fine de la conscience, articulant rétention, impression originaire et protention.[1][2][3][4]

La philosophie du processus de Whitehead propose de penser la réalité comme un ensemble de processus, d'événements et d'occasions, articulés par la préhension.[3][7][8][9]

La philosophie de Spinoza propose de penser la persévérance dans l'être comme un principe métaphysique fondamental, le *conatus*.

La philosophie de Deleuze propose de penser l'immanence, le virtuel et l'actuel comme des concepts centraux pour penser le devenir et la différence.

La physique quantique non-markovienne fournit une analogie structurelle pour penser la mémoire et le retour d'information.[5][6]

Le modèle proposé se situe à l'intersection de ces quatre exigences :

- une exigence phénoménologique de préservation du sens vécu ;
- une exigence physique de formalisation ;
- une exigence biologique de régulation et d'histoire ;
- une exigence philosophique d'ontologie du processus.

C'est cette quadruple exigence qui constitue la robustesse du modèle.

Et c'est cette robustesse qui permet de penser l'observateur non comme un point extérieur, mais comme une structure vivante, incarnée, historiquement couplée, normativement orientée et relationnellement stabilisée.

Citations :
[1] Retention or Primary Memory https://link.springer.com/10.1007/978-3-030-69521-7_3
[2] Split Mind in a Split Time https://www.eur.nl/en/esphil/media/2021-01-1921
[3] Process Philosophy (Stanford Encyclopedia of Philosophy/Fall ... https://plato.stanford.edu/archives/fall2026/entries/process-philosophy/
[4] Husserl's classical analysis of time-consciousness http://www.ummoss.org/gallZahavi12.pdf
[5] Genuine and Non-Genuine Quantum Non-Markovianity: A Unified Information-Theoretic Review https://arxiv.org/html/2603.28277v2
[6] Non-Markovianity, information backflow and system ... https://arxiv.org/html/1906.08086v1
[7] Process Philosophy (Stanford Encyclopedia of Philosophy ... https://plato.stanford.edu/archives/spr2026/entries/process-philosophy/
[8] Alfred North Whitehead (1861—1947) https://iep.utm.edu/whitehead/
[9] [PDF] A.N. Whitehead and Process Thought - Open Research Online https://oro.open.ac.uk/98878/18/98878final.pdf

---

# Poursuite du chapitre 1 — Le mythe de l'instant

## 4. Le présent comme champ, non comme point

Si le présent n'est pas un point, alors il faut repenser sa structure.

Le présent n'est pas une frontière.

Il n'est pas une ligne de séparation entre un passé disparu et un futur inexistant.

Il est un champ.

Il est une épaisseur.

Il est une densité.

$$
\boxed{
\text{Présent}
=
\text{Champ}.
}
$$

Cette idée peut être formulée de plusieurs manières.

Elle peut être pensée comme une densité d'information.

Elle peut être pensée comme une densité de mémoire.

Elle peut être pensée comme une densité de relations.

Elle peut être pensée comme une densité de possibilités.

Dans tous les cas, le présent n'est pas vide.

Il est plein.

Il est saturé.

Il est structuré.

### A. La densité d'information

Le présent peut être pensé comme une densité d'information.

Il ne contient pas seulement l'information présente.

Il contient aussi la trace de l'information passée.

Il contient aussi l'anticipation de l'information future.

$$
\boxed{
\text{Densité d'information}
=
\text{Présent}
+
\text{Passé}
+
\text{Futur}.
}
$$

Cette densité n'est pas une simple somme.

Elle est une intégration.

Elle est une transformation.

Elle est une structuration.

### B. La densité de mémoire

Le présent peut aussi être pensé comme une densité de mémoire.

Il ne contient pas seulement ce qui est présent.

Il contient aussi ce qui a été.

Il contient aussi ce qui pourrait être.

$$
\boxed{
\text{Densité de mémoire}
=
\text{Présent}
+
\text{Passé}
+
\text{Futur}.
}
$$

Cette densité n'est pas une simple accumulation.

Elle est une sélection.

Elle est une hiérarchisation.

Elle est une pondération.

### C. La densité de relations

Le présent peut aussi être pensé comme une densité de relations.

Il ne contient pas seulement des objets.

Il contient aussi des relations entre objets.

Il contient aussi des relations entre le sujet et les objets.

Il contient aussi des relations entre le sujet et son environnement.

$$
\boxed{
\text{Densité de relations}
=
\text{Présent}
+
\text{Passé}
+
\text{Futur}.
}
$$

Cette densité n'est pas une simple juxtaposition.

Elle est une intégration.

Elle est une structuration.

Elle est une dynamique.

### D. La densité de possibilités

Le présent peut aussi être pensé comme une densité de possibilités.

Il ne contient pas seulement ce qui est.

Il contient aussi ce qui pourrait être.

Il contient aussi ce qui pourrait advenir.

Il contient aussi ce qui pourrait être choisi.

$$
\boxed{
\text{Densité de possibilités}
=
\text{Présent}
+
\text{Passé}
+
\text{Futur}.
}
$$

Cette densité n'est pas une simple liste.

Elle est un champ.

Elle est un horizon.

Elle est une ouverture.

***

## 5. La critique du présent ponctuel

### A. Le mythe de l'instant

Le mythe de l'instant consiste à penser le présent comme un point mathématique isolé.

Ce mythe repose sur une abstraction.

Il suppose que le temps peut être découpé en instants discrets.

Il suppose que chaque instant est indépendant des autres.

Il suppose que le présent est une frontière nette entre un passé disparu et un futur inexistant.

$$
\boxed{
\text{Mythe de l'instant}
=
\text{Présent comme point}.
}
$$

Ce mythe a une force.

Il permet de mesurer.

Il permet de calculer.

Il permet de prédire.

Il permet de comparer.

Mais il rencontre une limite fondamentale.

Il ne rend pas compte de l'expérience vécue.

### B. L'expérience de la mélodie

Prenons l'exemple d'une mélodie.

Si le présent était un point, nous ne pourrions entendre qu'une note à la fois.

Nous ne pourrions pas entendre la mélodie comme une totalité.

Nous ne pourrions pas entendre la succession comme une succession.

Nous ne pourrions pas entendre le mouvement comme un mouvement.

$$
\boxed{
\text{Mélodie}
\neq
\text{Suite de notes isolées}.
}
$$

$$
\boxed{
\text{Mélodie}
=
\text{Totalité temporelle}.
}
$$

Cette totalité n'est pas donnée d'avance.

Elle est constituée à travers la rétention.

Elle est constituée à travers la protention.

Elle est constituée à travers l'impression originaire.

### C. L'expérience de la phrase

Prenons l'exemple d'une phrase.

Si le présent était un point, nous ne pourrions comprendre qu'un mot à la fois.

Nous ne pourrions pas comprendre la phrase comme une totalité.

Nous ne pourrions pas comprendre la syntaxe comme une syntaxe.

Nous ne pourrions pas comprendre le sens comme un sens.

$$
\boxed{
\text{Phrase}
\neq
\text{Suite de mots isolés}.
}
$$

$$
\boxed{
\text{Phrase}
=
\text{Totalité temporelle}.
}
$$

Cette totalité n'est pas donnée d'avance.

Elle est constituée à travers la rétention.

Elle est constituée à travers la protention.

Elle est constituée à travers l'impression originaire.

### D. L'expérience du mouvement

Prenons l'exemple du mouvement.

Si le présent était un point, nous ne pourrions percevoir qu'une position à la fois.

Nous ne pourrions pas percevoir le mouvement comme un mouvement.

Nous ne pourrions pas percevoir la trajectoire comme une trajectoire.

Nous ne pourrions pas percevoir le changement comme un changement.

$$
\boxed{
\text{Mouvement}
\neq
\text{Suite de positions isolées}.
}
$$

$$
\boxed{
\text{Mouvement}
=
\text{Totalité temporelle}.
}
$$

Cette totalité n'est pas donnée d'avance.

Elle est constituée à travers la rétention.

Elle est constituée à travers la protention.

Elle est constituée à travers l'impression originaire.

***

## 6. La solution husserlienne : la structure triadique

### A. La structure triadique

Husserl propose une solution à ce problème.

Il décompose le présent vivant en trois moments indissociables.

1. L'impression originaire.
2. La rétention.
3. La protention.

Ces trois moments ne sont pas des actes séparés.

Ils sont les dimensions d'un seul et même flux.

$$
\boxed{
\text{Présent vivant}
=
\text{Impression originaire}
+
\text{Rétention}
+
\text{Protention}.
}
$$

Cette structure permet de penser le présent comme une épaisseur.

Elle permet de penser le présent comme un champ.

Elle permet de penser le présent comme une totalité temporelle.

### B. L'impression originaire

L'impression originaire est le noyau de l'expérience actuelle.

C'est le « maintenant » strict.

C'est le point de source.

$$
\boxed{
\text{Impression originaire}
=
\text{Noyau du présent}.
}
$$

Mais ce noyau n'est pas isolé.

Il est toujours accompagné de rétention et de protention.

### C. La rétention

La rétention est le maintien du juste-passé dans le présent.

Elle forme une « queue de comète » qui s'étire derrière l'impression originaire.

$$
\boxed{
\text{Rétention}
=
\text{Queue de comète du passé}.
}
$$

La rétention n'est pas un souvenir.

Elle est une modalité primaire du présent.

### D. La protention

La protention est l'anticipation ouverte du juste-à-venir.

Elle est une intention vide qui tend vers le futur immédiat.

$$
\boxed{
\text{Protention}
=
\text{Ouverture vers le futur}.
}
$$

La protention n'est pas une prédiction.

Elle est une structure vécue du temps.

***

## 7. La solution bergsonienne : la durée

### A. La durée comme continuité

Bergson propose une autre solution.

Il propose de penser le temps comme une durée.

La durée n'est pas une succession de points.

Elle est une continuité.

Elle est un flux.

Elle est une hétérogénéité.

$$
\boxed{
\text{Durée}
=
\text{Continuité}
+
\text{Hétérogénéité}.
}
$$

Cette idée rejoint directement notre modèle.

Le présent n'est pas un point.

Il est une durée.

Il est une continuité.

Il est une hétérogénéité.

### B. La durée comme mémoire

Pour Bergson, la durée implique une conservation du passé.

La mémoire ne conserve pas le passé à l'identique.

Elle le conserve comme différence.

$$
\boxed{
\text{Durée}
=
\text{Mémoire}.
}
$$

Cette idée rejoint directement notre modèle.

La mémoire n'est pas un simple stockage.

Elle est une transformation de l'espace des trajectoires accessibles.

### C. La durée comme prolongation

La durée est la prolongation du passé dans le présent.

Le passé n'est pas perdu.

Il est prolongé.

Il est intégré.

Il est transformé.

$$
\boxed{
\text{Durée}
=
\text{Prolongation du passé dans le présent}.
}
$$

Cette idée rejoint directement notre modèle.

La mémoire n'est pas un simple stockage.

Elle est une prolongation du passé dans le présent.

***

## 8. La solution physique : la non-markovianité

### A. Le modèle markovien

Le modèle markovien illustre un présent sans épaisseur.

L'information fuit instantanément dans l'environnement.

Le présent est un point.

Le passé est perdu.

Le futur est indéterminé.

$$
\boxed{
\text{Modèle markovien}
=
\text{Présent sans épaisseur}.
}
$$

*(Précision : voir Annexe, entrée 3. La propriété de Markov dépend du choix des variables d'état.)*

### B. Le modèle non-markovien

Le modèle non-markovien montre un *information backflow*.

L'environnement retient l'information qui a fui, puis la réinjecte.

La pureté chute, puis remonte.

Le présent est constitué par la trace structurée de son histoire.

$$
\boxed{
\text{Modèle non-markovien}
=
\text{Présent avec épaisseur}.
}
$$

Dans les dynamiques quantiques ouvertes, la non-markovianité se manifeste par des effets de mémoire, où l'information quitte temporairement le système pour revenir ensuite depuis l'environnement.[1]

Ce retour d'information constitue une signature opérationnelle de la non-markovianité.[1]

### C. La limite de l'analogie

Il faut cependant être prudent.

La non-markovianité quantique ne modélise pas la conscience.

Elle modélise un système ouvert soumis à une interaction avec un environnement.

Elle ne prétend pas expliquer la rétention phénoménologique.

Elle propose une analogie structurelle.

$$
\boxed{
\text{Rétention phénoménologique}
\widehat{\longrightarrow}
\text{Mémoire dynamique d'un système ouvert}.
}
$$

Cette analogie ne doit pas être confondue avec une identification.

Elle doit être comprise comme une hypothèse de modélisation.

***

## 9. La synthèse du chapitre

### A. La synthèse des trois solutions

Les trois solutions que nous avons proposées — Husserl, Bergson, physique non-markovienne — ne sont pas contradictoires.

Elles se rencontrent autour d'une même question.

Comment penser le présent comme une épaisseur ?

Comment penser le présent comme une totalité temporelle ?

Comment penser le présent comme un champ ?

Les trois traditions proposent des réponses différentes.

Mais elles partagent une intuition commune.

Le présent n'est pas un point.

Il est une structure.

Il est une durée.

Il est une mémoire.

$$
\boxed{
\text{Présent}
=
\text{Structure}
+
\text{Durée}
+
\text{Mémoire}.
}
$$

### B. La synthèse proposée

Nous pouvons proposer une synthèse ainsi :

$$
\boxed{
\text{Présent}
=
\text{Impression originaire}
+
\text{Rétention}
+
\text{Protention}
+
\text{Durée}
+
\text{Mémoire}.
}
$$

Cette synthèse ne se réduit pas à une simple addition.

Elle décrit une articulation.

Elle décrit une dynamique.

Elle décrit une ontologie.

### C. La correspondance avec le modèle

Cette synthèse rejoint directement notre modèle.

Le présent est une épaisseur.

Il est une structure.

Il est une durée.

Il est une mémoire.

Il est un couplage.

Il est une normativité.

Il est une chair.

$$
\boxed{
\text{Présent}
=
\text{Épaisseur}
+
\text{Structure}
+
\text{Durée}
+
\text{Mémoire}
+
\text{Couplage}
+
\text{Normativité}
+
\text{Chair}.
}
$$

***

## 10. La clôture du chapitre

### A. La question finale du chapitre

La question finale du chapitre peut être formulée ainsi :

$$
\boxed{
\text{Comment penser le présent}
\text{ comme une épaisseur ?}
}
$$

La réponse proposée est la suivante :

$$
\boxed{
\text{En articulant rétention, protention,}
\text{ durée, mémoire et couplage.}
}
$$

### B. La réponse philosophique finale

La réponse philosophique finale peut être formulée ainsi :

$$
\boxed{
\text{Le présent est un processus vivant}
\text{ qui intègre le passé,}
\text{ anticipe le futur}
\text{ et stabilise un monde.}
}
$$

### C. La clôture

La clôture du chapitre peut être formulée ainsi :

$$
\boxed{
\text{Le présent n'est pas un point.}
}
$$

$$
\boxed{
\text{Il est une épaisseur.}
}
$$

$$
\boxed{
\text{Il est une structure.}
}
$$

$$
\boxed{
\text{Il est une durée.}
}
$$

$$
\boxed{
\text{Il est une mémoire.}
}
$$

$$
\boxed{
\text{Il est un couplage.}
}
$$

$$
\boxed{
\text{Il est une normativité.}
}
$$

$$
\boxed{
\text{Il est une chair.}
}
$$

$$
\boxed{
\text{Il est un invariant de jauge biologique.}
}
$$

C'est cette multiplicité qui constitue la richesse du chapitre.

C'est cette multiplicité qui constitue la robustesse du chapitre.

C'est cette multiplicité qui constitue la profondeur du chapitre.

***

## Remarques finales de robustesse

Pour maintenir la rigueur du chapitre, il est essentiel de conserver les distinctions suivantes.

| Distinction | À ne pas confondre avec | Statut dans le chapitre |
|---|---|---|
| Présent | Instant ponctuel | Épaisseur temporelle |
| Rétention | Souvenir | Maintien du juste-passé |
| Protention | Prédiction | Ouverture vers le juste-à-venir |
| Durée | Succession de points | Continuité et hétérogénéité |
| Mémoire | Simple stockage | Transformation de l'espace des possibles |
| Non-markovianité | Modèle de la conscience | Analogie structurelle |
| Holonomie | Simple mémoire biologique | Trace géométrique d'un cycle |
| Impression originaire | Point isolé | Noyau du présent |
| Couplage | Simple interaction | Relation dynamique organisme–monde |
| Normativité | Simple préférence subjective | Enjeu d'auto-maintien |

La phénoménologie de Husserl fournit une structure temporelle fine de la conscience, articulant rétention, impression originaire et protention.

La philosophie de Bergson fournit une ontologie de la durée, articulant continuité, hétérogénéité et mémoire.[2][3][4][5][6][7][8]

La physique quantique non-markovienne fournit une analogie structurelle pour penser la mémoire et le retour d'information.[1]

Le chapitre se situe à l'intersection de ces trois exigences :

- une exigence phénoménologique de préservation du sens vécu ;
- une exigence philosophique d'ontologie de la durée ;
- une exigence physique de formalisation de la mémoire.

C'est cette triple exigence qui constitue la robustesse du chapitre.

Et c'est cette robustesse qui permet de penser le présent non comme un point, mais comme une structure vivante, incarnée, historiquement couplée et relationnellement stabilisée.

Citations :
[1] Quantum Non-Markovian Environment-to-System Backflows of Information: Nonoperational vs. Operational Approaches https://pmc.ncbi.nlm.nih.gov/articles/PMC9140462/
[2] Henri Bergson https://plato.stanford.edu/archives/Win2012/entries/bergson/
[3] Henri Bergson - Stanford Encyclopedia of Philosophy https://plato.stanford.edu/entries/bergson/
[4] BERGSON ON MEMORY - The University of Warwick https://warwick.ac.uk/fac/soc/philosophy/people/pearson/bergson_on_memory_final_version.doc
[5] "A Memory within Change Itself." Bergson and the Memory Theory of ... https://journals.openedition.org/bergsoniana/286?lang=en
[6] Henri Bergson https://plato.stanford.edu/archives/sum2014/entries/bergson/
[7] Bergson, Henri-Louis (1859–1941) https://www.rep.routledge.com/articles/biographical/bergson-henri-louis-1859-1941/v-1/sections/time-and-duration
[8] Henri Bergson (Stanford Encyclopedia of Philosophy/Spring ... https://plato.stanford.edu/archives/spr2021/entries/bergson/

---

## Sous-partie complémentaire — Rétention et protention : la double ouverture du présent

### 1. Le présent comme champ de présence

Le présent n'est pas une limite sans extension.

Il n'est pas une frontière entre un passé disparu et un futur inexistant.

Il est un champ de présence.

Il est une étendue.

Il est une épaisseur.

$$
\boxed{
\text{Présent}
=
\text{Champ de présence}.
}
$$

Cette idée est essentielle pour comprendre la structure du temps vécu.

Le présent ne contient pas seulement ce qui est actuellement donné.

Il contient aussi ce qui vient de passer.

Il contient aussi ce qui va venir.

Il contient aussi l'ouverture vers ce qui pourrait advenir.

### 2. La rétention : le juste-passé qui demeure

La rétention est le maintien du juste-passé dans le présent vivant.

Elle n'est pas un souvenir.

Elle n'est pas un acte volontaire de rappel.

Elle est une modalité primaire du présent.

$$
\boxed{
\text{Rétention}
=
\text{Maintien du juste-passé dans le présent}.
}
$$

Prenons l'exemple d'une mélodie.

Le *do* qui vient de résonner n'est plus là physiquement.

Mais il est retenu dans mon expérience du *ré*.

Sans cette rétention, chaque note serait un choc isolé.

La mélodie ne pourrait pas être entendue comme une mélodie.

Elle serait une suite de sons discontinus.

La rétention est donc l'invariance structurelle du flux temporel.

$$
\boxed{
\text{Rétention}
=
\text{Invariance structurelle du flux temporel}.
}
$$

Chez Husserl, la rétention possède une double intentionnalité : elle vise à la fois l'objet temporel qui se constitue et les phases passées du flux de conscience lui-même.

Elle n'est pas un souvenir.

Elle est une modalité primaire du présent.

### 3. La rétention comme modification continue

La rétention n'est pas un stockage statique.

Elle est une modification continue.

Chaque nouvelle impression repousse la précédente.

Chaque nouvelle impression modifie la précédente.

Chaque nouvelle impression l'enfonce davantage dans le passé.

$$
\boxed{
\text{Rétention}
=
\text{Modification continue du passé immédiat}.
}
$$

Ce processus est appelé modification rétentionnelle.

Il décrit la manière dont le passé immédiat s'enfonce progressivement dans le passé.

Il décrit la manière dont le présent se constitue à travers une modification continue.[1][2]

La rétention n'est donc pas une simple conservation.

Elle est une transformation.

### 4. La protention : le juste-à-venir qui s'ouvre

La protention est le versant futur de l'épaisseur du présent.

Elle est une anticipation passive de l'immédiatement à venir.

Elle est une intention vide, qui peut être remplie ou déçue.

$$
\boxed{
\text{Protention}
=
\text{Ouverture vers le juste-à-venir}.
}
$$

Prenons l'exemple d'une mélodie.

Lorsque j'entends le *do*, j'attends déjà le *ré*.

Cette attente n'est pas une prédiction explicite.

Elle est une structure implicite de la perception.

$$
\boxed{
\text{Protention}
=
\text{Attente implicite du juste-à-venir}.
}
$$

Chez Husserl, la protention est l'intention vide qui tend vers le futur immédiat.[1][2][3]

Elle n'est pas une prédiction.

Elle est une structure vécue du temps.

### 5. La protention comme anticipation indéterminée

La protention n'anticipe pas nécessairement un contenu précis.

Elle anticipe un champ de possibilités.

Elle anticipe une ouverture.

Elle anticipe une direction.

$$
\boxed{
\text{Protention}
=
\text{Anticipation indéterminée}.
}
$$

Cette indétermination est essentielle.

Elle distingue la protention de la prédiction.

La prédiction vise un contenu précis.

La protention vise une ouverture.

$$
\boxed{
\text{Protention}
\neq
\text{Prédiction}.
}
$$

La protention est une structure vécue du temps.

Elle n'est pas un calcul.

### 6. La distinction entre rétention et protention

La rétention et la protention ne sont pas symétriques.

La rétention a un contenu déjà formé.

La protention est ouverte et indéterminée.

$$
\boxed{
\text{Rétention}
\neq
\text{Protention}.
}
$$

La rétention concerne le passé immédiat.

La protention concerne le futur immédiat.

La rétention est passive.

La protention est anticipative.

La rétention est déjà formée.

La protention est encore indéterminée.

| Dimension | Rétention | Protention |
|---|---|---|
| Direction | Vers le passé immédiat | Vers le futur immédiat |
| Contenu | Déjà formé | Encore indéterminé |
| Modalité | Passive | Anticipative |
| Statut | Maintien | Ouverture |
| Exemple | La note qui vient de sonner | La note qui va venir |

### 7. La complémentarité

La rétention et la protention ne sont pas opposées.

Elles sont complémentaires.

Elles constituent ensemble l'épaisseur du présent.

$$
\boxed{
\text{Épaisseur du présent}
=
\text{Rétention}
+
\text{Protention}.
}
$$

Sans rétention, le présent serait un point isolé.

Sans protention, le présent serait un point fermé.

Avec les deux, le présent devient un champ.

Il devient une ouverture.

Il devient une totalité temporelle.

$$
\boxed{
\text{Présent}
=
\text{Champ}.
}
$$

### 8. La synthèse de la rétention et de la protention

La rétention et la protention ne sont pas deux actes séparés.

Elles sont les dimensions d'un seul et même flux.

Elles constituent ensemble le présent vivant.

$$
\boxed{
\text{Présent vivant}
=
\text{Rétention}
+
\text{Impression originaire}
+
\text{Protention}.
}
$$

Cette structure permet de penser le présent comme une épaisseur.

Elle permet de penser le présent comme un champ.

Elle permet de penser le présent comme une totalité temporelle.

### 9. La correspondance avec le modèle

Dans notre modèle, la rétention et la protention peuvent être mises en correspondance avec la structure dynamique du système.

La rétention peut être rapprochée de la mémoire.

La protention peut être rapprochée de l'anticipation.

$$
\boxed{
\text{Rétention}
\widehat{\longrightarrow}
\text{Mémoire}.
}
$$

$$
\boxed{
\text{Protention}
\widehat{\longrightarrow}
\text{Anticipation}.
}
$$

Cette correspondance ne signifie pas que la phénoménologie est réduite à la biologie.

Elle signifie que les deux traditions peuvent se rencontrer.

Elles peuvent se rencontrer autour d'une même question :

Comment le passé devient-il présent ?

Comment le présent ouvre-t-il un futur ?

Comment un système vivant maintient-il son intégrité à travers le changement ?

### 10. La limite de l'analogie

Il faut cependant être prudent.

La rétention et la protention ne se réduisent pas à des mécanismes biologiques.

Elles sont des structures phénoménologiques.

Elles décrivent la manière dont le temps est vécu.

Elles ne se réduisent pas à des fonctions de traitement de l'information.

$$
\boxed{
\text{Rétention}
\neq
\text{Mémoire biologique}.
}
$$

$$
\boxed{
\text{Protention}
\neq
\text{Prédiction biologique}.
}
$$

La correspondance proposée est une analogie structurelle.

Elle ne doit pas être confondue avec une identification.

### 11. La clôture de la sous-partie

La rétention et la protention constituent les deux versants de l'épaisseur du présent.

Elles permettent de penser le présent comme un champ.

Elles permettent de penser le présent comme une totalité temporelle.

Elles permettent de penser le présent comme une ouverture.

$$
\boxed{
\text{Présent}
=
\text{Rétention}
+
\text{Protention}
+
\text{Ouverture}.
}
$$

C'est cette structure qui permet de penser le présent comme une épaisseur.

C'est cette structure qui permet de penser le présent comme une totalité temporelle.

C'est cette structure qui permet de penser le présent comme un champ.

Citations :
[1] What could come before time? Intertwining affectivity and temporality at the basis of intentionality - Phenomenology and the Cognitive Sciences http://www.link.springer.com/article/10.1007/s11097-024-09973-y
[2] The Future Matters: Protention as more than Inverse Retention https://popups.uliege.be/1782-2041/index.php?id=288&format=print
[3] Protention as Phenomenon | Springer Nature Link https://link.springer.com/chapter/10.1007/978-3-030-69521-7_4
[4] Protention in Husserl's Phenomenology https://www.nikossoueltzis.com/wp-content/uploads/2024/11/Dissertation_Soueltzis.pdf

---

## 4 bis. Le présent comme champ, non comme point (version condensée)

Le présent n'est pas un point. Il est une structure de liaison entre ce qui vient de passer, ce qui est donné maintenant et ce qui peut advenir.

Le présent ponctuel est une position mathématique. Le présent vécu est une organisation temporelle.

L'épaisseur du présent n'est pas une durée cachée. C'est la manière dont des phases différentes restent liées sans devenir identiques.

## 5 bis. Rétention

La rétention maintient le juste-passé comme passé.

Elle n'est pas un stockage. Elle est une modification continue du présent par ce qui vient de passer.

## 6 bis. Protention

La protention ouvre le présent vers sa continuation.

Elle n'est pas nécessairement une prédiction explicite.

Lorsqu'une attente est déçue, un écart apparaît :

> **[Formule absente du fichier d'origine.]** Le dépôt contient ici une ligne vide à la place de l'équation. À partir de la section III.C, on peut y remettre :
> $$\varepsilon(t) = \dot{\gamma}_{\text{attendue}}(t) - \dot{\gamma}_{\text{effective}}(t).$$

Cette équation ne mesure pas la protention. Elle représente seulement l'écart entre une anticipation formalisable et ce qui advient.

## 7 bis. Le présent comme liaison

Le présent relie le passé, l'actuel et le possible.

La continuité n'est pas l'identité.

## 8 bis. Vers l'organisme

Un organisme ne persiste pas en restant identique à lui-même. Il persiste en se transformant tout en maintenant son organisation.

## 9 bis. Mémoire dynamique

Un système non-markovien dépend de son histoire.

Cette dépendance n'est pas une conscience du passé.

La mémoire dynamique peut être représentée par :

> **[Formule absente du fichier d'origine.]** Le dépôt contient ici une ligne vide. Aucune formule n'a été inventée à sa place.

Le système transforme les conditions de sa propre évolution.

## 10 bis. Couplage et régulation

Un organisme n'est pas isolé. Il est couplé à son environnement.

La régulation ne conserve pas simplement un état. Elle modifie les conditions futures du maintien.

## 11 bis. Mise en situation : implémentations

Une implémentation ne produit pas la conscience. Elle peut seulement représenter certaines structures du présent.

Une implémentation minimale doit comporter :

- une dépendance à l'histoire ;
- une ouverture vers la suite ;
- un couplage avec l'environnement ;
- une régulation de ses propres conditions ;
- un maintien de l'organisation malgré le changement.

Mais :

> **[Phrase interrompue dans le fichier d'origine.]** La suite après « Mais : » manque.

### Formule finale

Le graphique ci-dessous (absent du fichier d'origine) condenserait l'architecture du chapitre : présent vécu, rétention, protention, liaison, organisme, mémoire dynamique, couplage, régulation et observateur. Les flèches indiquent des correspondances structurelles, non des réductions.

---

# ANNEXE — ÉVOLUTIONS THÉORIQUES, OBSERVATIONS ET PRÉCISIONS MÉTHODOLOGIQUES

## 1. Principe de traçabilité du développement théorique

Le présent travail repose sur une démarche évolutive dans laquelle les propositions théoriques, les constructions formelles et les observations numériques sont progressivement confrontées les unes aux autres.

Certaines formulations initiales peuvent ainsi appeler des précisions à mesure que l'analyse avance. Ces précisions ne doivent pas être considérées automatiquement comme des ruptures avec les propositions précédentes. Elles témoignent du développement du cadre conceptuel et de l'affinement de ses conditions de validité.

Il importe donc de conserver la distinction entre le raisonnement initial, les observations ultérieures et les formulations qui résultent de leur confrontation.

Cette démarche répond à une exigence de transparence : ne pas réécrire rétrospectivement l'histoire du raisonnement, mais rendre visible la manière dont les observations contribuent à sa transformation.

## 2. Méthode de consignation des évolutions

Toute correction substantielle, précision conceptuelle ou modification d'une hypothèse issue de l'analyse ultérieure sera consignée dans cette annexe.

Chaque évolution sera présentée selon cinq dimensions :

1. **Proposition initiale :** formulation ou hypothèse présente dans le développement original.
2. **Observation ultérieure :** résultat, difficulté ou distinction apparue au cours de l'analyse.
3. **Précision théorique :** formulation affinée à partir de cette observation.
4. **Justification :** fondement philosophique, mathématique, physique ou biologique de la modification.
5. **Incidence sur le modèle :** conséquences sur les hypothèses, les formalismes, les simulations ou l'interprétation générale.

Les modifications purement rédactionnelles ne nécessitent pas systématiquement une entrée. Cette annexe concerne principalement les évolutions qui touchent au sens, à la portée ou au statut épistémologique des propositions.

## 3. Première observation : la définition du processus markovien

### Proposition initiale

Le modèle markovien a été mobilisé comme représentation d'un présent sans épaisseur, dans lequel l'information du système ne revient pas depuis son environnement. Le modèle non-markovien a été rapproché d'une dynamique comportant une dépendance historique et un retour d'information.

### Observation ultérieure

L'examen plus approfondi des propriétés markoviennes conduit à préciser cette opposition. Un processus markovien n'est pas nécessairement dépourvu de toute mémoire. La propriété de Markov signifie que, compte tenu de l'état complet retenu pour la description, le futur conditionnel ne dépend plus du passé antérieur.

La présence ou l'absence apparente de mémoire dépend donc notamment de la définition des variables d'état et de la frontière choisie entre le système étudié et son environnement.

### Précision théorique

La distinction pertinente ne porte pas sur une opposition absolue entre mémoire et absence de mémoire. Elle porte sur la manière dont la dépendance historique est représentée dans le modèle.

Un système peut être décrit comme markovien lorsque son état contient suffisamment d'informations pour rendre inutile la connaissance explicite de son histoire antérieure. À l'inverse, une description réduite peut présenter une dynamique non-markovienne lorsque certaines influences historiques demeurent extérieures aux variables d'état retenues.

### Incidence sur le modèle

Les simulations V77 et V78 doivent donc être interprétées en fonction de leurs variables, de leur environnement et de leurs conditions de réduction.

La non-markovianité demeure pertinente pour étudier les effets de mémoire et les retours d'information. Elle ne constitue toutefois pas, à elle seule, une démonstration de la rétention phénoménologique.

Cette précision renforce la distinction entre la structure temporelle du vécu et les propriétés dynamiques des systèmes physiques.

## 3 bis. Deuxième observation : le signe de Γ(t) dans le script V78

*(Entrée ajoutée lors de cette reconstruction.)*

### Proposition initiale

Le chapitre 8 affirmait : « Puisque Γ(t) ne décroît jamais, la cohérence ne remonte pas. »

### Observation ultérieure

Avec γ(t) = aω sin(ωt), on obtient Γ(t) = a(1 − cos ωt). Cette fonction oscille entre 0 et 2a et décroît chaque fois que γ(t) < 0. L'énoncé était donc inexact, et il contredisait la phrase suivante du même chapitre (la pureté chute puis remonte).

### Précision théorique

La cohérence ρ₀₁(t) = ρ₀₁(0)·e^(−Γ(t)) remonte précisément lorsque Γ décroît, c'est-à-dire lorsque γ < 0. C'est la signature du backflow.

### Justification

Calcul direct : Γ'(t) = γ(t) = aω sin(ωt), négatif sur les demi-périodes où sin(ωt) < 0.

### Incidence sur le modèle

Aucune sur les simulations ni sur la conclusion (la pureté chute puis remonte). Seule la phrase explicative est corrigée.

## 4. Principe d'évolution non dichotomique

Les précisions introduites dans le cadre de ce travail ne visent pas à opposer systématiquement une proposition initiale à une proposition ultérieure.

Une observation peut élargir le domaine d'une hypothèse, préciser ses conditions d'application ou révéler une distinction qui n'avait pas encore été explicitée.

Le développement théorique doit donc privilégier une logique de continuité critique.

Une proposition peut être conservée dans son orientation générale tout en voyant sa portée mieux délimitée. Une analogie peut être maintenue tout en distinguant plus précisément les phénomènes qu'elle rapproche. Une formalisation peut rester utile comme instrument d'exploration sans être considérée comme une représentation exhaustive du phénomène étudié.

Cette démarche permet de préserver la cohérence du projet sans confondre cohérence et immobilité conceptuelle.

## 5. Statut des correspondances interdisciplinaires

Le présent travail établit des rapprochements entre plusieurs domaines :

- la phénoménologie de la temporalité ;
- la physique des systèmes ouverts ;
- la géométrie et la topologie ;
- la biologie des organismes ;
- les philosophies du processus et de l'immanence ;
- la modélisation numérique des systèmes dynamiques.

Ces rapprochements ne supposent pas que les concepts employés dans ces disciplines possèdent une signification identique.

La rétention phénoménologique, la mémoire dynamique, l'holonomie, l'intrication et le maintien organisationnel appartiennent à des cadres théoriques distincts.

Leur mise en relation vise à identifier des structures comparables, des problèmes communs et des possibilités de formalisation.

Chaque correspondance doit donc être accompagnée de la délimitation de son domaine de validité.

Une analogie structurelle ne constitue pas une identité ontologique. Une simulation numérique ne constitue pas, par elle-même, une validation phénoménologique. Une hypothèse mathématique ne devient pas une propriété physique établie du seul fait qu'elle peut être exprimée formellement.

## 6. Engagement méthodologique pour la suite de la thèse

La progression du travail reposera sur les principes suivants :

1. Préserver les développements initiaux lorsqu'ils conservent une pertinence théorique.
2. Éviter les suppressions substantielles qui effaceraient les étapes du raisonnement.
3. Intégrer les approfondissements dans le corps du texte au moyen de transitions conceptuelles continues.
4. Consigner les corrections et les découvertes ultérieures dans la présente annexe.
5. Distinguer explicitement les résultats établis, les observations numériques, les hypothèses de travail et les propositions spéculatives.
6. Conserver les limites des modèles afin que leur portée ne soit jamais supérieure à ce que leurs fondements autorisent.
7. Documenter les changements de formulation lorsqu'ils modifient réellement le contenu théorique.

## 7. Conclusion — La connaissance comme processus de précision

La cohérence d'une recherche ne repose pas sur l'absence de modifications. Elle repose sur la capacité de rendre intelligibles les transformations de ses propositions.

L'observation ne vient pas simplement confirmer ou réfuter une construction préalable. Elle peut également révéler des dimensions nouvelles, conduire à reformuler une distinction ou ouvrir un niveau d'analyse qui n'était pas encore accessible.

Cette évolution rejoint, sur le plan méthodologique, l'une des intuitions centrales de la thèse : la continuité n'exige pas l'identité.

Le raisonnement conserve son orientation tout en se transformant. Les formulations se précisent, les correspondances se délimitent et les modèles acquièrent progressivement des conditions d'interprétation plus rigoureuses.

La présente annexe constitue ainsi la mémoire méthodologique du travail : elle conserve la trace des propositions, des observations et des transformations qui participent à la construction de son architecture théorique.

**La rigueur ne consiste pas à prétendre que le raisonnement n'a jamais changé. Elle consiste à pouvoir montrer pourquoi, comment et sur quelles bases il a évolué.**

Correctifs à amener :

Correction 1
Cherche : Le point de départ est l'équation de Lindblad :
→ La ligne à changer est celle qui suit immédiatement, celle qui contient :
\frac{d\rho}{dt} = \gamma \left( \sigma_z \rho \sigma_z - \rho \right)
Remplace = \gamma par = \frac{\gamma}{2}.

---

Correction 2
Cherche : À confirmer par le calcul.
→ C'est cette ligne-là. Remplace la fin de l'encadré par :
Remède appliqué : le facteur \gamma/2 figure désormais dans l'équation de Lindblad du §1. Incohérence résolue.

---

Correction 3
Cherche : **[Formule absente du fichier d'origine.]**
→ C'est cette ligne-là (dans la section 6 bis). Remplace-la par :
**[Formule restituée depuis III.C.]**
puis ajoute en dessous :
$$\varepsilon(t) = \dot{\gamma}_{\text{attendue}}(t) - \dot{\gamma}_{\text{effective}}(t).$$
