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
