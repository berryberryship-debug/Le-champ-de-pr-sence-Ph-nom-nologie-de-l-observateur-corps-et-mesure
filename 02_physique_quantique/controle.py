#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
moteur.py
=========

Le moteur d'exécution central.
Il encapsule le temps, l'état du système, et fournit des méthodes
pour faire avancer la simulation pas à pas, récupérer les métriques,
et exporter les résultats.
"""

import time
import json
import pandas as pd
from typing import Dict, Any, List

from champ import DynamiqueJaugeCovarianteExacte
from vacuite_holotelegraphique import SystemeHybrideUnifie

class MoteurSimulation:
    def __init__(self, config: Dict[str, Any] = None):
        """Initialise le moteur avec une configuration (ou les défauts)."""
        config = config or {}
        
        # 1. Initialisation du champ physique
        self.champ = DynamiqueJaugeCovarianteExacte(
            resolution=config.get("resolution", 512),
            flux_theta=config.get("flux_theta", 0.37),
            gamma=config.get("gamma", 0.0),
            coeff_courbure=config.get("courbure", 0.0),
            g_kerr=config.get("g_kerr", 1.0),
            graine=config.get("graine", 42)
        )
        
        # 2. Initialisation de la boucle de contrôle (RLS + Précision)
        self.systeme = SystemeHybrideUnifie(
            champ=self.champ,
            retroaction=config.get("retroaction", 0.2)
        )
        
        # 3. État interne du moteur
        self.temps_ecoule = 0.0
        self.pas_effectues = 0
        self.dt = config.get("dt", 0.01)
        self.historique: List[Dict[str, float]] = []
        
        print(f"[MOTEUR] Initialisé. Grille : {self.champ.N} points, L = {self.champ.L}.")

    def avancer_d_un_pas(self):
        """Fait avancer la simulation d'un seul pas de temps (dt)."""
        etat_courant = self.systeme.pas_temporel(self.dt)
        self.temps_ecoule += self.dt
        self.pas_effectues += 1
        self.historique.append(etat_courant)
        return etat_courant

    def run(self, nombre_de_pas: int, log_frequence: int = 50):
        """Lance le moteur pour N pas, avec un affichage périodique."""
        print(f"[MOTEUR] Démarrage du calcul pour {nombre_de_pas} pas (dt={self.dt})...")
        debut = time.time()
        
        for _ in range(nombre_de_pas):
            etat = self.avancer_d_un_pas()
            
            if self.pas_effectues % log_frequence == 0:
                print(f"  Pas {self.pas_effectues:04d} | t={self.temps_ecoule:.2f} | "
                      f"IPR={etat['ipr']:.5f} | Pi={etat['Pi']:.4f} | "
                      f"Erreur={etat['erreur_pred_rel']:.2e}")
                
        duree = time.time() - debut
        print(f"[MOTEUR] Terminé en {duree:.2f} secondes.")

    def obtenir_etat(self) -> Dict[str, Any]:
        """Retourne un dictionnaire complet de l'état actuel (physique et contrôle)."""
        if not self.historique:
            return {}
        
        dernier_etat = self.historique[-1]
        
        # On ajoute les données spatiales (pour faire des graphiques par exemple)
        return {
            "meta": {
                "temps": self.temps_ecoule,
                "pas": self.pas_effectues,
                "resolution": self.champ.N
            },
            "metriques": dernier_etat,
            "spatial": {
                "x": self.champ.x.tolist(),
                "densite": self.champ.densite().tolist(),
                "phase": self.champ.psi.tolist() # Attention, c'est complexe, on pourrait extraire juste l'angle
            }
        }

    def exporter_donnees(self, nom_fichier: str):
        """Exporte l'historique complet dans un fichier CSV."""
        if not self.historique:
            print("[MOTEUR] Rien à exporter.")
            return
            
        df = pd.DataFrame(self.historique)
        df.to_csv(nom_fichier, index=False)
        print(f"[MOTEUR] Historique complet exporté dans : {nom_fichier}")

    def sauvegarder_etat(self, nom_fichier: str):
        """Sauvegarde l'état complet (JSON) pour reprendre plus tard."""
        etat = self.obtenir_etat()
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            json.dump(etat, f, ensure_ascii=False, indent=2)
        print(f"[MOTEUR] État sauvegardé dans : {nom_fichier}")
