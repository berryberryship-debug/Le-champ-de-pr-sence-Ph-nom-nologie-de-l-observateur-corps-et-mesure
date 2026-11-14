import numpy as np
import sys, os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.topology.winding import analyse_rang as analyse_A
from src.topology.bcs_independent import analyse_rang_networkx as analyse_B

L = 41

def test_carre():
    B = np.zeros((L, L), dtype=int); B[15:25, 15:25] = 1
    assert analyse_A(B, 1, 4) == 0
    assert analyse_B(B, 1, 4) == 0

def test_bande_horizontale():
    B = np.zeros((L, L), dtype=int); B[15:25, :] = 1
    assert analyse_A(B, 1, 4) == 1
    assert analyse_B(B, 1, 4) == 1

def test_grille_pleine():
    B = np.ones((L, L), dtype=int)
    assert analyse_A(B, 1, 4) == 2
    assert analyse_B(B, 1, 4) == 2

def test_deux_bandes_paralleles():
    B = np.zeros((L, L), dtype=int)
    B[5:8, :] = 1; B[25:28, :] = 1
    assert analyse_A(B, 1, 4) == 1
    assert analyse_B(B, 1, 4) == 1

@pytest.mark.parametrize("p", [0.55, 0.60, 0.65, 0.70])
@pytest.mark.parametrize("graine", range(20))
def test_comparaison_aleatoire(p, graine):
    B = (np.random.default_rng(graine).random((L, L)) < p).astype(int)
    for v in (0, 1):
        assert analyse_A(B, v, 4) == analyse_B(B, v, 4), \
            f"A≠B à p={p}, graine={graine}, val={v}"

def test_comparaison_aleatoire_connexite8():
    B = (np.random.default_rng(1).random((L, L)) < 0.7).astype(int)
    for v in (0, 1):
        assert analyse_A(B, v, 8) == analyse_B(B, v, 8)
