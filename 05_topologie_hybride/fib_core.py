"""
fib_core.py — Noyau du système F-I-B.
Ce fichier centralise les constantes et les équations fondamentales.
Tous les scripts d'expérience (v9, v11, v12, v13) doivent importer depuis ici
pour garantir que les corrections sont appliquées partout.
"""

import numpy as np

# =========================================================
# CONSTANTES GLOBALES
# =========================================================
ALPHA = 0.25
BETA  = 0.05
G     = 0.3
D_I   = 4.0
GAMMA = 1.0
SEUIL = 0.0

# Taille par défaut (peut être écrasée par les scripts)
L_DEFAULT = 41

def lap(Z):
    """
    Laplacien discret avec conditions aux limites périodiques.
    """
    return (
        np.roll(Z, 1, 0) + np.roll(Z, -1, 0)
        + np.roll(Z, 1, 1) + np.roll(Z, -1, 1)
        - 4.0 * Z
    )

def pas_fib(F, I, B, D_F):
    """
    Un pas de la dynamique F-I-B.
    B est traité comme une entrée fixe.
    """
    Q = 2.0 * B - 1.0
    
    # Mise à jour de F
    Fn = (1.0 - ALPHA) * F + ALPHA * np.tanh(I + G * Q + D_F * lap(F))
    
    # Mise à jour de I (dépend du nouveau Fn)
    In = (1.0 - BETA) * I + BETA * np.tanh(Fn + D_I * lap(I) - GAMMA * I**3)
    
    return Fn, In
