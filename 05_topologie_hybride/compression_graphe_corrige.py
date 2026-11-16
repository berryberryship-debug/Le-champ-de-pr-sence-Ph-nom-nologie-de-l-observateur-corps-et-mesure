import numpy as np
import networkx as nx

N_NOEUDS, K_VOISINS = 100, 10
ALPHA, BETA, G, D_I, GAMMA = 0.25, 0.05, 0.3, 4.0, 1.0
D_F = 0.1
T = 50

def laplacien_graphe(A):
    return np.diag(A.sum(axis=1)) - A

def pas_fib_graphe(F, I, B, Lp):
    Q = 2.0 * B - 1.0
    Fn = (1 - ALPHA) * F + ALPHA * np.tanh(I + G * Q - D_F * (Lp @ F))
    In = (1 - BETA) * I + BETA * np.tanh(Fn - D_I * (Lp @ I) - GAMMA * I**3)
    return Fn, In

def compresser(A, F, I, rng, q=50):
    iu = np.array(np.nonzero(np.triu(A, 1))).T
    if len(iu) == 0: return np.zeros_like(A)
    W = np.abs(F[iu[:, 0]] * F[iu[:, 1]] + I[iu[:, 0]] * I[iu[:, 1]])
    n_aretes = max(1, int(round(len(iu) * (100 - q) / 100)))
    n_aretes = min(n_aretes, len(iu))
    indices = np.argsort(W, kind="stable")[-n_aretes:]
    choix = iu[indices]
    Ac = np.zeros_like(A)
    Ac[choix[:, 0], choix[:, 1]] = 1
    Ac[choix[:, 1], choix[:, 0]] = 1
    return Ac
