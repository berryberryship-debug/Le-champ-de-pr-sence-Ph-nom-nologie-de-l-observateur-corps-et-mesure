from __future__ import annotations

import numpy as np
from scipy.special import ive

EPSILON = 1e-12


def normaliser_L2(champ: np.ndarray, dx: float, cible: float = 1.0) -> np.ndarray:
    """Normalise un champ pour que ∫|ψ|² dx = cible."""
    champ = np.asarray(champ)

    if not np.all(np.isfinite(champ)):
        raise ValueError("Champ non fini (NaN ou inf).")

    norme2 = float(np.sum(np.abs(champ) ** 2) * dx)

    if norme2 <= 1e-30:
        raise ValueError("Norme du champ quasi nulle.")

    return champ * np.sqrt(cible / norme2)


def plancher_lisse(
    valeurs: np.ndarray,
    seuil: float = 0.01,
    largeur: float = 0.01,
) -> np.ndarray:
    """Plancher lisse évitant les valeurs nulles ou négatives."""
    valeurs = np.asarray(valeurs)
    return seuil + largeur * np.logaddexp(
        (valeurs - seuil) / largeur,
        0.0,
    )


def kappa_bessel(x):
    """Rapport de concentration circulaire kappa(x) = I1(x) / I0(x)."""
    x = np.maximum(x, EPSILON)
    return ive(1, x) / np.maximum(ive(0, x), 1e-300)


def inverser_kappa_newton(
    target: float,
    tol: float = 1e-10,
    max_iter: int = 50,
) -> float:
    """Résout kappa(x) = target par Newton, puis dichotomie."""
    target = float(np.clip(target, 1e-6, 0.999))
    x = 1.0

    for _ in range(max_iter):
        k = float(kappa_bessel(x))
        diff = k - target

        if abs(diff) < tol:
            return x

        dk = max(1.0 - k / x - k * k, 1e-10)
        x = max(x - diff / dk, 1e-8)

    bas, haut = 1e-9, 1e4

    for _ in range(200):
        milieu = 0.5 * (bas + haut)

        if float(kappa_bessel(milieu)) < target:
            bas = milieu
        else:
            haut = milieu

    return 0.5 * (bas + haut)
