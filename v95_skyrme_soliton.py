#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
V95 — Soliton de Skyrme (Ansatz Hedgehog, B = 1)
Résolution numérique du profil radial F(r) et vérification de la densité d'énergie
complète (terme quadratique + terme quartique stabilisant de Skyrme).

Statut épistémique : modèle mathématique et numérique classique de théorie des champs.
Sert d'illustration formelle de stabilisation par invariant topologique ; ne constitue
pas une mesure empirique de la conscience ni du volume subjectif V_psi.
"""

import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt


# ==========================================
# 1. ÉQUATION DIFFÉRENTIELLE DE SKYRME
# ==========================================
def skyrme_ode(r, y):
    """
    y[0] = F(r), y[1] = F'(r)

    Équation d'Euler-Lagrange :

      (r^2 + 2 sin^2 F) F''
      + 2 r F'
      + sin(2F) [ (F')^2 - 1 - sin^2(F)/r^2 ]
      = 0
    """
    F = y[0]
    dF = y[1]

    sin2F = np.sin(2.0 * F)
    sin_sq = np.sin(F) ** 2

    num = (
        -2.0 * r * dF
        - sin2F * (
            dF ** 2
            - 1.0
            - sin_sq / (r ** 2)
        )
    )

    den = (
        r ** 2
        + 2.0 * sin_sq
    )

    d2F = num / den

    return np.vstack(
        (
            dF,
            d2F,
        )
    )


def bc(ya, yb):
    """
    Conditions aux limites :

        F(r_min) = pi
        F(r_max) = 0
    """
    return np.array(
        [
            ya[0] - np.pi,
            yb[0] - 0.0,
        ]
    )


# ==========================================
# 2. RÉSOLUTION NUMÉRIQUE
# ==========================================
r = np.linspace(
    1e-5,
    15.0,
    600,
)

F_guess = (
    np.pi
    * 0.5
    * (
        1.0
        - np.tanh(r - 2.0)
    )
)

dF_guess = np.gradient(
    F_guess,
    r,
)

y_guess = np.vstack(
    (
        F_guess,
        dF_guess,
    )
)

print(
    "Résolution de l'équation de Skyrme (B=1)..."
)

sol = solve_bvp(
    skyrme_ode,
    bc,
    r,
    y_guess,
    tol=1e-7,
    max_nodes=3000,
)

if not sol.success:
    raise RuntimeError(
        "Échec de la convergence du solveur BVP : "
        f"{sol.message}"
    )

F_sol = sol.sol(r)[0]
dF_sol = sol.sol(r)[1]


# ==========================================
# 3. CHARGE TOPOLOGIQUE & ÉNERGIE TOTALE
# ==========================================
B_boundary = (
    F_sol[0]
    - F_sol[-1]
) / np.pi

B_integral = (
    -2.0
    / np.pi
    * np.trapezoid(
        (
            np.sin(F_sol) ** 2
        )
        * dF_sol,
        r,
    )
)

# Densité radiale complète E(r) telle que :
#
#     E_tot = 4 * pi * int E(r) dr
#
sin_sq = np.sin(F_sol) ** 2

e_quad = (
    (r ** 2)
    * (dF_sol ** 2)
    + 2.0 * sin_sq
)

e_quart = (
    2.0
    * sin_sq
    * (dF_sol ** 2)
    + (
        sin_sq ** 2
    )
    / (r ** 2)
)

energy_density = (
    e_quad
    + e_quart
)

E_total = (
    4.0
    * np.pi
    * np.trapezoid(
        energy_density,
        r,
    )
)

bogomolny_ratio = (
    E_total
    / (
        12.0
        * (np.pi ** 2)
    )
)

print(
    "Charge topologique (bornes)    : "
    f"B = {B_boundary:.6f}"
)

print(
    "Charge topologique (intégrale) : "
    f"B = {B_integral:.6f}"
)

print(
    "Rapport énergie / borne 12π²   : "
    f"E / (12π²) = {bogomolny_ratio:.4f} "
    "(attendu ~ 1.232)"
)


# ==========================================
# 4. GRAPHIQUES
# ==========================================
fig, axs = plt.subplots(
    1,
    3,
    figsize=(15, 4),
)

axs[0].plot(
    r,
    F_sol,
    color="blue",
    linewidth=2,
)

axs[0].axhline(
    np.pi,
    color="red",
    linestyle="--",
    label="F(0) = π",
)

axs[0].axhline(
    0.0,
    color="green",
    linestyle="--",
    label="F(∞) = 0",
)

axs[0].set_title(
    "Profil radial F(r)"
)

axs[0].set_xlabel(
    "r"
)

axs[0].set_ylabel(
    "F(r)"
)

axs[0].legend()
axs[0].grid(
    True,
    alpha=0.3,
)


axs[1].plot(
    r,
    dF_sol,
    color="purple",
    linewidth=2,
)

axs[1].set_title(
    "Dérivée F'(r)"
)

axs[1].set_xlabel(
    "r"
)

axs[1].set_ylabel(
    "F'(r)"
)

axs[1].grid(
    True,
    alpha=0.3,
)


axs[2].plot(
    r,
    energy_density,
    color="orange",
    linewidth=2,
    label="Totale (quad. + quart.)",
)

axs[2].plot(
    r,
    e_quad,
    color="gray",
    linestyle=":",
    linewidth=1.3,
    label="Quadratique seule",
)

axs[2].fill_between(
    r,
    energy_density,
    alpha=0.25,
    color="orange",
)

axs[2].set_title(
    "Densité radiale d'énergie "
    f"(E/12π² = {bogomolny_ratio:.3f})"
)

axs[2].set_xlabel(
    "r"
)

axs[2].set_ylabel(
    "E(r)"
)

axs[2].legend()
axs[2].grid(
    True,
    alpha=0.3,
)


plt.tight_layout()

plt.savefig(
    "v95_skyrme_soliton.png",
    dpi=300,
)

plt.close(
    fig
)

print(
    "Figure sauvegardée : "
    "v95_skyrme_soliton.png"
)
