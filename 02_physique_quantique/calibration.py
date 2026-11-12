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
