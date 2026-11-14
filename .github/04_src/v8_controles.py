import os, sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.topology.winding import analyse_rang as A
from src.topology.bcs_independent import analyse_rang_networkx as B

CAS = ((1, 4), (0, 8))
for L in (41, 61):
    print(f"\n=== TAILLE L = {L} ===")
    print(f"{'p':>5} {'cas':>9} {'champs':>7} {'diverg':>7} {'rang>0':>7}")
    for p in (0.50, 0.55, 0.58, 0.59, 0.60, 0.62, 0.70):
        for val, conn in CAS:
            n = div = nz = 0
            for s in range(50):
                M = (np.random.default_rng(s).random((L, L)) < p).astype(int)
                a, b = A(M, val, conn, L), B(M, val, conn, L)
                n += 1; div += (a != b); nz += (a > 0)
            print(f"{p:>5} {str((val,conn)):>9} {n:>7} {div:>7} {nz:>7}")
