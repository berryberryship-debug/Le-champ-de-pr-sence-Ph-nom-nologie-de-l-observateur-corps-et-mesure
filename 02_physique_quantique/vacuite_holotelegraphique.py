# La simulation numérique de l’ordre implicite

*Document assemblé : texte de la section 3 (inchangé), puis script complet remplacé par les 5 modules corrigés.*

### 3. La simulation numérique de l'ordre implicite
Le script `vacuite_holotelegraphique.py` implémente numériquement cette dynamique. Il résout une équation d'onde complexe, non linéaire, amortie et métriquement auto-gravitante sur une grille périodique (un tore). 
- La métrique \(L_{\text{field}}\) est couplée à la densité d'énergie via la courbure.
- La dérivée covariante introduit un champ de jauge \(A_{\text{torus}}\) (le tore topologique).
- L'équation d'évolution utilise une intégration de Verlet (vitesse de Verlet) pour garantir la stabilité numérique.
Ce script permet de visualiser la sédimentation de l'ordre implicite : les fluctuations initiales s'effondrent progressivement vers un état stationnaire autopoïétique, validant numériquement la boucle A2.

### 3. La simulation numérique de l’ordre implicite

Le script `vacuite_holotelegraphique.py` implémente numériquement cette dynamique.

Il ne prétend pas modéliser directement la conscience.

Il modélise un système d’onde complexe, non linéaire, amorti et métriquement auto-gravitant, évoluant sur une grille périodique assimilable à un tore.

Son objectif est de visualiser une hypothèse : celle d’une **sédimentation de l’ordre implicite**.

Les fluctuations initiales, loin de se dissiper vers le bruit, peuvent se stabiliser progressivement vers une configuration stationnaire et auto-organisée.

Cette section précise ce que le script fait, ce qu’il montre, et surtout ce qu’il ne prétend pas démontrer.

***

#### A. Le cadre de simulation

La simulation repose sur une équation d’évolution de type ondulatoire, complexe, non linéaire et amortie.

Elle peut être schématisée ainsi :

$$
\frac{\partial^2 \psi}{\partial t^2}
=
\mathcal{L}_{\text{field}}[\psi]
-
\gamma \frac{\partial \psi}{\partial t}
+
\mathcal{N}[\psi],
$$

où :

- $$\psi$$ désigne le champ complexe ;
- $$\mathcal{L}_{\text{field}}$$ désigne l’opérateur de propagation, couplé à la métrique ;
- $$\gamma$$ désigne le coefficient d’amortissement ;
- $$\mathcal{N}[\psi]$$ désigne la composante non linéaire.

La non-linéarité est essentielle.

Elle permet que le champ ne se contente pas de se propager.

Il peut interagir avec lui-même.

Il peut amplifier certaines configurations.

Il peut en atténuer d’autres.

Il peut stabiliser des structures.

La simulation ne décrit donc pas une simple diffusion.

Elle décrit une dynamique de sélection.

***

#### B. Le couplage métrique

La métrique $$L_{\text{field}}$$ est couplée à la densité d’énergie via la courbure.

Cette hypothèse peut être formulée ainsi :

$$
G_{\mu\nu}
\sim
T_{\mu\nu}[\psi],
$$

où $$G_{\mu\nu}$$ représente la courbure effective du champ et $$T_{\mu\nu}$$ la densité d’énergie associée au champ.

Dans le modèle, cette relation ne doit pas être comprise comme une identification à la relativité générale.

Elle constitue une analogie structurelle.

L’idée est la suivante :

$$
\boxed{
\text{L’intensité du champ}
\rightarrow
\text{Courbure effective}
\rightarrow
\text{Modification de la propagation}.
}
$$

Le champ ne se propage pas dans un espace neutre.

Il modifie les conditions de sa propre propagation.

Il courbe l’espace dans lequel il évolue.

Il modifie les trajectoires futures.

C’est précisément ce que nous appelons la sédimentation de l’ordre implicite.

***

#### C. Le champ de jauge torique

La dérivée covariante introduit un champ de jauge $$A_{\text{torus}}$$, associé à la topologie du tore.

La dérivée covariante peut être schématisée ainsi :

$$
D_\mu \psi
=
\partial_\mu \psi
+
i A_\mu \psi.
$$

Le champ de jauge $$A_\mu$$ ne décrit pas une force au sens classique.

Il décrit une règle de transport.

Il décrit une manière de comparer les phases, les orientations ou les configurations locales.

Dans le cas d’un tore, cette règle de transport possède une spécificité topologique.

Elle peut produire des effets non triviaux après un tour complet.

$$
\boxed{
\text{Transport sur un tore}
\rightarrow
\text{Holonomie possible}.
}
$$

Cette structure est essentielle pour notre modèle.

Elle permet de penser la mémoire non comme un stockage, mais comme une dépendance au chemin.

Un retour aux mêmes coordonnées ne signifie pas nécessairement un retour au même état relationnel.

***

#### D. L’intégration de Verlet

L’équation d’évolution utilise une intégration de Verlet, plus précisément une forme de vitesse de Verlet.

Cette méthode est choisie pour sa stabilité numérique relative.

Elle est particulièrement adaptée aux systèmes dynamiques où la conservation des structures, des oscillations ou des invariants est importante.[1][2][3]

La méthode de Verlet possède plusieurs propriétés intéressantes.

Elle est d’ordre deux.

Elle est relativement stable.

Elle préserve mieux certaines structures que les méthodes d’Euler simples.[1][3][4]

Mais elle a aussi une limite.

Elle est moins adaptée lorsque l’amortissement dépend explicitement de la vitesse.[5]

Dans notre cas, l’amortissement est présent.

Il faut donc interpréter la stabilité du schéma avec prudence.

La stabilité numérique ne garantit pas la validité physique du modèle.

Elle garantit seulement que la simulation ne diverge pas immédiatement.

***

#### E. Ce que le script montre

Le script permet de visualiser la sédimentation de l’ordre implicite.

Les fluctuations initiales s’effondrent progressivement vers un état stationnaire autopoïétique.

Cette évolution peut être schématisée ainsi :

$$
\boxed{
\text{Fluctuations initiales}
\rightarrow
\text{Couplage non linéaire}
\rightarrow
\text{Sélection}
\rightarrow
\text{Stabilisation}
\rightarrow
\text{État stationnaire}.
}
$$

Ce que le script montre, ce n’est pas une création ex nihilo.

C’est une sélection.

Certaines fluctuations sont amplifiées.

D’autres sont atténuées.

Certaines structures persistent.

D’autres disparaissent.

Le système ne produit pas un ordre à partir du néant.

Il sélectionne un ordre à partir d’un bruit initial.

***

#### F. Ce que le script ne montre pas

Il est essentiel de préciser ce que le script ne montre pas.

Il ne montre pas que la conscience émerge de cette dynamique.

Il ne montre pas que le temps vécu est réductible à une équation d’onde.

Il ne montre pas que la rétention phénoménologique est identique à une mémoire numérique.

Il ne montre pas que l’holonomie est une observable biologique.

Il ne montre pas que l’état stationnaire est une conscience.

Il montre seulement qu’un système dynamique non linéaire, couplé à une métrique et à une topologie, peut produire une stabilisation sélective.

$$
\boxed{
\text{Stabilisation numérique}
\neq
\text{Conscience}.
}
$$

$$
\boxed{
\text{État stationnaire}
\neq
\text{Expérience vécue}.
}
$$

Cette distinction est essentielle.

Elle protège le modèle contre une surinterprétation.

***

#### G. La boucle A2

Le script permet de valider numériquement la boucle A2.

Cette boucle peut être formulée ainsi :

$$
\boxed{
\text{Fluctuation}
\rightarrow
\text{Couplage}
\rightarrow
\text{Courbure}
\rightarrow
\text{Sélection}
\rightarrow
\text{Stabilisation}
\rightarrow
\text{Nouvelle fluctuation}.
}
$$

Cette boucle n’est pas linéaire.

Elle est récursive.

Elle est auto-organisée.

Elle est auto-productrice.

Elle constitue une forme minimale d’autopoïèse.

$$
\boxed{
\text{Boucle A2}
\equiv
\text{Boucle d’auto-production}.
}
$$

Cette boucle ne prétend pas expliquer la vie.

Elle prétend en proposer une analogie structurelle.

***

#### H. L’autopoïèse comme hypothèse

L’autopoïèse désigne, dans la théorie de Maturana et Varela, la capacité d’un système à produire et à maintenir les composants qui produisent le réseau qui les produit.[6][7][8][9][10]

Un système autopoïétique est clos du point de vue de son organisation, mais ouvert du point de vue de ses échanges avec l’environnement.[6][9]

Il ne s’adapte pas simplement à son environnement.

Il co-évolue avec lui.[6]

Dans notre modèle, l’état stationnaire produit par la simulation peut être interprété comme une forme minimale d’autopoïèse.

Il ne s’agit pas d’un organisme vivant.

Il s’agit d’une structure qui se maintient à travers ses propres interactions.

$$
\boxed{
\text{État stationnaire}
\equiv
\text{Forme minimale d’autopoïèse}.
}
$$

Cette interprétation doit rester prudente.

Elle ne prétend pas expliquer la vie.

Elle prétend en proposer une analogie structurelle.

***

#### I. La sédimentation de l’ordre implicite

La sédimentation de l’ordre implicite désigne le processus par lequel les fluctuations initiales se stabilisent progressivement.

Ce processus peut être schématisé ainsi :

$$
\boxed{
\text{Bruit}
\rightarrow
\text{Couplage}
\rightarrow
\text{Sélection}
\rightarrow
\text{Stabilisation}
\rightarrow
\text{Ordre implicite}.
}
$$

Ce processus ne se réduit pas à une simple dissipation.

Il ne se réduit pas non plus à une simple amplification.

Il est une sélection.

Il est une hiérarchisation.

Il est une structuration.

$$
\boxed{
\text{Ordre implicite}
=
\text{Sélection}
+
\text{Hiérarchisation}
+
\text{Structuration}.
}
$$

***

#### J. La correspondance avec la rétention

La sédimentation de l’ordre implicite peut être mise en correspondance avec la rétention phénoménologique.

La rétention ne conserve pas le passé à l’identique.

Elle le transforme.

Elle l’intègre.

Elle le rend pertinent pour le présent.

$$
\boxed{
\text{Rétention}
\widehat{\longrightarrow}
\text{Sédimentation de l’ordre implicite}.
}
$$

Cette correspondance ne signifie pas que la rétention est une équation d’onde.

Elle signifie que les deux phénomènes partagent une structure commune.

Ils partagent une dépendance au chemin.

Ils partagent une mémoire.

Ils partagent une transformation.

***

#### K. La correspondance avec la protention

La sédimentation de l’ordre implicite peut aussi être mise en correspondance avec la protention phénoménologique.

La protention ne prédit pas un contenu précis.

Elle ouvre un champ de possibilités.

Elle oriente la trajectoire.

$$
\boxed{
\text{Protention}
\widehat{\longrightarrow}
\text{Orientation de la trajectoire}.
}
$$

La sédimentation de l’ordre implicite ne prédit pas non plus un contenu précis.

Elle sélectionne un champ de possibilités.

Elle oriente la trajectoire.

$$
\boxed{
\text{Sédimentation}
\widehat{\longrightarrow}
\text{Orientation de la trajectoire}.
}
$$

Cette correspondance ne signifie pas que la protention est une équation d’onde.

Elle signifie que les deux phénomènes partagent une structure commune.

Ils partagent une ouverture.

Ils partagent une orientation.

Ils partagent une sélection.

***

#### L. La clôture de la sous-partie

La simulation numérique de l’ordre implicite ne prétend pas expliquer la conscience.

Elle prétend illustrer une hypothèse.

Elle prétend montrer qu’un système dynamique non linéaire, couplé à une métrique et à une topologie, peut produire une stabilisation sélective.

Elle prétend montrer que le bruit peut devenir ordre.

Elle prétend montrer que la fluctuation peut devenir structure.

Elle prétend montrer que le passage peut devenir mémoire.

$$
\boxed{
\text{Bruit}
\rightarrow
\text{Ordre}.
}
$$

$$
\boxed{
\text{Fluctuation}
\rightarrow
\text{Structure}.
}
$$

$$
\boxed{
\text{Passage}
\rightarrow
\text{Mémoire}.
}
$$

C’est cette hypothèse qui constitue le cœur de la sous-partie.

C’est cette hypothèse qui permet de penser le présent comme une épaisseur.

C’est cette hypothèse qui permet de penser le présent comme une sédimentation.

C’est cette hypothèse qui permet de penser le présent comme un ordre implicite.

Citations :
[1] Verlet Integration - NMM 2023 https://fab.cba.mit.edu/classes/864.23/people/Erik/verlet-integration/
[2] NUMERICAL INTEGRATORS FOR THE https://www.birs.ca/cmo-workshops/2018/18w5202/files/sanzserna.pdf
[3] Verlet integration - Wikipedia https://en.wikipedia.org/wiki/Verlet_integration
[4] Euler and Verlet Integration for Particle Physics https://www.gorillasun.de/blog/euler-and-verlet-integration-for-particle-physics/
[5] vdrift/docs/Numerical_integration.md at master https://github.com/VDrift/vdrift/blob/master/docs/Numerical_integration.md
[6] A Brief Review of Systems Theories and Their Managerial Applications https://pubsonline.informs.org/doi/pdf/10.1287/serv.2.1_2.126
[7] Self-organizing systems: what, how, and why? - npj Complexity http://www.link.springer.com/article/10.1038/s44260-025-00031-5
[8] Autocatalysis, Autopoiesis, and the Opportunity Cost of ... - PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC11201707/
[9] Autopoiesis | Biology | EBSCOhost https://www.ebsco.com/knowledge/biology/autopoiesis/
[10] Autopoiesis: The Organization of Living Systems, Its Characterization and A Model - F. G Varela, H. R. Maturana and R. Uribe https://dn710209.ca.archive.org/0/items/autopoiesis-f.-g-varela-r.-uribe/Autopoiesis%20-%20F.%20G%20Varela,%20R.%20Uribe_text.pdf
[11] Information Measures of Complexity, Emergence, Self-organization, Homeostasis, and Autopoiesis https://arxiv.org/pdf/1304.1842.pdf
[12] arXiv:1405.3153v1  [math.NA]  13 May 2014 https://arxiv.org/pdf/1405.3153v1.pdf
[13] Microsoft Word - CIMMACS-first.doc https://www.ing.ula.ve/~aguilar/publicaciones/objetos/congreso/CIMMACS-10.pdf
[14] CSCC https://www.mdpi.com/2617-8699/3/2/106/pdf
[15] Verlet Integration Physics — Console Simulation https://github.com/77natsu77/verlet-integration


---

# Script complet corrigé et unifié

## 1. Objectif du script

Le script ci-dessous corrige les principales lacunes identifiées dans les prototypes précédents.

Il ne prétend pas démontrer une conscience, une mémoire phénoménologique ou une théorie de jauge biologique.

Il construit un **système hybride minimal**, articulant :

- une dynamique de champ complexe sur un tore, avec jauge U(1) ;
- une phase et une cohérence hilbertienne non triviale ;
- une mémoire dynamique (filtre RLS) ;
- une prédiction ;
- une régulation de précision en boucle fermée ;
- une calibration multidimensionnelle (indépendante du champ) ;
- un suivi de norme, de phase et d’holonomie.

$$
\boxed{
\text{Champ}
\rightarrow
\text{Phase}
\rightarrow
\text{Cohérence}
\rightarrow
\text{Mémoire}
\rightarrow
\text{Prédiction}
\rightarrow
\text{Précision}
\rightarrow
\text{Calibration}.
}
$$

***

## 2. Corrections apportées

| Lacune initiale | Correction apportée |
|---|---|
| Holonomie nulle (A sans composante moyenne) | A = A₀ + A_per, avec A₀ = 2πθ/L imposé ; seul A₀ est physique en 1D |
| Texte et script non alignés | Amortissement γ et couplage de courbure réintroduits (analogie) |
| Densité moyenne constante (= 1/L) | IPR, contraste de densité, moyenne complexe Re/Im |
| Contraste de cohérence ≈ 1 | Phase du miroir π·ρ/ρ_max |
| Précision sans effet sur le champ | Boucle fermée : Pi module g_eff |
| Bruit D fixe | D calculé à partir du champ |
| Calibration déconnectée | Déclarée indépendante du champ, cible déclarée arbitraire |
| Aliasing de l’état initial | Bruit complexe passe-bas |
| Norme triviale en régime dissipatif | `norme_avant_renorm` mesurée avant renormalisation |
| Échelle RLS ambiguë | Initialisation explicite |
| Robustesse | Validation des paramètres, détection de divergence, Newton + dichotomie |
| Absence de validation | `--verifier` : régime unitaire et régime dissipatif |

***

## 3. Script complet : les 5 modules

À placer dans un même dossier. Point d’entrée : `vacuite_holotelegraphique.py`.

```bash
python vacuite_holotelegraphique.py --verifier
python vacuite_holotelegraphique.py --steps 100 --dt 0.01
python vacuite_holotelegraphique.py --gamma 0.5      # régime dissipatif
```

### 3.1 `outils.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
outils.py
=========

Utilitaires : normalisation L2, plancher lisse, rapport de Bessel
kappa(x) = I1(x) / I0(x) et son inverse.
"""

from __future__ import annotations

import numpy as np
from scipy.special import ive

# ============================================================
# 0. CONSTANTES
# ============================================================

EPSILON = 1e-12

# ============================================================
# 1. UTILITAIRES MATHÉMATIQUES
# ============================================================


def normaliser_L2(champ: np.ndarray, dx: float, cible: float = 1.0) -> np.ndarray:
    """Normalise un champ complexe pour que ``∫|ψ|² dx = cible``.

    Raises
    ------
    ValueError
        Si le champ contient des valeurs non finies ou une norme quasi nulle.
    """
    champ = np.asarray(champ)
    if not np.all(np.isfinite(champ)):
        raise ValueError("Champ non fini (NaN ou inf).")
    norme2 = float(np.sum(np.abs(champ) ** 2) * dx)
    if norme2 <= 1e-30:
        raise ValueError("Norme du champ quasi-nulle.")
    return champ * np.sqrt(cible / norme2)


def plancher_lisse(
    valeurs: np.ndarray,
    seuil: float = 0.01,
    largeur: float = 0.01,
) -> np.ndarray:
    """Plancher lisse évitant les valeurs nulles ou négatives."""
    return seuil + largeur * np.logaddexp((valeurs - seuil) / largeur, 0.0)


def kappa_bessel(x):
    """Rapport de concentration circulaire ``kappa(x) = I1(x) / I0(x)``."""
    x = np.maximum(x, 1e-12)
    return ive(1, x) / np.maximum(ive(0, x), 1e-300)


def inverser_kappa_newton(
    target: float,
    tol: float = 1e-10,
    max_iter: int = 50,
) -> float:
    """Résout ``kappa(x) = target`` par Newton, avec repli par dichotomie.

    La dérivée exacte est ``dkappa/dx = 1 - k/x - k²``. Kappa étant
    strictement croissante, la dichotomie sert de filet de sécurité si
    Newton ne converge pas.
    """
    target = float(np.clip(target, 1e-6, 0.999))
    x = 1.0
    for _ in range(max_iter):
        k = float(kappa_bessel(x))
        diff = k - target
        if abs(diff) < tol:
            return float(x)
        dk = max(1.0 - k / x - k * k, 1e-10)
        x = max(x - diff / dk, 1e-8)

    bas, haut = 1e-9, 1e4
    for _ in range(200):
        milieu = 0.5 * (bas + haut)
        if float(kappa_bessel(milieu)) < target:
            bas = milieu
        else:
            haut = milieu
    return float(0.5 * (bas + haut))
```

### 3.2 `champ.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
champ.py
========

Champ complexe sur un tore, jauge U(1), Strang splitting, cohérence
hilbertienne.

Équation (régime unitaire, gamma = 0) ::

    i ∂ψ/∂t = -½ D²ψ + g_eff |ψ|²ψ + V(x)ψ + V_courbure[ρ]ψ ,  D = ∂x - iA(x)

Régime dissipatif (gamma > 0) : ``i ∂ψ/∂t = (1 - iγ) H ψ`` avec
renormalisation L2.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.fft import fft, fftfreq, ifft

from outils import normaliser_L2

# ============================================================
# 2. DYNAMIQUE DU CHAMP
# ============================================================


@dataclass
class DynamiqueJaugeCovarianteExacte:
    """Dynamique spectrale d'un champ complexe sur un tore avec jauge U(1).

    La jauge est décomposée en ``A = A_0 + A_per`` : ``A_0 = 2πθ/L`` porte
    l'holonomie (seule physique, modulo 2π en flux) et ``A_per`` est de
    jauge pure en 1D.
    """

    resolution: int = 1024
    etendue_spatiale: float = 50.0
    p: int = 2
    q: int = 3
    flux_theta: float = 0.37  # flux en quanta (physique mod 1)
    lambda_jauge: float = 2.0
    amplitude_jauge: float = 0.1  # amplitude de A_per
    k_coupure_init: float = 2.0  # bande passante de l'état initial
    g_kerr: float = 1.0
    alpha_pot: float = 0.1
    gamma: float = 0.0  # 0 = unitaire ; > 0 = relaxation
    # densité -> potentiel ; instable si trop grand avec gamma > 0
    # (0,5 stable, 5 diverge dans nos essais)
    coeff_courbure: float = 0.0
    largeur_filtre: float = 0.15
    graine: int = 42

    def __post_init__(self) -> None:
        self._valider()
        self.N = int(self.resolution)
        self.L = float(self.etendue_spatiale)
        self.dx = self.L / self.N
        self.x = np.linspace(-self.L / 2, self.L / 2, self.N, endpoint=False)
        self.k_base = 2.0 * np.pi * fftfreq(self.N, d=self.dx)
        self.g_eff = float(self.g_kerr)

        # Jauge : A = A_0 (holonomie) + A_per (moyenne nulle, de jauge)
        ang_p = 2.0 * np.pi * self.p * self.x / self.L
        ang_q = 2.0 * np.pi * self.q * self.x / self.L
        A_per = (
            self.amplitude_jauge
            * (2.0 * np.pi / self.lambda_jauge)
            * (self.p * np.cos(ang_q) + self.q * np.sin(ang_p))
        )
        A_per -= np.mean(A_per)
        self.A_0 = 2.0 * np.pi * self.flux_theta / self.L
        self.A = self.A_0 + A_per
        self.flux_jauge = self.A_0 * self.L  # = 2π θ

        # Phase périodique φ telle que φ' = A_per
        denom = 1j * self.k_base
        denom[0] = 1.0
        phi_k = fft(A_per) / denom
        phi_k[0] = 0.0
        self.phi_jauge = ifft(phi_k).real
        self.phase_gauge_plus = np.exp(1j * self.phi_jauge)
        self.phase_gauge_moins = np.exp(-1j * self.phi_jauge)

        # Grille spectrale tordue : (ik - iA_0) = i(k - A_0)
        self.k_tordu = self.k_base - self.A_0

        # Potentiel scalaire externe
        self.V = self.alpha_pot * np.cos(2.0 * np.pi * self.x / self.L)

        # Champ initial : bruit complexe passe-bas (un bruit blanc sature
        # la grille et provoque de l'aliasing)
        rng = np.random.default_rng(self.graine)
        enveloppe = np.exp(-(self.x**2) / 8.0)
        bruit = rng.normal(size=self.N) + 1j * rng.normal(size=self.N)
        bruit = ifft(fft(bruit) * np.exp(-((self.k_base / self.k_coupure_init) ** 2)))
        self.psi = normaliser_L2(enveloppe * bruit, self.dx)
        self.norme_avant_renorm = self.norme()

    def _valider(self) -> None:
        """Vérifie la cohérence des paramètres."""
        if int(self.resolution) < 8:
            raise ValueError("resolution doit être >= 8.")
        if not self.etendue_spatiale > 0:
            raise ValueError("etendue_spatiale doit être > 0.")
        if self.gamma < 0:
            raise ValueError("gamma doit être >= 0.")
        if self.g_kerr < 0:
            raise ValueError("g_kerr doit être >= 0.")
        if not self.k_coupure_init > 0:
            raise ValueError("k_coupure_init doit être > 0.")
        if self.largeur_filtre < 0:
            raise ValueError("largeur_filtre doit être >= 0.")
        if self.lambda_jauge == 0:
            raise ValueError("lambda_jauge ne doit pas être nul.")

    # -- courbure effective (analogie, pas relativité générale) --
    def courbure(self, rho: np.ndarray) -> np.ndarray:
        """Retourne ``-∂²ρ_lissé`` (analogie structurelle)."""
        k_max = np.max(np.abs(self.k_base))
        filtre = np.exp(-self.largeur_filtre * (np.abs(self.k_base) / k_max) ** 4)
        rho_k = fft(rho) * filtre
        return ifft(self.k_base**2 * rho_k).real

    def potentiel_effectif(self, rho: np.ndarray) -> np.ndarray:
        """Potentiel total : externe + Kerr + courbure effective."""
        v = self.V + self.g_eff * rho
        if self.coeff_courbure != 0.0:
            v = v + self.coeff_courbure * self.courbure(rho)
        return v

    # -- pas élémentaires --------------------------------------
    def pas_potentiel(self, dt_demi: float) -> None:
        """Applique ``exp(-i v dt)`` (unitaire) et l'amortissement éventuel.

        La soustraction de la moyenne de ``v`` dans l'amortissement est un
        choix de modélisation : elle n'ajoute qu'un facteur global, annulé
        par la renormalisation L2.
        """
        v = self.potentiel_effectif(np.abs(self.psi) ** 2)
        self.psi *= np.exp(-1j * v * dt_demi)
        if self.gamma > 0.0:
            expo = np.clip(-self.gamma * (v - np.mean(v)) * dt_demi, -30.0, 30.0)
            self.psi *= np.exp(expo)

    def pas_cinetique_tordu(self, dt: float) -> None:
        """Pas cinétique covariant exact (jauge + FFT tordue + retour)."""
        chi = self.psi * self.phase_gauge_moins
        chi_k = fft(chi) * np.exp(-0.5 * (1j + self.gamma) * self.k_tordu**2 * dt)
        self.psi = ifft(chi_k) * self.phase_gauge_plus

    def pas_strang(self, dt: float) -> np.ndarray:
        """Un pas de Strang splitting ``e^{-iVdt/2} e^{-iTdt} e^{-iVdt/2}``.

        Raises
        ------
        ValueError
            Si ``dt`` n'est pas un réel fini strictement positif.
        FloatingPointError
            Si le champ devient non fini (divergence numérique).
        """
        if not (np.isfinite(dt) and dt > 0):
            raise ValueError("dt doit être un réel fini > 0.")
        self.pas_potentiel(0.5 * dt)
        self.pas_cinetique_tordu(dt)
        self.pas_potentiel(0.5 * dt)
        if not np.all(np.isfinite(self.psi)):
            raise FloatingPointError("Divergence numérique : champ non fini.")
        # Norme mesurée AVANT renormalisation : en régime dissipatif elle
        # reflète la perte réelle ; après renormalisation elle vaut 1.
        self.norme_avant_renorm = self.norme()
        if self.gamma > 0.0:
            self.psi = normaliser_L2(self.psi, self.dx)
        return self.psi

    # -- observables -------------------------------------------
    def densite(self) -> np.ndarray:
        """Densité ``|ψ|²``."""
        return np.abs(self.psi) ** 2

    def norme(self) -> float:
        """Norme L2 discrète."""
        return float(np.sum(self.densite()) * self.dx)

    def ipr(self) -> float:
        """``∫ρ² / (∫ρ)²`` : inverse de l'étendue effective."""
        rho = self.densite()
        total = float(np.sum(rho) * self.dx)
        return float(np.sum(rho**2) * self.dx / max(total**2, 1e-30))

    def contraste_densite(self) -> float:
        """Variance normalisée de la densité."""
        rho = self.densite()
        return float(np.var(rho) / max(np.mean(rho) ** 2, 1e-30))

    def moyenne_complexe(self) -> complex:
        """``m = (1/√L) ∫ψ dx`` ; ``|m| <= 1`` (évite le saut de ±π)."""
        return complex(np.sum(self.psi) * self.dx / np.sqrt(self.L))

    def phase_moyenne(self) -> float:
        """Phase de la moyenne complexe (peut sauter de ±π)."""
        return float(np.angle(np.sum(self.psi) * self.dx))

    def variance_phase(self) -> float:
        """Variance de la phase locale (sensible au repliement ±π)."""
        return float(np.var(np.angle(self.psi)))

    def holonomie_boucle(self) -> float:
        """Flux de jauge ``2πθ`` sur le tore (rad)."""
        return self.flux_jauge

    def holonomie_mod_2pi(self) -> float:
        """Flux de jauge réduit modulo 2π (grandeur physique)."""
        return float(np.mod(self.flux_jauge, 2.0 * np.pi))

    def energie_covariante(self) -> float:
        """``E = ∫[½|Dψ|² + (g/2)ρ² + Vρ + V_c ρ] dx`` (diagnostic)."""
        dpsi = ifft(1j * self.k_base * fft(self.psi)) - 1j * self.A * self.psi
        rho = self.densite()
        dens = 0.5 * np.abs(dpsi) ** 2 + 0.5 * self.g_eff * rho**2 + self.V * rho
        if self.coeff_courbure != 0.0:
            dens = dens + self.coeff_courbure * self.courbure(rho) * rho
        return float(np.sum(dens) * self.dx)


# ============================================================
# 3. COHÉRENCE HILBERTIENNE
# ============================================================


class ContrasteCoherenceHilbertien:
    """Contraste de recouvrement hilbertien (et non interférence physique).

    ``C = |<ψ,ψ_m>|² / (‖ψ‖² ‖ψ_m‖²)`` avec ``ψ_m = ψ·exp(iπ ρ/ρ_max)``.
    """

    @staticmethod
    def mesure(psi: np.ndarray, dx: float) -> float:
        """Retourne ``C`` dans ``[0, 1]``."""
        rho = np.abs(psi) ** 2
        rmax = np.max(rho)
        if rmax <= 1e-30:
            return 0.0
        psi_m = psi * np.exp(1j * np.pi * rho / rmax)
        n1 = np.sum(np.abs(psi) ** 2) * dx
        n2 = np.sum(np.abs(psi_m) ** 2) * dx
        ps = np.sum(np.conj(psi) * psi_m) * dx
        return float(np.abs(ps) ** 2 / (n1 * n2))
```

### 3.3 `controle.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
controle.py
===========

Prédicteur RLS adaptatif et régulateur homéostatique de précision.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np

from outils import inverser_kappa_newton, kappa_bessel

# ============================================================
# 4. PRÉDICTEUR RLS ADAPTATIF
# ============================================================


class PredicteurAdaptatifRLS:
    """Filtre des moindres carrés récursifs (RLS) d'ordre M.

    Ordre des opérations : prédiction -> erreur -> poids -> décalage.
    """

    def __init__(
        self,
        ordre: int = 3,
        lambda_oubli: float = 0.985,
        delta: float = 10.0,
    ) -> None:
        if int(ordre) < 1:
            raise ValueError("ordre doit être >= 1.")
        if not 0.0 < lambda_oubli <= 1.0:
            raise ValueError("lambda_oubli doit être dans ]0, 1].")
        self.ordre = int(ordre)
        self.lam = float(lambda_oubli)
        self.w = np.zeros(self.ordre)
        self.P = np.eye(self.ordre) * float(delta)
        self.tampon = np.zeros(self.ordre)
        self.echelle = 0.0  # moyenne glissante de |valeur|

    def predire(self) -> float:
        """Prédiction courante."""
        return float(np.dot(self.w, self.tampon))

    def actualiser(self, valeur: float) -> float:
        """Met à jour le filtre ; retourne l'erreur RELATIVE.

        Raises
        ------
        ValueError
            Si ``valeur`` n'est pas finie.
        """
        valeur = float(valeur)
        if not np.isfinite(valeur):
            raise ValueError("Observation non finie.")
        x = self.tampon.copy()
        erreur = float(valeur - np.dot(self.w, x))
        Px = self.P @ x
        g = Px / max(self.lam + float(np.dot(x, Px)), 1e-12)
        self.w += g * erreur
        self.P = (self.P - np.outer(g, Px)) / self.lam
        self.tampon = np.roll(self.tampon, 1)
        self.tampon[0] = valeur
        if self.echelle == 0.0:
            self.echelle = abs(valeur)
        else:
            self.echelle = 0.9 * self.echelle + 0.1 * abs(valeur)
        return abs(erreur) / max(self.echelle, 1e-9)


# ============================================================
# 5. RÉGULATEUR DE PRÉCISION
# ============================================================


@dataclass
class RegulateurPrecisionRobuste:
    """Régulateur homéostatique de précision de type PI."""

    target_kappa: float = 0.85
    kp: float = 0.35
    ki: float = 0.03
    integrale: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 < self.target_kappa < 1.0:
            raise ValueError("target_kappa doit être dans ]0, 1[.")
        self.x_consigne = inverser_kappa_newton(self.target_kappa)

    def corriger(
        self,
        Pi: float,
        D: float,
        K: float,
        incertitude: float,
    ) -> Dict[str, float]:
        """Met à jour la précision selon bruit ``D``, couplage ``K`` et incertitude."""
        D = max(float(D), 1e-6)
        K = max(float(K), 1e-6)
        incertitude = float(np.nan_to_num(incertitude, nan=0.0, posinf=5.0))
        consigne = (self.x_consigne * D / K) * (1.0 + incertitude)
        erreur = consigne - Pi
        self.integrale = float(np.clip(self.integrale + erreur, -5.0, 5.0))
        Pi_new = float(
            np.clip(Pi + self.kp * erreur + self.ki * self.integrale, 0.01, 20.0)
        )
        x_eff = Pi_new * K / D
        k_mes = float(kappa_bessel(x_eff))
        return {
            "Pi": Pi_new,
            "x": x_eff,
            "kappa": k_mes,
            "erreur_kappa": self.target_kappa - k_mes,
        }
```

### 3.4 `calibration.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calibration.py
==============

Calibration dimensionnelle multidimensionnelle, INDÉPENDANTE du champ simulé.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

import numpy as np
import pandas as pd

# ============================================================
# 6. CALIBRATION MULTIDIMENSIONNELLE
# ============================================================

LIGHT_SPEED = 3.0e8  # m/s, référence de calibration uniquement


@dataclass
class CalibrationMultidimensionnelle:
    """Exercice d'analyse dimensionnelle, NON couplé au champ.

    La cible ``[800, 1200]`` m est arbitraire (non justifiée).
    """

    omega_scales: np.ndarray = field(default_factory=lambda: np.logspace(-5, 2, 30))
    gamma_scales: np.ndarray = field(default_factory=lambda: np.logspace(-2, 1, 15))
    spatial_scales: np.ndarray = field(default_factory=lambda: np.logspace(-2, 3, 15))
    cible_min: float = 800.0
    cible_max: float = 1200.0

    def __post_init__(self) -> None:
        if self.cible_min > self.cible_max:
            raise ValueError("cible_min doit être <= cible_max.")

    def evaluer_longueur_onde(
        self,
        omega_scale: float,
        gamma_scale: float,
        spatial_scale: float,
    ) -> float:
        """Longueur d'onde effective (m), ``nan`` si sur-amorti."""
        omega_0 = 1.0e6 * omega_scale
        gamma = 1.2 * gamma_scale
        disc = omega_0**2 - (gamma / 2) ** 2
        if disc <= 0:
            return float("nan")
        return (2.0 * np.pi * LIGHT_SPEED / np.sqrt(disc)) * spatial_scale

    def executer_balayage(self) -> pd.DataFrame:
        """Balayage complet ; retourne un ``DataFrame``."""
        lignes: List[Dict[str, float | bool]] = []
        for o in self.omega_scales:
            for g in self.gamma_scales:
                for s in self.spatial_scales:
                    lam = self.evaluer_longueur_onde(o, g, s)
                    lignes.append(
                        {
                            "omega_scale": o,
                            "gamma_scale": g,
                            "spatial_scale": s,
                            "lambda_m": lam,
                            "dans_cible": self.cible_min <= lam <= self.cible_max,
                        }
                    )
        return pd.DataFrame(lignes)
```

### 3.5 `vacuite_holotelegraphique.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vacuite_holotelegraphique.py
============================

Système hybride en boucle fermée, vérification des invariants et CLI.

Architecture ::

    Champ -> Phase -> Cohérence -> Mémoire -> Prédiction -> Précision -> Calibration

Statut : prototype conceptuel. Aucune prétention à modéliser la conscience,
une mémoire phénoménologique, une holonomie biologique ou une autopoïèse
réelle. Prototype != démonstration ; simulation != explication.

Exemples ::

    python vacuite_holotelegraphique.py --steps 100 --dt 0.01
    python vacuite_holotelegraphique.py --gamma 0.5          # relaxation
    python vacuite_holotelegraphique.py --verifier
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from calibration import CalibrationMultidimensionnelle
from champ import ContrasteCoherenceHilbertien, DynamiqueJaugeCovarianteExacte
from controle import PredicteurAdaptatifRLS, RegulateurPrecisionRobuste

# ============================================================
# 7. SYSTÈME HYBRIDE (BOUCLE FERMÉE)
# ============================================================


@dataclass
class SystemeHybrideUnifie:
    """Boucle : champ -> observables -> prédiction -> Pi -> g_eff -> champ.

    La loi ``g_eff = g (1 + β (Pi/Pi_ref - 1))`` est un CHOIX DE
    CONCEPTION, non dérivé d'une théorie.
    """

    champ: DynamiqueJaugeCovarianteExacte = field(
        default_factory=DynamiqueJaugeCovarianteExacte
    )
    rls_ipr: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    rls_re: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    rls_im: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    regulateur: RegulateurPrecisionRobuste = field(
        default_factory=RegulateurPrecisionRobuste
    )
    retroaction: float = 0.2
    Pi: float = 1.0
    Pi_ref: float = 1.0
    K: float = 1.2

    def pas_temporel(self, dt: float = 0.01) -> Dict[str, float]:
        """Exécute un pas complet et retourne les observables."""
        c = self.champ
        c.g_eff = max(
            0.0,
            c.g_kerr * (1.0 + self.retroaction * (self.Pi / self.Pi_ref - 1.0)),
        )
        psi = c.pas_strang(dt)

        ipr = c.ipr()
        m = c.moyenne_complexe()
        contraste = ContrasteCoherenceHilbertien.mesure(psi, c.dx)
        cd = c.contraste_densite()

        # Bruit D calculé à partir du champ, borné dans [0.1, 2)
        D = 0.1 + 1.9 * cd / (1.0 + cd)

        err = (
            self.rls_ipr.actualiser(ipr)
            + self.rls_re.actualiser(m.real)
            + self.rls_im.actualiser(m.imag)
        ) / 3.0
        err = float(np.clip(err, 0.0, 5.0))

        K_dyn = self.K * (1.0 + 0.05 * contraste)
        reg = self.regulateur.corriger(self.Pi, D, K_dyn, err)
        self.Pi = reg["Pi"]

        return {
            "norme_L2": c.norme(),
            "norme_avant_renorm": c.norme_avant_renorm,
            "energie_covariante": c.energie_covariante(),
            "ipr": ipr,
            "contraste_densite": cd,
            "m_re": m.real,
            "m_im": m.imag,
            "phase": c.phase_moyenne(),
            "variance_phase": c.variance_phase(),
            "contraste_coherence": contraste,
            "erreur_pred_rel": err,
            "D": D,
            "Pi": self.Pi,
            "g_eff": c.g_eff,
            "kappa": reg["kappa"],
            "holonomie": c.holonomie_boucle(),
            "holonomie_mod_2pi": c.holonomie_mod_2pi(),
        }


# ============================================================
# 8. VÉRIFICATION DES INVARIANTS
# ============================================================


def verifier_invariants(
    resolution: int = 512,
    steps: int = 200,
    dt: float = 0.005,
) -> bool:
    """Régime unitaire, boucle ouverte : norme et énergie conservées, flux non nul."""
    ch = DynamiqueJaugeCovarianteExacte(resolution=resolution, gamma=0.0)
    E0 = ch.energie_covariante()
    N0 = ch.norme()
    for _ in range(steps):
        ch.pas_strang(dt)
    dN = abs(ch.norme() - N0)
    dE = abs(ch.energie_covariante() - E0) / max(abs(E0), 1e-30)
    ok = dN < 1e-10 and ch.flux_jauge != 0.0 and dE < 1e-2
    print(
        f"[VERIF] unitaire   |ΔNorme| = {dN:.2e} | ΔE/E = {dE:.2e} | "
        f"flux = {ch.flux_jauge:.6f} rad -> {'OK' if ok else 'ÉCHEC'}"
    )
    return ok


def verifier_relaxation(
    resolution: int = 256,
    steps: int = 150,
    dt: float = 0.01,
    gamma: float = 0.5,
) -> bool:
    """Régime dissipatif : l'énergie doit décroître, le champ rester fini."""
    ch = DynamiqueJaugeCovarianteExacte(resolution=resolution, gamma=gamma)
    E0 = ch.energie_covariante()
    for _ in range(steps):
        ch.pas_strang(dt)
    E1 = ch.energie_covariante()
    ok = bool(np.isfinite(E1)) and E1 < E0
    print(
        f"[VERIF] dissipatif E0 = {E0:.5f} -> E1 = {E1:.5f} "
        f"| perte de norme/pas = {1.0 - ch.norme_avant_renorm:.2e} "
        f"-> {'OK' if ok else 'ÉCHEC'}"
    )
    return ok


# ============================================================
# 9. EXÉCUTION
# ============================================================


def executer_simulation(
    steps: int = 100,
    dt: float = 0.01,
    champ: Optional[DynamiqueJaugeCovarianteExacte] = None,
    retroaction: float = 0.2,
) -> List[Dict[str, float]]:
    """Exécute une simulation complète et retourne l'historique."""
    if steps <= 0:
        raise ValueError("steps doit être > 0.")
    systeme = SystemeHybrideUnifie(
        champ=champ if champ is not None else DynamiqueJaugeCovarianteExacte(),
        retroaction=retroaction,
    )
    return [systeme.pas_temporel(dt) for _ in range(steps)]


def construire_parser() -> argparse.ArgumentParser:
    """Construit le parseur d'arguments en ligne de commande."""
    p = argparse.ArgumentParser(description="Système hybride covariant à boucle fermée.")
    p.add_argument("--steps", type=int, default=None, help="Pas (défaut 100 ; 200 en --verifier).")
    p.add_argument("--dt", type=float, default=None, help="Pas de temps (défaut 0.01 ; 0.005 en --verifier).")
    p.add_argument("--resolution", type=int, default=None, help="Points de grille (défaut 1024 ; 512 en --verifier).")
    p.add_argument("--flux", type=float, default=0.37, help="Flux θ en quanta.")
    p.add_argument("--gamma", type=float, default=0.0, help="Amortissement (0 = unitaire).")
    p.add_argument("--courbure", type=float, default=0.0, help="Couplage densité -> potentiel.")
    p.add_argument("--retroaction", type=float, default=0.2, help="β : Pi -> g_eff (0 = boucle ouverte).")
    p.add_argument("--g", type=float, default=1.0, help="Couplage Kerr g.")
    p.add_argument("--graine", type=int, default=42, help="Graine aléatoire.")
    p.add_argument("--csv", type=str, default=None, help="Écrit l'historique dans ce fichier CSV.")
    p.add_argument("--calibration", action="store_true")
    p.add_argument("--verifier", action="store_true")
    p.add_argument("--json", action="store_true")
    return p


def _valider_args(args: argparse.Namespace) -> Optional[str]:
    """Retourne un message d'erreur, ou ``None`` si les arguments sont valides."""
    if args.steps <= 0:
        return "--steps doit être > 0."
    if not (np.isfinite(args.dt) and args.dt > 0):
        return "--dt doit être un réel fini > 0."
    if args.resolution < 8:
        return "--resolution doit être >= 8."
    if args.gamma < 0:
        return "--gamma doit être >= 0."
    if args.g < 0:
        return "--g doit être >= 0."
    if args.retroaction < 0:
        return "--retroaction doit être >= 0."
    return None


def main() -> int:
    """Point d'entrée principal."""
    args = construire_parser().parse_args()

    # Défauts dépendant du mode
    defauts = (200, 0.005, 512) if args.verifier else (100, 0.01, 1024)
    args.steps = defauts[0] if args.steps is None else args.steps
    args.dt = defauts[1] if args.dt is None else args.dt
    args.resolution = defauts[2] if args.resolution is None else args.resolution

    erreur = _valider_args(args)
    if erreur:
        print(f"[!] {erreur}")
        return 1

    if args.verifier:
        ok1 = verifier_invariants(args.resolution, args.steps, args.dt)
        ok2 = verifier_relaxation()
        return 0 if (ok1 and ok2) else 1

    if args.calibration:
        cal = CalibrationMultidimensionnelle()
        df = cal.executer_balayage()
        cible = df[df["dans_cible"]]
        print(
            cible.head(10)
            if not cible.empty
            else f"[!] Aucune configuration dans [{cal.cible_min}, {cal.cible_max}] m."
        )
        return 0

    try:
        champ = DynamiqueJaugeCovarianteExacte(
            resolution=args.resolution,
            flux_theta=args.flux,
            gamma=args.gamma,
            coeff_courbure=args.courbure,
            g_kerr=args.g,
            graine=args.graine,
        )
        systeme = SystemeHybrideUnifie(champ=champ, retroaction=args.retroaction)
    except ValueError as exc:
        print(f"[!] Paramètre invalide : {exc}")
        return 1

    print(
        f"[INIT] {args.steps} pas, dt={args.dt}, N={args.resolution}, "
        f"θ={args.flux}, γ={args.gamma}, β={args.retroaction}"
    )

    historique: List[Dict[str, float]] = []
    try:
        for i in range(args.steps):
            etat = systeme.pas_temporel(args.dt)
            historique.append(etat)
            if (i + 1) % 20 == 0:
                print(
                    f"  Pas {i + 1:04d} | N={etat['norme_L2']:.10f} | "
                    f"E={etat['energie_covariante']:.5f} | IPR={etat['ipr']:.5f} | "
                    f"C={etat['contraste_coherence']:.4f} | Pi={etat['Pi']:.4f} | "
                    f"κ={etat['kappa']:.4f} | err={etat['erreur_pred_rel']:.3e}"
                )
    except (FloatingPointError, ValueError) as exc:
        print(f"[!] Simulation interrompue au pas {len(historique) + 1} : {exc}")
        return 2

    dernier = historique[-1]
    print("\n[BILAN FINAL]")
    for cle, val in dernier.items():
        print(f"  {cle:20s}: {val:14.8f}")
    if args.json:
        print(json.dumps(dernier, indent=2, ensure_ascii=False))
    if args.csv:
        pd.DataFrame(historique).to_csv(args.csv, index=False)
        print(f"[CSV] Historique écrit dans {args.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

***

## 4. Ce que le script ne prétend pas

Le script ne prétend pas :

- démontrer l’émergence de la conscience ;
- démontrer l’existence d’une mémoire phénoménologique ;
- démontrer une holonomie biologique ;
- démontrer une théorie de jauge de la conscience ;
- démontrer une autopoïèse réelle ;
- démontrer une physique quantique de l’esprit.

Il prétend seulement construire un prototype cohérent.

$$
\boxed{
\text{Prototype}
\neq
\text{Démonstration}.
}
$$

$$
\boxed{
\text{Simulation}
\neq
\text{Explication}.
}
$$

$$
\boxed{
\text{Stabilisation numérique}
\neq
\text{Expérience vécue}.
}
$$

***

## 5. Points de robustesse

- Le schéma de Strang applique chaque sous-flux par une exponentielle exacte : en régime unitaire (γ = 0), la norme L² est conservée à la précision machine (|ΔN| ≈ 4·10⁻¹⁴ sur 200 pas, N = 512).
- La grille spectrale tordue `k − A₀` implémente (ik − iA₀) ; la composante périodique de A est absorbée par une transformation de jauge.
- L’holonomie est non nulle : flux 2πθ = 2,3248 rad pour θ = 0,37, réduit modulo 2π.
- L’énergie covariante est un diagnostic, conservée à 6·10⁻⁷ près (ΔE/E, 200 pas, N = 512), sans être annoncée comme exactement conservée.
- Le contraste de cohérence hilbertien est distingué de l’interférence physique.
- Le filtre RLS applique l’ordre prédiction → erreur → mise à jour → décalage.
- Les paramètres sont validés ; une divergence numérique est détectée et signalée (code de retour 2).
- Le script est exécutable en ligne de commande : `--steps`, `--dt`, `--resolution`, `--flux`, `--gamma`, `--courbure`, `--retroaction`, `--g`, `--graine`, `--csv`, `--calibration`, `--verifier`, `--json`.

***

## 6. Limites explicites

Ce module ne prétend pas :

- démontrer l’émergence de la conscience ;
- démontrer l’existence d’une mémoire phénoménologique ;
- démontrer une holonomie biologique ;
- démontrer une théorie de jauge de la conscience ;
- démontrer une autopoïèse réelle ;
- démontrer une physique quantique de l’esprit.

Il construit un prototype cohérent, testable et non surinterprété.

C’est cette clarté qui constitue la robustesse du module.

***

## 7. La clôture

Le script complet corrige les principales lacunes identifiées.

Il articule champ, phase, mémoire, prédiction, précision et calibration.

Il construit une architecture unifiée.

Cette architecture ne prétend pas expliquer la conscience.

Elle propose une analogie structurelle.

Elle propose une manière de penser la mémoire non comme un stockage, mais comme une dépendance au chemin.

Elle propose une manière de penser le présent non comme un point, mais comme une épaisseur.

Elle propose une manière de penser l’ordre implicite non comme une substance, mais comme une dynamique.

$$
\boxed{
\text{Bruit}
\rightarrow
\text{Ordre}.
}
$$

$$
\boxed{
\text{Fluctuation}
\rightarrow
\text{Structure}.
}
$$

$$
\boxed{
\text{Passage}
\rightarrow
\text{Mémoire}.
}
$$

C’est cette architecture qui constitue le cœur du modèle.

C’est cette architecture qui permet de penser l’observateur comme une structure vivante, incarnée, historiquement couplée, normativement orientée et relationnellement stabilisée.

***

## Annexe : notes de concordance entre le texte (section 3) et les scripts

*Cette annexe est ajoutée ; elle est séparable du reste du document. Elle signale où le texte de la section 3, laissé intact, décrit autre chose que ce que font les 5 modules.*

| Section | Le texte dit | Les 5 modules font |
|---|---|---|
| A | Équation d’onde du second ordre en temps, amortie | Équation de type Schrödinger non linéaire (premier ordre en temps). Variante dissipative : i∂ₜψ = (1 − iγ)Hψ, avec renormalisation L² |
| B | Métrique couplée à la densité d’énergie | Potentiel effectif −∂²ρ_lissé (option `--courbure`, nulle par défaut) : une analogie, pas une métrique |
| C | D = ∂ + iA | D = ∂ − iA (convention de signe) ; A = A₀ + A_per |
| D | Intégration de Verlet ; réf. [1]–[5] | Strang splitting spectral. Les réf. [1]–[5] portent sur Verlet, pas sur le schéma actuel |
| E, G | Convergence vers un état stationnaire ; « validation » de la boucle A2 | Voir mesures ci-dessous : non démontré |
| G | Boucle A2 : fluctuation → … → nouvelle fluctuation | Boucle implémentée : champ → observables → prédiction → Pi → g_eff → champ. Ce n’est pas la boucle A2 |
| H | État stationnaire ≡ forme minimale d’autopoïèse | Le modèle ne produit pas ses propres composants : analogie seulement |

**Mesures (régime dissipatif, γ = 0,5, N = 256, dt = 0,01, graine 42, une seule exécution)**

| Pas | Énergie covariante | IPR | Contraste de densité |
|---|---|---|---|
| 1 | 1,502 | 0,2975 | 13,88 |
| 100 | 0,726 | 0,1533 | 6,67 |
| 500 | 0,290 | 0,0891 | 3,46 |
| 1000 | 0,201 | 0,0623 | 2,12 |
| 2000 | 0,154 | 0,0382 | 0,91 |
| 4000 | 0,123 | 0,0229 | 0,146 |

L’énergie décroît de façon monotone et la densité tend vers l’uniformité (IPR → 1/L = 0,02). Au pas 4000, l’énergie n’a pas atteint de plateau, et le mode de Fourier dominant (k ≈ −0,503) ne porte que 16 % du poids spectral : **un état stationnaire n’est pas démontré par ces essais.**

**Références (citées de mémoire, non revérifiées en ligne dans cette session)**

- Strang, G. (1968), « On the construction and comparison of difference schemes », *SIAM Journal on Numerical Analysis*, 5(3), 506–517.
- Varela, F. G., Maturana, H. R., Uribe, R. (1974), « Autopoiesis: the organization of living systems, its characterization and a model », *BioSystems*, 5(4), 187–196.
- Aharonov, Y., Bohm, D. (1959), « Significance of electromagnetic potentials in the quantum theory », *Physical Review*, 115(3), 485–491.

**La FORMULE et le mode CONFIGURATION** (fiche de préférences) : leur mise en correspondance avec les variables du code n’est pas établie. *Je ne sais pas.*
    
Voici la correction de vacuite_holotelegraphique.py en 5 fichiers

    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vacuite_holotelegraphique_unifie.py
===================================

Version à fichier unique des 5 modules : outils, champ, controle,
calibration, système + CLI.

Architecture ::

    Champ -> Phase -> Cohérence -> Mémoire -> Prédiction -> Précision -> Calibration

Équation (régime unitaire, gamma = 0) ::

    i ∂ψ/∂t = -½ D²ψ + g_eff |ψ|²ψ + V(x)ψ + V_courbure[ρ]ψ ,  D = ∂x - iA(x)

Régime dissipatif (gamma > 0) : ``i ∂ψ/∂t = (1 - iγ) H ψ`` + renormalisation L2.

Statut : prototype conceptuel. Aucune prétention à modéliser la conscience,
une mémoire phénoménologique, une holonomie biologique ou une autopoïèse
réelle. Prototype != démonstration ; simulation != explication.

Usage ::

    python vacuite_holotelegraphique_unifie.py --steps 100 --dt 0.01
    python vacuite_holotelegraphique_unifie.py --verifier
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
from numpy.fft import fft, fftfreq, ifft
from scipy.special import ive

# ============================================================
# 0. CONSTANTES
# ============================================================

EPSILON = 1e-12

# ============================================================
# 1. UTILITAIRES MATHÉMATIQUES
# ============================================================


def normaliser_L2(champ: np.ndarray, dx: float, cible: float = 1.0) -> np.ndarray:
    """Normalise un champ complexe pour que ``∫|ψ|² dx = cible``.

    Raises
    ------
    ValueError
        Si le champ contient des valeurs non finies ou une norme quasi nulle.
    """
    champ = np.asarray(champ)
    if not np.all(np.isfinite(champ)):
        raise ValueError("Champ non fini (NaN ou inf).")
    norme2 = float(np.sum(np.abs(champ) ** 2) * dx)
    if norme2 <= 1e-30:
        raise ValueError("Norme du champ quasi-nulle.")
    return champ * np.sqrt(cible / norme2)


def plancher_lisse(
    valeurs: np.ndarray,
    seuil: float = 0.01,
    largeur: float = 0.01,
) -> np.ndarray:
    """Plancher lisse évitant les valeurs nulles ou négatives."""
    return seuil + largeur * np.logaddexp((valeurs - seuil) / largeur, 0.0)


def kappa_bessel(x):
    """Rapport de concentration circulaire ``kappa(x) = I1(x) / I0(x)``."""
    x = np.maximum(x, 1e-12)
    return ive(1, x) / np.maximum(ive(0, x), 1e-300)


def inverser_kappa_newton(
    target: float,
    tol: float = 1e-10,
    max_iter: int = 50,
) -> float:
    """Résout ``kappa(x) = target`` par Newton, avec repli par dichotomie.

    La dérivée exacte est ``dkappa/dx = 1 - k/x - k²``. Kappa étant
    strictement croissante, la dichotomie sert de filet de sécurité si
    Newton ne converge pas.
    """
    target = float(np.clip(target, 1e-6, 0.999))
    x = 1.0
    for _ in range(max_iter):
        k = float(kappa_bessel(x))
        diff = k - target
        if abs(diff) < tol:
            return float(x)
        dk = max(1.0 - k / x - k * k, 1e-10)
        x = max(x - diff / dk, 1e-8)

    bas, haut = 1e-9, 1e4
    for _ in range(200):
        milieu = 0.5 * (bas + haut)
        if float(kappa_bessel(milieu)) < target:
            bas = milieu
        else:
            haut = milieu
    return float(0.5 * (bas + haut))


# ============================================================
# 2. DYNAMIQUE DU CHAMP
# ============================================================


@dataclass
class DynamiqueJaugeCovarianteExacte:
    """Dynamique spectrale d'un champ complexe sur un tore avec jauge U(1).

    La jauge est décomposée en ``A = A_0 + A_per`` : ``A_0 = 2πθ/L`` porte
    l'holonomie (seule physique, modulo 2π en flux) et ``A_per`` est de
    jauge pure en 1D.
    """

    resolution: int = 1024
    etendue_spatiale: float = 50.0
    p: int = 2
    q: int = 3
    flux_theta: float = 0.37  # flux en quanta (physique mod 1)
    lambda_jauge: float = 2.0
    amplitude_jauge: float = 0.1  # amplitude de A_per
    k_coupure_init: float = 2.0  # bande passante de l'état initial
    g_kerr: float = 1.0
    alpha_pot: float = 0.1
    gamma: float = 0.0  # 0 = unitaire ; > 0 = relaxation
    # densité -> potentiel ; instable si trop grand avec gamma > 0
    # (0,5 stable, 5 diverge dans nos essais)
    coeff_courbure: float = 0.0
    largeur_filtre: float = 0.15
    graine: int = 42

    def __post_init__(self) -> None:
        self._valider()
        self.N = int(self.resolution)
        self.L = float(self.etendue_spatiale)
        self.dx = self.L / self.N
        self.x = np.linspace(-self.L / 2, self.L / 2, self.N, endpoint=False)
        self.k_base = 2.0 * np.pi * fftfreq(self.N, d=self.dx)
        self.g_eff = float(self.g_kerr)

        # Jauge : A = A_0 (holonomie) + A_per (moyenne nulle, de jauge)
        ang_p = 2.0 * np.pi * self.p * self.x / self.L
        ang_q = 2.0 * np.pi * self.q * self.x / self.L
        A_per = (
            self.amplitude_jauge
            * (2.0 * np.pi / self.lambda_jauge)
            * (self.p * np.cos(ang_q) + self.q * np.sin(ang_p))
        )
        A_per -= np.mean(A_per)
        self.A_0 = 2.0 * np.pi * self.flux_theta / self.L
        self.A = self.A_0 + A_per
        self.flux_jauge = self.A_0 * self.L  # = 2π θ

        # Phase périodique φ telle que φ' = A_per
        denom = 1j * self.k_base
        denom[0] = 1.0
        phi_k = fft(A_per) / denom
        phi_k[0] = 0.0
        self.phi_jauge = ifft(phi_k).real
        self.phase_gauge_plus = np.exp(1j * self.phi_jauge)
        self.phase_gauge_moins = np.exp(-1j * self.phi_jauge)

        # Grille spectrale tordue : (ik - iA_0) = i(k - A_0)
        self.k_tordu = self.k_base - self.A_0

        # Potentiel scalaire externe
        self.V = self.alpha_pot * np.cos(2.0 * np.pi * self.x / self.L)

        # Champ initial : bruit complexe passe-bas (un bruit blanc sature
        # la grille et provoque de l'aliasing)
        rng = np.random.default_rng(self.graine)
        enveloppe = np.exp(-(self.x**2) / 8.0)
        bruit = rng.normal(size=self.N) + 1j * rng.normal(size=self.N)
        bruit = ifft(fft(bruit) * np.exp(-((self.k_base / self.k_coupure_init) ** 2)))
        self.psi = normaliser_L2(enveloppe * bruit, self.dx)
        self.norme_avant_renorm = self.norme()

    def _valider(self) -> None:
        """Vérifie la cohérence des paramètres."""
        if int(self.resolution) < 8:
            raise ValueError("resolution doit être >= 8.")
        if not self.etendue_spatiale > 0:
            raise ValueError("etendue_spatiale doit être > 0.")
        if self.gamma < 0:
            raise ValueError("gamma doit être >= 0.")
        if self.g_kerr < 0:
            raise ValueError("g_kerr doit être >= 0.")
        if not self.k_coupure_init > 0:
            raise ValueError("k_coupure_init doit être > 0.")
        if self.largeur_filtre < 0:
            raise ValueError("largeur_filtre doit être >= 0.")
        if self.lambda_jauge == 0:
            raise ValueError("lambda_jauge ne doit pas être nul.")

    # -- courbure effective (analogie, pas relativité générale) --
    def courbure(self, rho: np.ndarray) -> np.ndarray:
        """Retourne ``-∂²ρ_lissé`` (analogie structurelle)."""
        k_max = np.max(np.abs(self.k_base))
        filtre = np.exp(-self.largeur_filtre * (np.abs(self.k_base) / k_max) ** 4)
        rho_k = fft(rho) * filtre
        return ifft(self.k_base**2 * rho_k).real

    def potentiel_effectif(self, rho: np.ndarray) -> np.ndarray:
        """Potentiel total : externe + Kerr + courbure effective."""
        v = self.V + self.g_eff * rho
        if self.coeff_courbure != 0.0:
            v = v + self.coeff_courbure * self.courbure(rho)
        return v

    # -- pas élémentaires --------------------------------------
    def pas_potentiel(self, dt_demi: float) -> None:
        """Applique ``exp(-i v dt)`` (unitaire) et l'amortissement éventuel.

        La soustraction de la moyenne de ``v`` dans l'amortissement est un
        choix de modélisation : elle n'ajoute qu'un facteur global, annulé
        par la renormalisation L2.
        """
        v = self.potentiel_effectif(np.abs(self.psi) ** 2)
        self.psi *= np.exp(-1j * v * dt_demi)
        if self.gamma > 0.0:
            expo = np.clip(-self.gamma * (v - np.mean(v)) * dt_demi, -30.0, 30.0)
            self.psi *= np.exp(expo)

    def pas_cinetique_tordu(self, dt: float) -> None:
        """Pas cinétique covariant exact (jauge + FFT tordue + retour)."""
        chi = self.psi * self.phase_gauge_moins
        chi_k = fft(chi) * np.exp(-0.5 * (1j + self.gamma) * self.k_tordu**2 * dt)
        self.psi = ifft(chi_k) * self.phase_gauge_plus

    def pas_strang(self, dt: float) -> np.ndarray:
        """Un pas de Strang splitting ``e^{-iVdt/2} e^{-iTdt} e^{-iVdt/2}``.

        Raises
        ------
        ValueError
            Si ``dt`` n'est pas un réel fini strictement positif.
        FloatingPointError
            Si le champ devient non fini (divergence numérique).
        """
        if not (np.isfinite(dt) and dt > 0):
            raise ValueError("dt doit être un réel fini > 0.")
        self.pas_potentiel(0.5 * dt)
        self.pas_cinetique_tordu(dt)
        self.pas_potentiel(0.5 * dt)
        if not np.all(np.isfinite(self.psi)):
            raise FloatingPointError("Divergence numérique : champ non fini.")
        # Norme mesurée AVANT renormalisation : en régime dissipatif elle
        # reflète la perte réelle ; après renormalisation elle vaut 1.
        self.norme_avant_renorm = self.norme()
        if self.gamma > 0.0:
            self.psi = normaliser_L2(self.psi, self.dx)
        return self.psi

    # -- observables -------------------------------------------
    def densite(self) -> np.ndarray:
        """Densité ``|ψ|²``."""
        return np.abs(self.psi) ** 2

    def norme(self) -> float:
        """Norme L2 discrète."""
        return float(np.sum(self.densite()) * self.dx)

    def ipr(self) -> float:
        """``∫ρ² / (∫ρ)²`` : inverse de l'étendue effective."""
        rho = self.densite()
        total = float(np.sum(rho) * self.dx)
        return float(np.sum(rho**2) * self.dx / max(total**2, 1e-30))

    def contraste_densite(self) -> float:
        """Variance normalisée de la densité."""
        rho = self.densite()
        return float(np.var(rho) / max(np.mean(rho) ** 2, 1e-30))

    def moyenne_complexe(self) -> complex:
        """``m = (1/√L) ∫ψ dx`` ; ``|m| <= 1`` (évite le saut de ±π)."""
        return complex(np.sum(self.psi) * self.dx / np.sqrt(self.L))

    def phase_moyenne(self) -> float:
        """Phase de la moyenne complexe (peut sauter de ±π)."""
        return float(np.angle(np.sum(self.psi) * self.dx))

    def variance_phase(self) -> float:
        """Variance de la phase locale (sensible au repliement ±π)."""
        return float(np.var(np.angle(self.psi)))

    def holonomie_boucle(self) -> float:
        """Flux de jauge ``2πθ`` sur le tore (rad)."""
        return self.flux_jauge

    def holonomie_mod_2pi(self) -> float:
        """Flux de jauge réduit modulo 2π (grandeur physique)."""
        return float(np.mod(self.flux_jauge, 2.0 * np.pi))

    def energie_covariante(self) -> float:
        """``E = ∫[½|Dψ|² + (g/2)ρ² + Vρ + V_c ρ] dx`` (diagnostic)."""
        dpsi = ifft(1j * self.k_base * fft(self.psi)) - 1j * self.A * self.psi
        rho = self.densite()
        dens = 0.5 * np.abs(dpsi) ** 2 + 0.5 * self.g_eff * rho**2 + self.V * rho
        if self.coeff_courbure != 0.0:
            dens = dens + self.coeff_courbure * self.courbure(rho) * rho
        return float(np.sum(dens) * self.dx)


# ============================================================
# 3. COHÉRENCE HILBERTIENNE
# ============================================================


class ContrasteCoherenceHilbertien:
    """Contraste de recouvrement hilbertien (et non interférence physique).

    ``C = |<ψ,ψ_m>|² / (‖ψ‖² ‖ψ_m‖²)`` avec ``ψ_m = ψ·exp(iπ ρ/ρ_max)``.
    """

    @staticmethod
    def mesure(psi: np.ndarray, dx: float) -> float:
        """Retourne ``C`` dans ``[0, 1]``."""
        rho = np.abs(psi) ** 2
        rmax = np.max(rho)
        if rmax <= 1e-30:
            return 0.0
        psi_m = psi * np.exp(1j * np.pi * rho / rmax)
        n1 = np.sum(np.abs(psi) ** 2) * dx
        n2 = np.sum(np.abs(psi_m) ** 2) * dx
        ps = np.sum(np.conj(psi) * psi_m) * dx
        return float(np.abs(ps) ** 2 / (n1 * n2))


# ============================================================
# 4. PRÉDICTEUR RLS ADAPTATIF
# ============================================================


class PredicteurAdaptatifRLS:
    """Filtre des moindres carrés récursifs (RLS) d'ordre M.

    Ordre des opérations : prédiction -> erreur -> poids -> décalage.
    """

    def __init__(
        self,
        ordre: int = 3,
        lambda_oubli: float = 0.985,
        delta: float = 10.0,
    ) -> None:
        if int(ordre) < 1:
            raise ValueError("ordre doit être >= 1.")
        if not 0.0 < lambda_oubli <= 1.0:
            raise ValueError("lambda_oubli doit être dans ]0, 1].")
        self.ordre = int(ordre)
        self.lam = float(lambda_oubli)
        self.w = np.zeros(self.ordre)
        self.P = np.eye(self.ordre) * float(delta)
        self.tampon = np.zeros(self.ordre)
        self.echelle = 0.0  # moyenne glissante de |valeur|

    def predire(self) -> float:
        """Prédiction courante."""
        return float(np.dot(self.w, self.tampon))

    def actualiser(self, valeur: float) -> float:
        """Met à jour le filtre ; retourne l'erreur RELATIVE.

        Raises
        ------
        ValueError
            Si ``valeur`` n'est pas finie.
        """
        valeur = float(valeur)
        if not np.isfinite(valeur):
            raise ValueError("Observation non finie.")
        x = self.tampon.copy()
        erreur = float(valeur - np.dot(self.w, x))
        Px = self.P @ x
        g = Px / max(self.lam + float(np.dot(x, Px)), 1e-12)
        self.w += g * erreur
        self.P = (self.P - np.outer(g, Px)) / self.lam
        self.tampon = np.roll(self.tampon, 1)
        self.tampon[0] = valeur
        if self.echelle == 0.0:
            self.echelle = abs(valeur)
        else:
            self.echelle = 0.9 * self.echelle + 0.1 * abs(valeur)
        return abs(erreur) / max(self.echelle, 1e-9)


# ============================================================
# 5. RÉGULATEUR DE PRÉCISION
# ============================================================


@dataclass
class RegulateurPrecisionRobuste:
    """Régulateur homéostatique de précision de type PI."""

    target_kappa: float = 0.85
    kp: float = 0.35
    ki: float = 0.03
    integrale: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 < self.target_kappa < 1.0:
            raise ValueError("target_kappa doit être dans ]0, 1[.")
        self.x_consigne = inverser_kappa_newton(self.target_kappa)

    def corriger(
        self,
        Pi: float,
        D: float,
        K: float,
        incertitude: float,
    ) -> Dict[str, float]:
        """Met à jour la précision selon bruit ``D``, couplage ``K`` et incertitude."""
        D = max(float(D), 1e-6)
        K = max(float(K), 1e-6)
        incertitude = float(np.nan_to_num(incertitude, nan=0.0, posinf=5.0))
        consigne = (self.x_consigne * D / K) * (1.0 + incertitude)
        erreur = consigne - Pi
        self.integrale = float(np.clip(self.integrale + erreur, -5.0, 5.0))
        Pi_new = float(
            np.clip(Pi + self.kp * erreur + self.ki * self.integrale, 0.01, 20.0)
        )
        x_eff = Pi_new * K / D
        k_mes = float(kappa_bessel(x_eff))
        return {
            "Pi": Pi_new,
            "x": x_eff,
            "kappa": k_mes,
            "erreur_kappa": self.target_kappa - k_mes,
        }


# ============================================================
# 6. CALIBRATION MULTIDIMENSIONNELLE
# ============================================================

LIGHT_SPEED = 3.0e8  # m/s, référence de calibration uniquement


@dataclass
class CalibrationMultidimensionnelle:
    """Exercice d'analyse dimensionnelle, NON couplé au champ.

    La cible ``[800, 1200]`` m est arbitraire (non justifiée).
    """

    omega_scales: np.ndarray = field(default_factory=lambda: np.logspace(-5, 2, 30))
    gamma_scales: np.ndarray = field(default_factory=lambda: np.logspace(-2, 1, 15))
    spatial_scales: np.ndarray = field(default_factory=lambda: np.logspace(-2, 3, 15))
    cible_min: float = 800.0
    cible_max: float = 1200.0

    def __post_init__(self) -> None:
        if self.cible_min > self.cible_max:
            raise ValueError("cible_min doit être <= cible_max.")

    def evaluer_longueur_onde(
        self,
        omega_scale: float,
        gamma_scale: float,
        spatial_scale: float,
    ) -> float:
        """Longueur d'onde effective (m), ``nan`` si sur-amorti."""
        omega_0 = 1.0e6 * omega_scale
        gamma = 1.2 * gamma_scale
        disc = omega_0**2 - (gamma / 2) ** 2
        if disc <= 0:
            return float("nan")
        return (2.0 * np.pi * LIGHT_SPEED / np.sqrt(disc)) * spatial_scale

    def executer_balayage(self) -> pd.DataFrame:
        """Balayage complet ; retourne un ``DataFrame``."""
        lignes: List[Dict[str, float | bool]] = []
        for o in self.omega_scales:
            for g in self.gamma_scales:
                for s in self.spatial_scales:
                    lam = self.evaluer_longueur_onde(o, g, s)
                    lignes.append(
                        {
                            "omega_scale": o,
                            "gamma_scale": g,
                            "spatial_scale": s,
                            "lambda_m": lam,
                            "dans_cible": self.cible_min <= lam <= self.cible_max,
                        }
                    )
        return pd.DataFrame(lignes)


# ============================================================
# 7. SYSTÈME HYBRIDE (BOUCLE FERMÉE)
# ============================================================


@dataclass
class SystemeHybrideUnifie:
    """Boucle : champ -> observables -> prédiction -> Pi -> g_eff -> champ.

    La loi ``g_eff = g (1 + β (Pi/Pi_ref - 1))`` est un CHOIX DE
    CONCEPTION, non dérivé d'une théorie.
    """

    champ: DynamiqueJaugeCovarianteExacte = field(
        default_factory=DynamiqueJaugeCovarianteExacte
    )
    rls_ipr: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    rls_re: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    rls_im: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    regulateur: RegulateurPrecisionRobuste = field(
        default_factory=RegulateurPrecisionRobuste
    )
    retroaction: float = 0.2
    Pi: float = 1.0
    Pi_ref: float = 1.0
    K: float = 1.2

    def pas_temporel(self, dt: float = 0.01) -> Dict[str, float]:
        """Exécute un pas complet et retourne les observables."""
        c = self.champ
        c.g_eff = max(
            0.0,
            c.g_kerr * (1.0 + self.retroaction * (self.Pi / self.Pi_ref - 1.0)),
        )
        psi = c.pas_strang(dt)

        ipr = c.ipr()
        m = c.moyenne_complexe()
        contraste = ContrasteCoherenceHilbertien.mesure(psi, c.dx)
        cd = c.contraste_densite()

        # Bruit D calculé à partir du champ, borné dans [0.1, 2)
        D = 0.1 + 1.9 * cd / (1.0 + cd)

        err = (
            self.rls_ipr.actualiser(ipr)
            + self.rls_re.actualiser(m.real)
            + self.rls_im.actualiser(m.imag)
        ) / 3.0
        err = float(np.clip(err, 0.0, 5.0))

        K_dyn = self.K * (1.0 + 0.05 * contraste)
        reg = self.regulateur.corriger(self.Pi, D, K_dyn, err)
        self.Pi = reg["Pi"]

        return {
            "norme_L2": c.norme(),
            "norme_avant_renorm": c.norme_avant_renorm,
            "energie_covariante": c.energie_covariante(),
            "ipr": ipr,
            "contraste_densite": cd,
            "m_re": m.real,
            "m_im": m.imag,
            "phase": c.phase_moyenne(),
            "variance_phase": c.variance_phase(),
            "contraste_coherence": contraste,
            "erreur_pred_rel": err,
            "D": D,
            "Pi": self.Pi,
            "g_eff": c.g_eff,
            "kappa": reg["kappa"],
            "holonomie": c.holonomie_boucle(),
            "holonomie_mod_2pi": c.holonomie_mod_2pi(),
        }


# ============================================================
# 8. VÉRIFICATION DES INVARIANTS
# ============================================================


def verifier_invariants(
    resolution: int = 512,
    steps: int = 200,
    dt: float = 0.005,
) -> bool:
    """Régime unitaire, boucle ouverte : norme et énergie conservées, flux non nul."""
    ch = DynamiqueJaugeCovarianteExacte(resolution=resolution, gamma=0.0)
    E0 = ch.energie_covariante()
    N0 = ch.norme()
    for _ in range(steps):
        ch.pas_strang(dt)
    dN = abs(ch.norme() - N0)
    dE = abs(ch.energie_covariante() - E0) / max(abs(E0), 1e-30)
    ok = dN < 1e-10 and ch.flux_jauge != 0.0 and dE < 1e-2
    print(
        f"[VERIF] unitaire   |ΔNorme| = {dN:.2e} | ΔE/E = {dE:.2e} | "
        f"flux = {ch.flux_jauge:.6f} rad -> {'OK' if ok else 'ÉCHEC'}"
    )
    return ok


def verifier_relaxation(
    resolution: int = 256,
    steps: int = 150,
    dt: float = 0.01,
    gamma: float = 0.5,
) -> bool:
    """Régime dissipatif : l'énergie doit décroître, le champ rester fini."""
    ch = DynamiqueJaugeCovarianteExacte(resolution=resolution, gamma=gamma)
    E0 = ch.energie_covariante()
    for _ in range(steps):
        ch.pas_strang(dt)
    E1 = ch.energie_covariante()
    ok = bool(np.isfinite(E1)) and E1 < E0
    print(
        f"[VERIF] dissipatif E0 = {E0:.5f} -> E1 = {E1:.5f} "
        f"| perte de norme/pas = {1.0 - ch.norme_avant_renorm:.2e} "
        f"-> {'OK' if ok else 'ÉCHEC'}"
    )
    return ok


# ============================================================
# 9. EXÉCUTION
# ============================================================


def executer_simulation(
    steps: int = 100,
    dt: float = 0.01,
    champ: Optional[DynamiqueJaugeCovarianteExacte] = None,
    retroaction: float = 0.2,
) -> List[Dict[str, float]]:
    """Exécute une simulation complète et retourne l'historique."""
    if steps <= 0:
        raise ValueError("steps doit être > 0.")
    systeme = SystemeHybrideUnifie(
        champ=champ if champ is not None else DynamiqueJaugeCovarianteExacte(),
        retroaction=retroaction,
    )
    return [systeme.pas_temporel(dt) for _ in range(steps)]


def construire_parser() -> argparse.ArgumentParser:
    """Construit le parseur d'arguments en ligne de commande."""
    p = argparse.ArgumentParser(description="Système hybride covariant à boucle fermée.")
    p.add_argument("--steps", type=int, default=None, help="Pas (défaut 100 ; 200 en --verifier).")
    p.add_argument("--dt", type=float, default=None, help="Pas de temps (défaut 0.01 ; 0.005 en --verifier).")
    p.add_argument("--resolution", type=int, default=None, help="Points de grille (défaut 1024 ; 512 en --verifier).")
    p.add_argument("--flux", type=float, default=0.37, help="Flux θ en quanta.")
    p.add_argument("--gamma", type=float, default=0.0, help="Amortissement (0 = unitaire).")
    p.add_argument("--courbure", type=float, default=0.0, help="Couplage densité -> potentiel.")
    p.add_argument("--retroaction", type=float, default=0.2, help="β : Pi -> g_eff (0 = boucle ouverte).")
    p.add_argument("--g", type=float, default=1.0, help="Couplage Kerr g.")
    p.add_argument("--graine", type=int, default=42, help="Graine aléatoire.")
    p.add_argument("--csv", type=str, default=None, help="Écrit l'historique dans ce fichier CSV.")
    p.add_argument("--calibration", action="store_true")
    p.add_argument("--verifier", action="store_true")
    p.add_argument("--json", action="store_true")
    return p


def _valider_args(args: argparse.Namespace) -> Optional[str]:
    """Retourne un message d'erreur, ou ``None`` si les arguments sont valides."""
    if args.steps <= 0:
        return "--steps doit être > 0."
    if not (np.isfinite(args.dt) and args.dt > 0):
        return "--dt doit être un réel fini > 0."
    if args.resolution < 8:
        return "--resolution doit être >= 8."
    if args.gamma < 0:
        return "--gamma doit être >= 0."
    if args.g < 0:
        return "--g doit être >= 0."
    if args.retroaction < 0:
        return "--retroaction doit être >= 0."
    return None


def main() -> int:
    """Point d'entrée principal."""
    args = construire_parser().parse_args()

    # Défauts dépendant du mode
    defauts = (200, 0.005, 512) if args.verifier else (100, 0.01, 1024)
    args.steps = defauts[0] if args.steps is None else args.steps
    args.dt = defauts[1] if args.dt is None else args.dt
    args.resolution = defauts[2] if args.resolution is None else args.resolution

    erreur = _valider_args(args)
    if erreur:
        print(f"[!] {erreur}")
        return 1

    if args.verifier:
        ok1 = verifier_invariants(args.resolution, args.steps, args.dt)
        ok2 = verifier_relaxation()
        return 0 if (ok1 and ok2) else 1

    if args.calibration:
        cal = CalibrationMultidimensionnelle()
        df = cal.executer_balayage()
        cible = df[df["dans_cible"]]
        print(
            cible.head(10)
            if not cible.empty
            else f"[!] Aucune configuration dans [{cal.cible_min}, {cal.cible_max}] m."
        )
        return 0

    try:
        champ = DynamiqueJaugeCovarianteExacte(
            resolution=args.resolution,
            flux_theta=args.flux,
            gamma=args.gamma,
            coeff_courbure=args.courbure,
            g_kerr=args.g,
            graine=args.graine,
        )
        systeme = SystemeHybrideUnifie(champ=champ, retroaction=args.retroaction)
    except ValueError as exc:
        print(f"[!] Paramètre invalide : {exc}")
        return 1

    print(
        f"[INIT] {args.steps} pas, dt={args.dt}, N={args.resolution}, "
        f"θ={args.flux}, γ={args.gamma}, β={args.retroaction}"
    )

    historique: List[Dict[str, float]] = []
    try:
        for i in range(args.steps):
            etat = systeme.pas_temporel(args.dt)
            historique.append(etat)
            if (i + 1) % 20 == 0:
                print(
                    f"  Pas {i + 1:04d} | N={etat['norme_L2']:.10f} | "
                    f"E={etat['energie_covariante']:.5f} | IPR={etat['ipr']:.5f} | "
                    f"C={etat['contraste_coherence']:.4f} | Pi={etat['Pi']:.4f} | "
                    f"κ={etat['kappa']:.4f} | err={etat['erreur_pred_rel']:.3e}"
                )
    except (FloatingPointError, ValueError) as exc:
        print(f"[!] Simulation interrompue au pas {len(historique) + 1} : {exc}")
        return 2

    dernier = historique[-1]
    print("\n[BILAN FINAL]")
    for cle, val in dernier.items():
        print(f"  {cle:20s}: {val:14.8f}")
    if args.json:
        print(json.dumps(dernier, indent=2, ensure_ascii=False))
    if args.csv:
        pd.DataFrame(historique).to_csv(args.csv, index=False)
        print(f"[CSV] Historique écrit dans {args.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vacuite_holotelegraphique.py
============================

Système hybride en boucle fermée, vérification des invariants et CLI.

Architecture ::

    Champ -> Phase -> Cohérence -> Mémoire -> Prédiction -> Précision -> Calibration

Statut : prototype conceptuel. Aucune prétention à modéliser la conscience,
une mémoire phénoménologique, une holonomie biologique ou une autopoïèse
réelle. Prototype != démonstration ; simulation != explication.

Exemples ::

    python vacuite_holotelegraphique.py --steps 100 --dt 0.01
    python vacuite_holotelegraphique.py --gamma 0.5          # relaxation
    python vacuite_holotelegraphique.py --verifier
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

from calibration import CalibrationMultidimensionnelle
from champ import ContrasteCoherenceHilbertien, DynamiqueJaugeCovarianteExacte
from controle import PredicteurAdaptatifRLS, RegulateurPrecisionRobuste

# ============================================================
# 7. SYSTÈME HYBRIDE (BOUCLE FERMÉE)
# ============================================================


@dataclass
class SystemeHybrideUnifie:
    """Boucle : champ -> observables -> prédiction -> Pi -> g_eff -> champ.

    La loi ``g_eff = g (1 + β (Pi/Pi_ref - 1))`` est un CHOIX DE
    CONCEPTION, non dérivé d'une théorie.
    """

    champ: DynamiqueJaugeCovarianteExacte = field(
        default_factory=DynamiqueJaugeCovarianteExacte
    )
    rls_ipr: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    rls_re: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    rls_im: PredicteurAdaptatifRLS = field(default_factory=PredicteurAdaptatifRLS)
    regulateur: RegulateurPrecisionRobuste = field(
        default_factory=RegulateurPrecisionRobuste
    )
    retroaction: float = 0.2
    Pi: float = 1.0
    Pi_ref: float = 1.0
    K: float = 1.2

    def pas_temporel(self, dt: float = 0.01) -> Dict[str, float]:
        """Exécute un pas complet et retourne les observables."""
        c = self.champ
        c.g_eff = max(
            0.0,
            c.g_kerr * (1.0 + self.retroaction * (self.Pi / self.Pi_ref - 1.0)),
        )
        psi = c.pas_strang(dt)

        ipr = c.ipr()
        m = c.moyenne_complexe()
        contraste = ContrasteCoherenceHilbertien.mesure(psi, c.dx)
        cd = c.contraste_densite()

        # Bruit D calculé à partir du champ, borné dans [0.1, 2)
        D = 0.1 + 1.9 * cd / (1.0 + cd)

        err = (
            self.rls_ipr.actualiser(ipr)
            + self.rls_re.actualiser(m.real)
            + self.rls_im.actualiser(m.imag)
        ) / 3.0
        err = float(np.clip(err, 0.0, 5.0))

        K_dyn = self.K * (1.0 + 0.05 * contraste)
        reg = self.regulateur.corriger(self.Pi, D, K_dyn, err)
        self.Pi = reg["Pi"]

        return {
            "norme_L2": c.norme(),
            "norme_avant_renorm": c.norme_avant_renorm,
            "energie_covariante": c.energie_covariante(),
            "ipr": ipr,
            "contraste_densite": cd,
            "m_re": m.real,
            "m_im": m.imag,
            "phase": c.phase_moyenne(),
            "variance_phase": c.variance_phase(),
            "contraste_coherence": contraste,
            "erreur_pred_rel": err,
            "D": D,
            "Pi": self.Pi,
            "g_eff": c.g_eff,
            "kappa": reg["kappa"],
            "holonomie": c.holonomie_boucle(),
            "holonomie_mod_2pi": c.holonomie_mod_2pi(),
        }


# ============================================================
# 8. VÉRIFICATION DES INVARIANTS
# ============================================================


def verifier_invariants(
    resolution: int = 512,
    steps: int = 200,
    dt: float = 0.005,
) -> bool:
    """Régime unitaire, boucle ouverte : norme et énergie conservées, flux non nul."""
    ch = DynamiqueJaugeCovarianteExacte(resolution=resolution, gamma=0.0)
    E0 = ch.energie_covariante()
    N0 = ch.norme()
    for _ in range(steps):
        ch.pas_strang(dt)
    dN = abs(ch.norme() - N0)
    dE = abs(ch.energie_covariante() - E0) / max(abs(E0), 1e-30)
    ok = dN < 1e-10 and ch.flux_jauge != 0.0 and dE < 1e-2
    print(
        f"[VERIF] unitaire   |ΔNorme| = {dN:.2e} | ΔE/E = {dE:.2e} | "
        f"flux = {ch.flux_jauge:.6f} rad -> {'OK' if ok else 'ÉCHEC'}"
    )
    return ok


def verifier_relaxation(
    resolution: int = 256,
    steps: int = 150,
    dt: float = 0.01,
    gamma: float = 0.5,
) -> bool:
    """Régime dissipatif : l'énergie doit décroître, le champ rester fini."""
    ch = DynamiqueJaugeCovarianteExacte(resolution=resolution, gamma=gamma)
    E0 = ch.energie_covariante()
    for _ in range(steps):
        ch.pas_strang(dt)
    E1 = ch.energie_covariante()
    ok = bool(np.isfinite(E1)) and E1 < E0
    print(
        f"[VERIF] dissipatif E0 = {E0:.5f} -> E1 = {E1:.5f} "
        f"| perte de norme/pas = {1.0 - ch.norme_avant_renorm:.2e} "
        f"-> {'OK' if ok else 'ÉCHEC'}"
    )
    return ok


# ============================================================
# 9. EXÉCUTION
# ============================================================


def executer_simulation(
    steps: int = 100,
    dt: float = 0.01,
    champ: Optional[DynamiqueJaugeCovarianteExacte] = None,
    retroaction: float = 0.2,
) -> List[Dict[str, float]]:
    """Exécute une simulation complète et retourne l'historique."""
    if steps <= 0:
        raise ValueError("steps doit être > 0.")
    systeme = SystemeHybrideUnifie(
        champ=champ if champ is not None else DynamiqueJaugeCovarianteExacte(),
        retroaction=retroaction,
    )
    return [systeme.pas_temporel(dt) for _ in range(steps)]


def construire_parser() -> argparse.ArgumentParser:
    """Construit le parseur d'arguments en ligne de commande."""
    p = argparse.ArgumentParser(description="Système hybride covariant à boucle fermée.")
    p.add_argument("--steps", type=int, default=None, help="Pas (défaut 100 ; 200 en --verifier).")
    p.add_argument("--dt", type=float, default=None, help="Pas de temps (défaut 0.01 ; 0.005 en --verifier).")
    p.add_argument("--resolution", type=int, default=None, help="Points de grille (défaut 1024 ; 512 en --verifier).")
    p.add_argument("--flux", type=float, default=0.37, help="Flux θ en quanta.")
    p.add_argument("--gamma", type=float, default=0.0, help="Amortissement (0 = unitaire).")
    p.add_argument("--courbure", type=float, default=0.0, help="Couplage densité -> potentiel.")
    p.add_argument("--retroaction", type=float, default=0.2, help="β : Pi -> g_eff (0 = boucle ouverte).")
    p.add_argument("--g", type=float, default=1.0, help="Couplage Kerr g.")
    p.add_argument("--graine", type=int, default=42, help="Graine aléatoire.")
    p.add_argument("--csv", type=str, default=None, help="Écrit l'historique dans ce fichier CSV.")
    p.add_argument("--calibration", action="store_true")
    p.add_argument("--verifier", action="store_true")
    p.add_argument("--json", action="store_true")
    return p


def _valider_args(args: argparse.Namespace) -> Optional[str]:
    """Retourne un message d'erreur, ou ``None`` si les arguments sont valides."""
    if args.steps <= 0:
        return "--steps doit être > 0."
    if not (np.isfinite(args.dt) and args.dt > 0):
        return "--dt doit être un réel fini > 0."
    if args.resolution < 8:
        return "--resolution doit être >= 8."
    if args.gamma < 0:
        return "--gamma doit être >= 0."
    if args.g < 0:
        return "--g doit être >= 0."
    if args.retroaction < 0:
        return "--retroaction doit être >= 0."
    return None


def main() -> int:
    """Point d'entrée principal."""
    args = construire_parser().parse_args()

    # Défauts dépendant du mode
    defauts = (200, 0.005, 512) if args.verifier else (100, 0.01, 1024)
    args.steps = defauts[0] if args.steps is None else args.steps
    args.dt = defauts[1] if args.dt is None else args.dt
    args.resolution = defauts[2] if args.resolution is None else args.resolution

    erreur = _valider_args(args)
    if erreur:
        print(f"[!] {erreur}")
        return 1

    if args.verifier:
        ok1 = verifier_invariants(args.resolution, args.steps, args.dt)
        ok2 = verifier_relaxation()
        return 0 if (ok1 and ok2) else 1

    if args.calibration:
        cal = CalibrationMultidimensionnelle()
        df = cal.executer_balayage()
        cible = df[df["dans_cible"]]
        print(
            cible.head(10)
            if not cible.empty
            else f"[!] Aucune configuration dans [{cal.cible_min}, {cal.cible_max}] m."
        )
        return 0

    try:
        champ = DynamiqueJaugeCovarianteExacte(
            resolution=args.resolution,
            flux_theta=args.flux,
            gamma=args.gamma,
            coeff_courbure=args.courbure,
            g_kerr=args.g,
            graine=args.graine,
        )
        systeme = SystemeHybrideUnifie(champ=champ, retroaction=args.retroaction)
    except ValueError as exc:
        print(f"[!] Paramètre invalide : {exc}")
        return 1

    print(
        f"[INIT] {args.steps} pas, dt={args.dt}, N={args.resolution}, "
        f"θ={args.flux}, γ={args.gamma}, β={args.retroaction}"
    )

    historique: List[Dict[str, float]] = []
    try:
        for i in range(args.steps):
            etat = systeme.pas_temporel(args.dt)
            historique.append(etat)
            if (i + 1) % 20 == 0:
                print(
                    f"  Pas {i + 1:04d} | N={etat['norme_L2']:.10f} | "
                    f"E={etat['energie_covariante']:.5f} | IPR={etat['ipr']:.5f} | "
                    f"C={etat['contraste_coherence']:.4f} | Pi={etat['Pi']:.4f} | "
                    f"κ={etat['kappa']:.4f} | err={etat['erreur_pred_rel']:.3e}"
                )
    except (FloatingPointError, ValueError) as exc:
        print(f"[!] Simulation interrompue au pas {len(historique) + 1} : {exc}")
        return 2

    dernier = historique[-1]
    print("\n[BILAN FINAL]")
    for cle, val in dernier.items():
        print(f"  {cle:20s}: {val:14.8f}")
    if args.json:
        print(json.dumps(dernier, indent=2, ensure_ascii=False))
    if args.csv:
        pd.DataFrame(historique).to_csv(args.csv, index=False)
        print(f"[CSV] Historique écrit dans {args.csv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
champ.py
========

Champ complexe sur un tore, jauge U(1), Strang splitting, cohérence
hilbertienne.

Équation (régime unitaire, gamma = 0) ::

    i ∂ψ/∂t = -½ D²ψ + g_eff |ψ|²ψ + V(x)ψ + V_courbure[ρ]ψ ,  D = ∂x - iA(x)

Régime dissipatif (gamma > 0) : ``i ∂ψ/∂t = (1 - iγ) H ψ`` avec
renormalisation L2.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.fft import fft, fftfreq, ifft

from outils import normaliser_L2

# ============================================================
# 2. DYNAMIQUE DU CHAMP
# ============================================================


@dataclass
class DynamiqueJaugeCovarianteExacte:
    """Dynamique spectrale d'un champ complexe sur un tore avec jauge U(1).

    La jauge est décomposée en ``A = A_0 + A_per`` : ``A_0 = 2πθ/L`` porte
    l'holonomie (seule physique, modulo 2π en flux) et ``A_per`` est de
    jauge pure en 1D.
    """

    resolution: int = 1024
    etendue_spatiale: float = 50.0
    p: int = 2
    q: int = 3
    flux_theta: float = 0.37  # flux en quanta (physique mod 1)
    lambda_jauge: float = 2.0
    amplitude_jauge: float = 0.1  # amplitude de A_per
    k_coupure_init: float = 2.0  # bande passante de l'état initial
    g_kerr: float = 1.0
    alpha_pot: float = 0.1
    gamma: float = 0.0  # 0 = unitaire ; > 0 = relaxation
    # densité -> potentiel ; instable si trop grand avec gamma > 0
    # (0,5 stable, 5 diverge dans nos essais)
    coeff_courbure: float = 0.0
    largeur_filtre: float = 0.15
    graine: int = 42

    def __post_init__(self) -> None:
        self._valider()
        self.N = int(self.resolution)
        self.L = float(self.etendue_spatiale)
        self.dx = self.L / self.N
        self.x = np.linspace(-self.L / 2, self.L / 2, self.N, endpoint=False)
        self.k_base = 2.0 * np.pi * fftfreq(self.N, d=self.dx)
        self.g_eff = float(self.g_kerr)

        # Jauge : A = A_0 (holonomie) + A_per (moyenne nulle, de jauge)
        ang_p = 2.0 * np.pi * self.p * self.x / self.L
        ang_q = 2.0 * np.pi * self.q * self.x / self.L
        A_per = (
            self.amplitude_jauge
            * (2.0 * np.pi / self.lambda_jauge)
            * (self.p * np.cos(ang_q) + self.q * np.sin(ang_p))
        )
        A_per -= np.mean(A_per)
        self.A_0 = 2.0 * np.pi * self.flux_theta / self.L
        self.A = self.A_0 + A_per
        self.flux_jauge = self.A_0 * self.L  # = 2π θ

        # Phase périodique φ telle que φ' = A_per
        denom = 1j * self.k_base
        denom[0] = 1.0
        phi_k = fft(A_per) / denom
        phi_k[0] = 0.0
        self.phi_jauge = ifft(phi_k).real
        self.phase_gauge_plus = np.exp(1j * self.phi_jauge)
        self.phase_gauge_moins = np.exp(-1j * self.phi_jauge)

        # Grille spectrale tordue : (ik - iA_0) = i(k - A_0)
        self.k_tordu = self.k_base - self.A_0

        # Potentiel scalaire externe
        self.V = self.alpha_pot * np.cos(2.0 * np.pi * self.x / self.L)

        # Champ initial : bruit complexe passe-bas (un bruit blanc sature
        # la grille et provoque de l'aliasing)
        rng = np.random.default_rng(self.graine)
        enveloppe = np.exp(-(self.x**2) / 8.0)
        bruit = rng.normal(size=self.N) + 1j * rng.normal(size=self.N)
        bruit = ifft(fft(bruit) * np.exp(-((self.k_base / self.k_coupure_init) ** 2)))
        self.psi = normaliser_L2(enveloppe * bruit, self.dx)
        self.norme_avant_renorm = self.norme()

    def _valider(self) -> None:
        """Vérifie la cohérence des paramètres."""
        if int(self.resolution) < 8:
            raise ValueError("resolution doit être >= 8.")
        if not self.etendue_spatiale > 0:
            raise ValueError("etendue_spatiale doit être > 0.")
        if self.gamma < 0:
            raise ValueError("gamma doit être >= 0.")
        if self.g_kerr < 0:
            raise ValueError("g_kerr doit être >= 0.")
        if not self.k_coupure_init > 0:
            raise ValueError("k_coupure_init doit être > 0.")
        if self.largeur_filtre < 0:
            raise ValueError("largeur_filtre doit être >= 0.")
        if self.lambda_jauge == 0:
            raise ValueError("lambda_jauge ne doit pas être nul.")

    # -- courbure effective (analogie, pas relativité générale) --
    def courbure(self, rho: np.ndarray) -> np.ndarray:
        """Retourne ``-∂²ρ_lissé`` (analogie structurelle)."""
        k_max = np.max(np.abs(self.k_base))
        filtre = np.exp(-self.largeur_filtre * (np.abs(self.k_base) / k_max) ** 4)
        rho_k = fft(rho) * filtre
        return ifft(self.k_base**2 * rho_k).real

    def potentiel_effectif(self, rho: np.ndarray) -> np.ndarray:
        """Potentiel total : externe + Kerr + courbure effective."""
        v = self.V + self.g_eff * rho
        if self.coeff_courbure != 0.0:
            v = v + self.coeff_courbure * self.courbure(rho)
        return v

    # -- pas élémentaires --------------------------------------
    def pas_potentiel(self, dt_demi: float) -> None:
        """Applique ``exp(-i v dt)`` (unitaire) et l'amortissement éventuel.

        La soustraction de la moyenne de ``v`` dans l'amortissement est un
        choix de modélisation : elle n'ajoute qu'un facteur global, annulé
        par la renormalisation L2.
        """
        v = self.potentiel_effectif(np.abs(self.psi) ** 2)
        self.psi *= np.exp(-1j * v * dt_demi)
        if self.gamma > 0.0:
            expo = np.clip(-self.gamma * (v - np.mean(v)) * dt_demi, -30.0, 30.0)
            self.psi *= np.exp(expo)

    def pas_cinetique_tordu(self, dt: float) -> None:
        """Pas cinétique covariant exact (jauge + FFT tordue + retour)."""
        chi = self.psi * self.phase_gauge_moins
        chi_k = fft(chi) * np.exp(-0.5 * (1j + self.gamma) * self.k_tordu**2 * dt)
        self.psi = ifft(chi_k) * self.phase_gauge_plus

    def pas_strang(self, dt: float) -> np.ndarray:
        """Un pas de Strang splitting ``e^{-iVdt/2} e^{-iTdt} e^{-iVdt/2}``.

        Raises
        ------
        ValueError
            Si ``dt`` n'est pas un réel fini strictement positif.
        FloatingPointError
            Si le champ devient non fini (divergence numérique).
        """
        if not (np.isfinite(dt) and dt > 0):
            raise ValueError("dt doit être un réel fini > 0.")
        self.pas_potentiel(0.5 * dt)
        self.pas_cinetique_tordu(dt)
        self.pas_potentiel(0.5 * dt)
        if not np.all(np.isfinite(self.psi)):
            raise FloatingPointError("Divergence numérique : champ non fini.")
        # Norme mesurée AVANT renormalisation : en régime dissipatif elle
        # reflète la perte réelle ; après renormalisation elle vaut 1.
        self.norme_avant_renorm = self.norme()
        if self.gamma > 0.0:
            self.psi = normaliser_L2(self.psi, self.dx)
        return self.psi

    # -- observables -------------------------------------------
    def densite(self) -> np.ndarray:
        """Densité ``|ψ|²``."""
        return np.abs(self.psi) ** 2

    def norme(self) -> float:
        """Norme L2 discrète."""
        return float(np.sum(self.densite()) * self.dx)

    def ipr(self) -> float:
        """``∫ρ² / (∫ρ)²`` : inverse de l'étendue effective."""
        rho = self.densite()
        total = float(np.sum(rho) * self.dx)
        return float(np.sum(rho**2) * self.dx / max(total**2, 1e-30))

    def contraste_densite(self) -> float:
        """Variance normalisée de la densité."""
        rho = self.densite()
        return float(np.var(rho) / max(np.mean(rho) ** 2, 1e-30))

    def moyenne_complexe(self) -> complex:
        """``m = (1/√L) ∫ψ dx`` ; ``|m| <= 1`` (évite le saut de ±π)."""
        return complex(np.sum(self.psi) * self.dx / np.sqrt(self.L))

    def phase_moyenne(self) -> float:
        """Phase de la moyenne complexe (peut sauter de ±π)."""
        return float(np.angle(np.sum(self.psi) * self.dx))

    def variance_phase(self) -> float:
        """Variance de la phase locale (sensible au repliement ±π)."""
        return float(np.var(np.angle(self.psi)))

    def holonomie_boucle(self) -> float:
        """Flux de jauge ``2πθ`` sur le tore (rad)."""
        return self.flux_jauge

    def holonomie_mod_2pi(self) -> float:
        """Flux de jauge réduit modulo 2π (grandeur physique)."""
        return float(np.mod(self.flux_jauge, 2.0 * np.pi))

    def energie_covariante(self) -> float:
        """``E = ∫[½|Dψ|² + (g/2)ρ² + Vρ + V_c ρ] dx`` (diagnostic)."""
        dpsi = ifft(1j * self.k_base * fft(self.psi)) - 1j * self.A * self.psi
        rho = self.densite()
        dens = 0.5 * np.abs(dpsi) ** 2 + 0.5 * self.g_eff * rho**2 + self.V * rho
        if self.coeff_courbure != 0.0:
            dens = dens + self.coeff_courbure * self.courbure(rho) * rho
        return float(np.sum(dens) * self.dx)


# ============================================================
# 3. COHÉRENCE HILBERTIENNE
# ============================================================


class ContrasteCoherenceHilbertien:
    """Contraste de recouvrement hilbertien (et non interférence physique).

    ``C = |<ψ,ψ_m>|² / (‖ψ‖² ‖ψ_m‖²)`` avec ``ψ_m = ψ·exp(iπ ρ/ρ_max)``.
    """

    @staticmethod
    def mesure(psi: np.ndarray, dx: float) -> float:
        """Retourne ``C`` dans ``[0, 1]``."""
        rho = np.abs(psi) ** 2
        rmax = np.max(rho)
        if rmax <= 1e-30:
            return 0.0
        psi_m = psi * np.exp(1j * np.pi * rho / rmax)
        n1 = np.sum(np.abs(psi) ** 2) * dx
        n2 = np.sum(np.abs(psi_m) ** 2) * dx
        ps = np.sum(np.conj(psi) * psi_m) * dx
        return float(np.abs(ps) ** 2 / (n1 * n2))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
controle.py
===========

Prédicteur RLS adaptatif et régulateur homéostatique de précision.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import numpy as np

from outils import inverser_kappa_newton, kappa_bessel

# ============================================================
# 4. PRÉDICTEUR RLS ADAPTATIF
# ============================================================


class PredicteurAdaptatifRLS:
    """Filtre des moindres carrés récursifs (RLS) d'ordre M.

    Ordre des opérations : prédiction -> erreur -> poids -> décalage.
    """

    def __init__(
        self,
        ordre: int = 3,
        lambda_oubli: float = 0.985,
        delta: float = 10.0,
    ) -> None:
        if int(ordre) < 1:
            raise ValueError("ordre doit être >= 1.")
        if not 0.0 < lambda_oubli <= 1.0:
            raise ValueError("lambda_oubli doit être dans ]0, 1].")
        self.ordre = int(ordre)
        self.lam = float(lambda_oubli)
        self.w = np.zeros(self.ordre)
        self.P = np.eye(self.ordre) * float(delta)
        self.tampon = np.zeros(self.ordre)
        self.echelle = 0.0  # moyenne glissante de |valeur|

    def predire(self) -> float:
        """Prédiction courante."""
        return float(np.dot(self.w, self.tampon))

    def actualiser(self, valeur: float) -> float:
        """Met à jour le filtre ; retourne l'erreur RELATIVE.

        Raises
        ------
        ValueError
            Si ``valeur`` n'est pas finie.
        """
        valeur = float(valeur)
        if not np.isfinite(valeur):
            raise ValueError("Observation non finie.")
        x = self.tampon.copy()
        erreur = float(valeur - np.dot(self.w, x))
        Px = self.P @ x
        g = Px / max(self.lam + float(np.dot(x, Px)), 1e-12)
        self.w += g * erreur
        self.P = (self.P - np.outer(g, Px)) / self.lam
        self.tampon = np.roll(self.tampon, 1)
        self.tampon[0] = valeur
        if self.echelle == 0.0:
            self.echelle = abs(valeur)
        else:
            self.echelle = 0.9 * self.echelle + 0.1 * abs(valeur)
        return abs(erreur) / max(self.echelle, 1e-9)


# ============================================================
# 5. RÉGULATEUR DE PRÉCISION
# ============================================================


@dataclass
class RegulateurPrecisionRobuste:
    """Régulateur homéostatique de précision de type PI."""

    target_kappa: float = 0.85
    kp: float = 0.35
    ki: float = 0.03
    integrale: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 < self.target_kappa < 1.0:
            raise ValueError("target_kappa doit être dans ]0, 1[.")
        self.x_consigne = inverser_kappa_newton(self.target_kappa)

    def corriger(
        self,
        Pi: float,
        D: float,
        K: float,
        incertitude: float,
    ) -> Dict[str, float]:
        """Met à jour la précision selon bruit ``D``, couplage ``K`` et incertitude."""
        D = max(float(D), 1e-6)
        K = max(float(K), 1e-6)
        incertitude = float(np.nan_to_num(incertitude, nan=0.0, posinf=5.0))
        consigne = (self.x_consigne * D / K) * (1.0 + incertitude)
        erreur = consigne - Pi
        self.integrale = float(np.clip(self.integrale + erreur, -5.0, 5.0))
        Pi_new = float(
            np.clip(Pi + self.kp * erreur + self.ki * self.integrale, 0.01, 20.0)
        )
        x_eff = Pi_new * K / D
        k_mes = float(kappa_bessel(x_eff))
        return {
            "Pi": Pi_new,
            "x": x_eff,
            "kappa": k_mes,
            "erreur_kappa": self.target_kappa - k_mes,
        }

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
outils.py
=========

Utilitaires : normalisation L2, plancher lisse, rapport de Bessel
kappa(x) = I1(x) / I0(x) et son inverse.
"""

from __future__ import annotations

import numpy as np
from scipy.special import ive

# ============================================================
# 0. CONSTANTES
# ============================================================

EPSILON = 1e-12

# ============================================================
# 1. UTILITAIRES MATHÉMATIQUES
# ============================================================


def normaliser_L2(champ: np.ndarray, dx: float, cible: float = 1.0) -> np.ndarray:
    """Normalise un champ complexe pour que ``∫|ψ|² dx = cible``.

    Raises
    ------
    ValueError
        Si le champ contient des valeurs non finies ou une norme quasi nulle.
    """
    champ = np.asarray(champ)
    if not np.all(np.isfinite(champ)):
        raise ValueError("Champ non fini (NaN ou inf).")
    norme2 = float(np.sum(np.abs(champ) ** 2) * dx)
    if norme2 <= 1e-30:
        raise ValueError("Norme du champ quasi-nulle.")
    return champ * np.sqrt(cible / norme2)


def plancher_lisse(
    valeurs: np.ndarray,
    seuil: float = 0.01,
    largeur: float = 0.01,
) -> np.ndarray:
    """Plancher lisse évitant les valeurs nulles ou négatives."""
    return seuil + largeur * np.logaddexp((valeurs - seuil) / largeur, 0.0)


def kappa_bessel(x):
    """Rapport de concentration circulaire ``kappa(x) = I1(x) / I0(x)``."""
    x = np.maximum(x, 1e-12)
    return ive(1, x) / np.maximum(ive(0, x), 1e-300)


def inverser_kappa_newton(
    target: float,
    tol: float = 1e-10,
    max_iter: int = 50,
) -> float:
    """Résout ``kappa(x) = target`` par Newton, avec repli par dichotomie.

    La dérivée exacte est ``dkappa/dx = 1 - k/x - k²``. Kappa étant
    strictement croissante, la dichotomie sert de filet de sécurité si
    Newton ne converge pas.
    """
    target = float(np.clip(target, 1e-6, 0.999))
    x = 1.0
    for _ in range(max_iter):
        k = float(kappa_bessel(x))
        diff = k - target
        if abs(diff) < tol:
            return float(x)
        dk = max(1.0 - k / x - k * k, 1e-10)
        x = max(x - diff / dk, 1e-8)

    bas, haut = 1e-9, 1e4
    for _ in range(200):
        milieu = 0.5 * (bas + haut)
        if float(kappa_bessel(milieu)) < target:
            bas = milieu
        else:
            haut = milieu
    return float(0.5 * (bas + haut))


Annexe de correction 

# Spécifications du module de jauge sur le tore

## 1. Objet du module

Le module `champ.py` implémente la dynamique d’un champ complexe $$\psi(x,t)$$ sur le cercle $$S^1$$ de longueur $$L$$, avec couplage minimal à une jauge $$U(1)$$.

Équation de base :

$$
i\frac{\partial\psi}{\partial t}
=
-\frac{1}{2}D^2\psi
+
g_{\text{eff}}|\psi|^2\psi
+
V(x)\psi
+
V_{\text{courbure}}[\rho]\psi,
$$

avec la dérivée covariante :

$$
D = \frac{\partial}{\partial x} - iA(x).
$$

Le module doit séparer clairement :

- la composante topologique de la jauge ;
- la composante de jauge pure ;
- la grille spectrale tordue ;
- les observables physiques.

***

## 2. Structure de la jauge

### 2.1 Décomposition

Le potentiel de jauge est décomposé en :

$$
A(x) = A_0 + A_{\text{per}}(x),
$$

où :

- $$A_0$$ est constant, porteur de l’holonomie globale ;
- $$A_{\text{per}}(x)$$ est périodique, de moyenne nulle, donc de jauge pure.

### 2.2 Composante topologique

$$
A_0 = \frac{2\pi\theta}{L},
$$

où $$\theta$$ est le flux en quanta.

Le flux total est :

$$
\Phi = A_0L = 2\pi\theta.
$$

Seul $$\Phi \bmod 2\pi$$ est physiquement observable. 

### 2.3 Composante de jauge pure

$$
A_{\text{per}}(x)
=
\frac{2\pi}{\lambda_{\text{jauge}}}
\left[
p\cos\left(\frac{2\pi qx}{L}\right)
+
q\sin\left(\frac{2\pi px}{L}\right)
\right],
$$

avec la contrainte :

$$
\int_0^L A_{\text{per}}(x)\,dx = 0.
$$

Cette composante est éliminable par une transformation de jauge $$U(1)$$.[1][2][3]

***

## 3. Grille spectrale tordue

### 3.1 Principe

La dérivée covariante s’écrit :

$$
D\psi
=
\left(\frac{\partial}{\partial x} - iA_0\right)\psi
-
iA_{\text{per}}(x)\psi.
$$

Après transformation de jauge :

$$
\chi(x) = e^{-i\phi(x)}\psi(x),
$$

avec $$\phi'(x) = A_{\text{per}}(x)$$, la partie périodique est absorbée.

Il reste :

$$
\left(\frac{\partial}{\partial x} - iA_0\right)\chi.
$$

### 3.2 Grille tordue

En espace de Fourier :

$$
k_{\text{tordu}} = k_{\text{base}} - A_0.
$$

Le pas cinétique s’écrit alors :

$$
\hat{\chi}(k,t+\Delta t)
=
\exp\left[-\frac{i}{2}(k-A_0)^2\Delta t\right]
\hat{\chi}(k,t).
$$

Cette grille tordue est la bonne manière de traiter l’holonomie spectralement. 

***

## 4. Conditions aux bords

### 4.1 Champ

$$
\psi(x+L) = \psi(x).
$$

### 4.2 Jauge

$$
A(x+L) = A(x).
$$

### 4.3 Phase de jauge

$$
\phi(x+L) = \phi(x).
$$

### 4.4 Holonomie

$$
\exp\left(i\oint A\,dx\right)
=
\exp(i2\pi\theta).
$$

L’holonomie est définie modulo $$2\pi$$.[2][3][4][5]

***

## 5. Observables physiques

| Observable | Définition | Rôle |
|---|---|---|
| Norme $$L^2$$ | $$\int|\psi|^2dx$$ | Conservation |
| IPR | $$\int\rho^2dx/(\int\rho dx)^2$$ | Localisation |
| Contraste de densité | $$\mathrm{Var}(\rho)/\langle\rho\rangle^2$$ | Hétérogénéité |
| Moyenne complexe | $$\frac{1}{\sqrt{L}}\int\psi dx$$ | Phase globale |
| Holonomie | $$\Phi \bmod 2\pi$$ | Invariant topologique |
| Énergie covariante | $$\int[\frac12|D\psi|^2+\frac{g}{2}\rho^2+V\rho]dx$$ | Diagnostic |

La moyenne complexe évite le saut de $$\pm\pi$$ de $$\arg(\sum\psi)$$.

***

## 6. Régimes dynamiques

### 6.1 Régime unitaire

$$
\gamma = 0.
$$

Propriétés :

- norme $$L^2$$ exactement conservée ;
- énergie approximativement conservée ;
- pas de Strang unitaire.

### 6.2 Régime dissipatif

$$
\gamma > 0.
$$

Équation effective :

$$
i\frac{\partial\psi}{\partial t}
=
(1-i\gamma)H\psi.
$$

Propriétés :

- norme non conservée sans renormalisation ;
- renormalisation $$L^2$$ imposée ;
- relaxation vers un état stationnaire ;
- énergie non conservée.

Le schéma de Strang est d’ordre 2 et préserve la masse dans le régime unitaire. 

***

## 7. Interface du module

### 7.1 Entrées

| Paramètre | Type | Rôle |
|---|---|---|
| `resolution` | int | Nombre de points |
| `etendue_spatiale` | float | Longueur du tore |
| `flux_theta` | float | Flux en quanta |
| `lambda_jauge` | float | Échelle de la jauge |
| `amplitude_jauge` | float | Amplitude de $$A_{\text{per}}$$ |
| `g_kerr` | float | Couplage Kerr |
| `alpha_pot` | float | Amplitude du potentiel |
| `gamma` | float | Amortissement |
| `coeff_courbure` | float | Couplage densité-potentiel |
| `graine` | int | Reproductibilité |

### 7.2 Sorties

| Observable | Type | Rôle |
|---|---|---|
| `norme_L2` | float | Norme |
| `norme_avant_renorm` | float | Norme avant renormalisation |
| `energie_covariante` | float | Énergie |
| `ipr` | float | Localisation |
| `contraste_densite` | float | Hétérogénéité |
| `moyenne_complexe` | complex | Phase globale |
| `holonomie_mod_2pi` | float | Invariant topologique |

***

## 8. Contraintes de conception

1. La composante topologique $$A_0$$ doit être distinguée de la composante de jauge pure $$A_{\text{per}}$$.
2. La grille tordue doit absorber $$A_0$$, pas $$A_{\text{per}}$$.
3. La phase de jauge doit être périodique.
4. L’holonomie doit être rapportée modulo $$2\pi$$.
5. La norme doit être mesurée avant renormalisation en régime dissipatif.
6. L’énergie doit être traitée comme un diagnostic, pas comme un invariant exact.
7. Le contraste de cohérence ne doit pas être confondu avec une interférence physique.

***

## 9. Limites explicites

Ce module ne prétend pas :

- démontrer l’émergence de la conscience ;
- démontrer une mémoire phénoménologique ;
- démontrer une holonomie biologique ;
- démontrer une théorie de jauge de l’esprit ;
- démontrer une physique quantique de la conscience.

Il construit une analogie structurelle entre :

- dynamique de champ ;
- régulation ;
- mémoire ;
- anticipation ;
- cohérence relationnelle.

$$
\boxed{
\text{Prototype}
\neq
\text{Démonstration}.
}
$$

$$
\boxed{
\text{Simulation}
\neq
\text{Explication}.
}
$$

***

## 10. La clôture

Le module de jauge sur le tore repose sur une séparation claire :

$$
\boxed{
A = A_0 + A_{\text{per}}.
}
$$

$$
\boxed{
\Phi = 2\pi\theta \pmod{2\pi}.
}
$$

$$
\boxed{
k_{\text{tordu}} = k - A_0.
}
$$

C’est cette séparation qui porte l’holonomie.

C’est cette séparation qui distingue le topologique du trivial.

C’est cette séparation qui constitue le cœur physique du module.

Citations :
[1] 1 Introduction https://arxiv.org/html/hep-th/9705137
[2] 1 Introduction https://arxiv.org/html/hep-th/0207277
[3] arXiv:hep-th/9406195v1  29 Jun 1994 https://arxiv.org/pdf/hep-th/9406195.pdf
[4] JHEP12(2017)056 https://link.springer.com/content/pdf/10.1007/JHEP12(2017)056.pdf?error=cookies_not_supported&code=ad068f2b-adee-4b72-9ec3-f9a959d2d581
[5] arXiv:hep-th/0103057v1  8 Mar 2001 http://arxiv.org/pdf/hep-th/0103057.pdf
[6] The Schrodinger Equation as a Gauge Theory https://arxiv.org/html/2604.26016
[7] arXiv:hep-th/0609203v1  28 Sep 2006 http://arxiv.org/pdf/hep-th/0609203.pdf
[8] Chern–Simons–Schrödinger theory on a one-dimensional lattice https://pelinovsky.mcmaster.ca/PaperBank/Discrete_CSS.pdf
[9] arXiv:1512.04684v2  [hep-th]  8 Jul 2016 http://arxiv.org/pdf/1512.04684.pdf
[10] 1Introduction https://ar5iv.labs.arxiv.org/html/hep-ph/9509417
[11] Revision 0df4c88a-7edd-4335-b56c-8e9966a8cb65 https://physics.stackexchange.com/revisions/0df4c88a-7edd-4335-b56c-8e9966a8cb65/view-source
[12] Revision addc3781-f29e-42e8-ad6f-7dd0acf6337b https://physics.stackexchange.com/revisions/addc3781-f29e-42e8-ad6f-7dd0acf6337b/view-source
[13] Contents https://ar5iv.labs.arxiv.org/html/1407.3789
[14] Revision a79ae70f-c9e3-445a-925d-7bf4c724d49e https://physics.stackexchange.com/revisions/a79ae70f-c9e3-445a-925d-7bf4c724d49e/view-source
