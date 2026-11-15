import numpy as np
import scipy.sparse as sp
import time
from fib_core import lap, ALPHA, BETA, G, D_I, GAMMA, SEUIL

def matrice_laplacienne(L):
    N = L * L
    idx = np.arange(N).reshape(L, L)
    rows, cols = [], []
    for s in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rows.append(idx.ravel())
        cols.append(np.roll(idx, s, axis=(0, 1)).ravel())
    r, c = np.concatenate(rows), np.concatenate(cols)
    return sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(N, N)).tocsr() - 4.0 * sp.identity(N, format='csr')

def jacobien_analytique_global(F, I, B, D_F):
    """Jacobien global creux (référence exacte, sous hypothèse B fixe)."""
    L = F.shape[0]; N = L * L
    Lp = matrice_laplacienne(L)
    Id = sp.identity(N, format='csr')
    
    a = I + G * (2 * B - 1) + D_F * lap(F)
    Fn = (1 - ALPHA) * F + ALPHA * np.tanh(a)
    b = Fn + D_I * lap(I) - GAMMA * I ** 3
    
    sa = sp.diags((1.0 / np.cosh(a) ** 2).ravel())
    sb = sp.diags((1.0 / np.cosh(b) ** 2).ravel())
    
    dFF = (1 - ALPHA) * Id + ALPHA * D_F * (sa @ Lp)
    dFI = ALPHA * sa
    dIF = BETA * (sb @ dFF)
    dII = (1 - BETA) * Id + BETA * (sb @ (dFI + D_I * Lp - 3 * GAMMA * sp.diags((I ** 2).ravel())))
    
    return sp.bmat([[dFF, dFI], [dIF, dII]], format='csr')

def mesurer_deformation(J):
    """Calcule l'anisotropie et la contraction volumique."""
    J_dense = J.toarray()
    
    # Anisotropie
    sv = np.linalg.svd(J_dense, compute_uv=False)
    kappa = sv[0] / sv[-1] if sv[-1] > 0 else np.inf
    
    # Contraction
    sign, logdet = np.linalg.slogdet(J_dense)
    
    return kappa, logdet

def balayage_D_F(D_F_values, n_realisations=3, L=21, seed=42):
    N = L * L
    rng = np.random.default_rng(seed)
    
    print(f"\n=== BALAYAGE D_F (L={L}, {n_realisations} réalisations) ===")
    print(f"{'D_F':>6} | {'kappa (moy)':>12} | {'logdet(J)':>12}")
    print("-" * 40)
    
    for D_F in D_F_values:
        kappas, logdets = [], []
        for _ in range(n_realisations):
            F = rng.uniform(-0.5, 0.5, (L, L))
            I = rng.uniform(-0.5, 0.5, (L, L))
            B = (F + 0.5 * I > SEUIL).astype(float)
            
            J = jacobien_analytique_global(F, I, B, D_F)
            k, ld = mesurer_deformation(J)
            kappas.append(k)
            logdets.append(ld)
            
        print(f"{D_F:6.3f} | {np.mean(kappas):12.4f} | {np.mean(logdets):12.4f}")

if __name__ == "__main__":
    t0 = time.time()
    # On teste D_F de 0 (pas de diffusion) à 0.8 (forte diffusion)
    valeurs = [0.0, 0.05, 0.1, 0.2, 0.4, 0.8]
    balayage_D_F(valeurs, n_realisations=2, L=21)
    print(f"\nTemps de calcul : {time.time() - t0:.1f} s")
