Illustration formelle — Décroissance et reprises de cohérence
Place dans la thèse
Cette note accompagne le chapitre 1, « Le mythe de l’instant ». Elle expose le rôle et les limites des simulations V77 et V78 dans le raisonnement philosophique.
1. Fonction de l’illustration
Les simulations rendent visibles deux formes d’évolution : une décroissance monotone et une évolution comportant des reprises. Elles ne constituent pas une démonstration physique de l’épaisseur du présent vécu.
La comparaison est une proposition de lecture : elle invite à distinguer perte progressive, persistance et reprise, sans identifier mémoire physique et rétention phénoménologique.
2. Modèle commun
On considère un qubit soumis à une équation maîtresse locale en temps de déphasage pur :
Lorsque le taux devient négatif, le générateur instantané n’est plus de forme GKSL à taux positifs. Cela ne signifie pas nécessairement que l’évolution depuis l’instant initial cesse d’être physique : il faut examiner le canal complet.
Résolution analytique
Pour une matrice densité générale :
le calcul du terme de déphasage donne :
Il s’ensuit :
En définissant le taux intégré :
on obtient :
Pour l’état initial équilibré :
la solution est :
Pureté
Donc :
3. V77 — Décroissance monotone
Pour un taux constant positif :
on obtient :
La matrice densité converge vers le mélange maximal I/2. Cette limite résulte ici des populations initiales équilibrées ; le déphasage conserve les populations pour tout état initial.
Cette évolution ne signifie pas que le système efface son passé à chaque instant. Le qualificatif « markovien » relève ici des propriétés du semi-groupe dynamique et ne décrit pas le présent subjectif.
4. V78 — Reprises de cohérence
On construit :
Le paramètre a est sans dimension ; la fréquence omega et le taux gamma ont la dimension d’un inverse de temps.
Validité du canal depuis l’instant initial
Puisque Gamma reste non négatif, le facteur de cohérence :
reste dans l’intervalle ]0,1]. Le canal s’écrit :
Cette combinaison convexe de deux canaux unitaires est complètement positive et conserve la trace (CPTP).
CP-divisibilité et distinguabilité
Pour k entier non négatif, le taux devient négatif lorsque :
Sur ces intervalles, la famille de canaux n’est pas CP-divisible : elle présente une non-markovianité au sens du critère de Rivas–Huelga–Plenio (RHP).
Le critère de Breuer–Laine–Piilo (BLP) porte, lui, sur l’augmentation de la distance de trace entre certains états. Pour les états initiaux orthogonaux |+> et |-> :
leurs états évolués vérifient :
La distinguabilité augmente donc lorsque gamma est négatif. Les deux critères concordent pour cette construction de déphasage, sans être équivalents en général.
Reprises et minima
Aux instants de retour :
on a Gamma(t_n)=0, donc :
Aux instants intermédiaires :
Gamma atteint 2a et la pureté atteint :
Le modèle décrit des reprises complètes après un déphasage partiel, sans atteindre exactement le mélange maximal pour a fini.
Les reprises sont construites par le choix de Gamma. Elles s’accompagnent d’une augmentation de la distinguabilité, interprétée dans le cadre BLP comme un retour d’information. Aucun réservoir microscopique n’est explicitement modélisé ici.
5. Portée philosophique
La simulation accompagne la réflexion sur la persistance dans le changement. Elle ne démontre ni la rétention husserlienne, ni une mémoire consciente, ni un accès physique au passé.
Retrouver une valeur de pureté ne signifie pas retrouver un événement passé. Dans cette construction, le retour de l’état réduit initial est une propriété de l’évolution choisie, non un voyage temporel.
L’argument philosophique guide le choix de l’illustration ; l’illustration aide à le comprendre, sans le certifier.
6. Contrôles techniques
Trace : Tr(rho(t)) = 1.
Hermiticité : rho(t) est égale à son adjointe.
Valeurs propres :
Pureté : elle reste comprise entre 1/2 et 1.
Validité du canal : vérifier la représentation comme combinaison convexe donnée ci-dessus.
Contrôle numérique prévu : comparer une intégration indépendante à la solution analytique et vérifier la convergence lorsque le pas diminue. Le script évaluant directement la solution exacte ne réalise pas ce test indépendant.
Discrétisation : inclure l’état initial et les N étapes sur N+1 points ; choisir un pas nettement inférieur à la période 2 pi / omega, puis contrôler la convergence. Un échantillonnage fin ne remplace pas un contrôle d’erreur.
7. Statut des énoncés
[Construction formelle] Choix des équations et de Gamma.
[Résultat analytique] Expressions de la matrice densité, de la pureté et de la distance de trace.
[À vérifier par exécution] Concordance des scripts déposés avec les solutions et convergence de l’intégration indépendante.
[Analogie philosophique] Comparaison entre persistance, reprise et temporalité vécue.
[Limite] Aucun résultat concernant la conscience, l’intentionnalité ou la rétrocausalité n’est établi.
Références de travail
Rivas, Huelga et Plenio : critère de CP-divisibilité.
Breuer, Laine et Piilo : critère fondé sur la distance de trace.
Synthèse : « Non-Markovian quantum dynamics: What does it mean? » https://arxiv.org/abs/2001.02252
Déphasage et divisibilité : « Quantum regression in dephasing phenomena » https://arxiv.org/abs/2202.11056
Les données bibliographiques complètes et les renvois précis seront vérifiés avant la version finale.
