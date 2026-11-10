Voici une version corrigée, nettoyée des artéfacts d'encodage (caractères mal décodés / *mojibake*) et formellement complétée avec toutes les équations mathématiques détaillées étape par étape.

---

# Illustration formelle — Décroissance et reprises de cohérence

## Place dans la thèse

Cette note accompagne le chapitre 1, « Le mythe de l’instant ». Elle expose le rôle et les limites des simulations V77 et V78 dans le raisonnement philosophique.

---

## 1. Fonction de l’illustration

Les simulations rendent visibles deux formes d’évolution : une décroissance monotone et une évolution comportant des reprises. Elles ne constituent pas une démonstration physique de l’épaisseur du présent vécu.

La comparaison est une proposition de lecture : elle invite à distinguer perte progressive, persistance et reprise, sans identifier mémoire physique et rétention phénoménologique.

---

## 2. Modèle commun

On considère un qubit soumis à une équation maîtresse de déphasage pur (équation de type Lindblad généralisée à taux dépendant du temps) :

$$\frac{d\rho(t)}{dt} = \frac{\gamma(t)}{2} \bigl(\sigma_z \rho(t) \sigma_z - \rho(t)\bigr)$$

où $\sigma_z$ est la matrice de Pauli :

$$\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

### Résolution analytique

Pour une matrice densité générale $2 \times 2$ :

$$\rho(t) = \begin{pmatrix} \rho_{00}(t) & \rho_{01}(t) \\ \rho_{10}(t) & \rho_{11}(t) \end{pmatrix}$$

Le commutateur et le dissipateur donnent :

$$\sigma_z \rho \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} \rho_{00} & -\rho_{01} \\ -\rho_{10} & \rho_{11} \end{pmatrix}$$

En insérant ce résultat dans l'équation maîtresse :

1. **Populations (éléments diagonaux) :**
   $$\frac{d\rho_{00}}{dt} = 0, \qquad \frac{d\rho_{11}}{dt} = 0$$
   Les populations demeurent strictement constantes au cours du temps.

2. **Cohérences (éléments hors diagonaux) :**
   $$\frac{d\rho_{01}(t)}{dt} = -\gamma(t) \rho_{01}(t)$$

En posant le taux intégré de décohérence :

$$\Gamma(t) = \int_0^t \gamma(s) \, ds$$

L'intégration donne directement :

$$\rho_{01}(t) = \rho_{01}(0) e^{-\Gamma(t)}$$

Pour l'état initial en superposition équilibrée $|\psi(0)\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ :

$$\rho(0) = \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$

La matrice densité à l'instant $t$ s'écrit donc :

$$\rho(t) = \frac{1}{2} \begin{pmatrix} 1 & e^{-\Gamma(t)} \\ e^{-\Gamma(t)} & 1 \end{pmatrix}$$

### Pureté du système

La pureté $P(t) = \operatorname{Tr}(\rho^2(t))$ se déduit des composantes :

$$P(t) = \rho_{00}^2(t) + \rho_{11}^2(t) + 2 |\rho_{01}(t)|^2 = \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 + 2 \left(\frac{1}{2} e^{-\Gamma(t)}\right)^2$$

$$P(t) = \frac{1}{4} + \frac{1}{4} + \frac{1}{2} e^{-2\Gamma(t)} = \frac{1}{2} \bigl[1 + e^{-2\Gamma(t)}\bigr]$$

---

## 3. V77 — Décroissance monotone

Pour un taux constant positif $\gamma(t) = \gamma_0 > 0$ :

$$\Gamma(t) = \gamma_0 t$$

- **Cohérence :** $\rho_{01}(t) = \frac{1}{2} e^{-\gamma_0 t} \xrightarrow[t \to +\infty]{} 0$
- **Pureté :** $P(t) = \frac{1}{2} \bigl[1 + e^{-2\gamma_0 t}\bigr] \xrightarrow[t \to +\infty]{} \frac{1}{2}$

La pureté décroît de façon strictement monotone depuis $1$ (état pur) vers l'état de mélange maximal diagonal $\frac{1}{2}\mathbb{I}_2$ avec $P = \frac{1}{2}$. 

Cette évolution ne signifie pas que le système efface son passé à chaque instant. Le qualificatif « markovien » relève ici d'une propriété du semi-groupe dynamique et ne constitue pas une description du présent subjectif.

---

## 4. V78 — Reprises de cohérence

On choisit une dynamique non monotone définie par :

$$\Gamma(t) = a [1 - \cos(\omega t)], \qquad \gamma(t) = \frac{d\Gamma(t)}{dt} = a \omega \sin(\omega t), \qquad a > 0$$

- Puisque $1 - \cos(\omega t) \ge 0$, on a $\Gamma(t) \ge 0$ pour tout $t \ge 0$. Le canal dynamique $\Lambda_{t,0}$ reste **complètement positif et conservant la trace (CPTP)** depuis l'instant initial $t=0$.
- Cependant, $\gamma(t) < 0$ sur les intervalles où $\sin(\omega t) < 0$ (c'est-à-dire $t \in \left]\frac{(2k+1)\pi}{\omega}, \frac{(2k+2)\pi}{\omega}\right[$). Le semi-groupe perd alors sa **CP-divisibilité** (critère de non-markovianité de Rivas-Huelga-Plenio / Breuer-Laine-Piilo).

### Conséquences sur la dynamique
- **Cohérence :** $\rho_{01}(t) = \frac{1}{2} \exp\bigl(-a [1 - \cos(\omega t)]\bigr)$
- **Pureté :** $P(t) = \frac{1}{2} \Bigl[1 + \exp\bigl(-2a [1 - \cos(\omega t)]\bigr)\Bigr]$

Aux instants $t_n = \frac{2n\pi}{\omega}$ ($n \in \mathbb{N}$) :
$$\cos(\omega t_n) = 1 \implies \Gamma(t_n) = 0 \implies \rho(t_n) = \rho(0) \implies P(t_n) = 1$$

La cohérence et la pureté oscillent périodiquement et reviennent exactement à leur valeur initiale. Ces reprises résultent de l'inversion de flux d'information modélisée par le taux $\gamma(t)$ négatif, et non d'une mémoire phénoménologique spontanée.

---

## 5. Portée philosophique

La simulation accompagne la réflexion sur la persistance dans le changement. Elle ne démontre ni la rétention husserlienne, ni une mémoire consciente, ni un accès physique au passé.

Retrouver une valeur de pureté ne signifie pas retrouver un événement passé. Dans ce modèle particulier, le retour complet de la cohérence est une propriété de l'évolution choisie, non un voyage temporel.

---

## 6. Contrôles techniques

- **Trace :** $\operatorname{Tr}(\rho(t)) = \rho_{00}(t) + \rho_{11}(t) = \frac{1}{2} + \frac{1}{2} = 1$.
- **Hermiticité :** $\rho^\dagger(t) = \rho(t)$, car $\rho_{01}(t) = \rho_{10}(t) \in \mathbb{R}$.
- **Positivité des valeurs propres :**
  $$\lambda_\pm = \frac{1}{2} \bigl(1 \pm e^{-\Gamma(t)}\bigr)$$
  Puisque $\Gamma(t) \ge 0$, $0 < e^{-\Gamma(t)} \le 1$, donc $\lambda_\pm \ge 0$.
- **Bornes de la pureté :** $P(t) \in \left[\frac{1}{2}, 1\right]$.
- **Concordance analytique :** Vérification point par point entre l'intégration numérique de Runge-Kutta et les formes fermées.
- **Discrétisation :** Cohérence du pas de temps $\Delta t$ avec la fréquence $\omega$ (condition d'échantillonnage $\Delta t \ll \frac{2\pi}{\omega}$).

---

## 7. Statut des énoncés

- **[Construction formelle]** Choix des équations différentielles et des formes paramétriques de $\Gamma(t)$.
- **[Résultat analytique]** Expressions exactes de $\rho_{01}(t)$ et de la pureté $P(t)$.
- **[À vérifier par exécution]** Concordance numérique des scripts déposés avec les solutions analytiques ci-dessus.
- **[Analogie philosophique]** Comparaison formelle entre persistance, reprise et temporalité vécue.
- **[Limite]** Aucun résultat concernant la conscience, l'intentionnalité ou la rétrocausalité n'est établi.

---

## Références de travail

Les références primaires, éditions, pages et sources techniques seront vérifiées et complétées avant la version finale. Cette note ne prétend pas constituer une revue de littérature exhaustive.
