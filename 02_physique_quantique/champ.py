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
