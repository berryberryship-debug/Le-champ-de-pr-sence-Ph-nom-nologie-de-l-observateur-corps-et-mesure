"""
V8 — Réplication indépendante du calcul de winding.
Compare l'algorithme A (BFS) et B (NetworkX) sur les mêmes champs.
"""
import csv
import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.dynamics import simuler
from src.topology.winding import classe_4_8 as classe_A
from src.topology.bcs_independent import analyse_rang_networkx

CSV_IN = 'v719_resultats.csv'
CSV_OUT = 'results/v8_replication.csv'
D_I = 4.0

os.makedirs('results', exist_ok=True)

def classe_B(Bm):
    return (
        analyse_rang_networkx(Bm, 1, 4),
        analyse_rang_networkx(1 - Bm, 1, 8),
    )

graines = []
degen_count = 0
try:
    with open(CSV_IN) as f:
        for row in csv.DictReader(f):
            if int(row['degen']) == 1 or row['sig_star'] == '':
                degen_count += 1
                continue
            graines.append({
                'seed': int(row['seed']),
                'rho': float(row['rho']),
                'cls_csv_rmaj': int(row['cls_rmaj']),
                'cls_csv_rmin': int(row['cls_rmin']),
            })
except FileNotFoundError:
    print(f"Fichier {CSV_IN} introuvable. Assurez-vous d'être à la racine du projet.")
    sys.exit(1)

print(f"Graines lues dans le CSV : {len(graines)} valides ({degen_count} ignorées)")
print("Recalcul des simulations + double analyse topologique...")

rows_out = []
n_diff_AB = 0
n_incoherence_csv = 0
n_nonzero_A = 0
n_nonzero_B = 0
n_A_2 = 0
n_B_2 = 0

for i, g in enumerate(graines):
    if (i + 1) % 20 == 0:
        print(f"  {i+1}/{len(graines)}...")

    B = np.asarray(simuler(g['seed'], D_I)).astype(int)
    p = B.mean()
    Bm = B if p >= 0.5 else 1 - B

    recalcul_A = classe_A(Bm)
    cls_B = classe_B(Bm)
    
    diff_AB = int(recalcul_A != cls_B)
    cls_csv = (g['cls_csv_rmaj'], g['cls_csv_rmin'])
    incoherence = int(recalcul_A != cls_csv)

    if diff_AB: n_diff_AB += 1
    if incoherence: n_incoherence_csv += 1
    
    if recalcul_A[0] > 0 or recalcul_A[1] > 0: n_nonzero_A += 1
    if cls_B[0] > 0 or cls_B[1] > 0: n_nonzero_B += 1
    
    if recalcul_A == (2, 0): n_A_2 += 1
    if cls_B == (2, 0): n_B_2 += 1

    rows_out.append({
        'seed': g['seed'],
        'rho': f"{g['rho']:.4f}",
        'A_rmaj': recalcul_A[0], 'A_rmin': recalcul_A[1],
        'B_rmaj': cls_B[0], 'B_rmin': cls_B[1],
        'diff_AB': diff_AB,
        'coherence_CSV': int(not incoherence),
    })

with open(CSV_OUT, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=rows_out[0].keys())
    w.writeheader()
    w.writerows(rows_out)

print(f"\n--- Résumé ---")
print(f"Graines traitées                : {len(rows_out)}")
print(f"Divergences A vs B              : {n_diff_AB}")
print(f"Incohérences CSV vs Recalcul A  : {n_incoherence_csv}")
print(f"Graines avec rang>0 en A        : {n_nonzero_A}")
print(f"Graines avec rang>0 en B        : {n_nonzero_B}")
print(f"Graines avec classe (2,0) en A  : {n_A_2}")
print(f"Graines avec classe (2,0) en B  : {n_B_2}")
print(f"\nFichier exporté : {CSV_OUT}")
