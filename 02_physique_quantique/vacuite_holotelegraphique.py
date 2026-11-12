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
