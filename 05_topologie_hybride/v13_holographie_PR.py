"""
v13 — Rapport de participation (PR) des modes singuliers du Jacobien F-I-B.
Compare la dynamique à deux contrôles (permutation et Fourier) pour tester
si la structure spatiale étale les modes.
"""
import numpy as np
import time
from fib_core import pas_fib, SEUIL

# On réutilise le jacobien analytique de v11
from v11_full_audit import jacobien_analytique_global

L = 21
N = L * L

def trajectoire(seed, D_F, temps):
    """Génère l'état (F, I, B) à des temps spécifiques."""
    rng = np.random.default_rng(seed)
    F = rng.uniform(-0.5, 0.5, (L, L))
    I = rng.uniform(-0.5, 0.5, (L, L))
    B = (F + 0.5 * I > SEUIL).astype(float)
    
    out = {}
    tmax = max(temps)
    
    for t in range(tmax + 1):
        if t in temps:
            out[t] = (F.copy(), I.copy(), B.copy())
            
        Fn, In = pas_fib(F, I, B, D_F)
        Bn = (Fn + 0.5 * In > SEUIL).astype(float)
        F, I, B = Fn, In, Bn
        
    return out

def pr(w):
    """Participation Ratio (1 = localisé, N = uniforme)."""
    s2 = np.sum(w)
    s4 = np.sum(w ** 2)
    return (s2 * s2) / s4 if s4 > 0 else np.nan

def mesures_PR(J, m=5):
    """Calcule kappa et le PR des modes singuliers dominants."""
    U, sv, Vt = np.linalg.svd(J.toarray(), full_matrices=False)
    
    def poids(v):
        return v[:N] ** 2 + v[N:] ** 2  # Poids par site
        
    return {
        'kappa': sv[0] / sv[-1],
        'PR_top1': pr(poids(Vt[0])),
        'PR_top5': np.mean([pr(poids(Vt[i])) for i in range(m)]),
        'PR_bot1': pr(poids(Vt[-1]))
    }

def substitut_fourier(F, I, seed):
    """Contrôle : préserve les spectres mais randomise les phases."""
    th = np.angle(np.fft.fft2(np.random.default_rng(seed).standard_normal((L, L))))
    th[0, 0] = 0.0
    ph = np.exp(1j * th)
    Fs = np.real(np.fft.ifft2(np.fft.fft2(F) * ph))
    Is = np.real(np.fft.ifft2(np.fft.fft2(I) * ph))
    Bs = (Fs + 0.5 * Is > SEUIL).astype(float)
    return Fs, Is, Bs

if __name__ == "__main__":
    print(f"L={L} (N={N})")
    print(f"{'Cas':>12} | {'t':>4} | {'PR_top1/N':>9} | {'PR_top5/N':>9} | {'PR_bot1/N':>9} | {'kappa':>8}")
    print("-" * 70)
    
    D_F = 0.1
    n_seeds = 3
    temps = [5, 100]  # Un temps précoce (transitoire) et un temps tardif (structuré)
    
    for t in temps:
        res = {'dynamique': [], 'permuté': [], 'fourier': []}
        
        for s in range(n_seeds):
            etats = trajectoire(s, D_F, temps)
            F, I, B = etats[t]
            
            # 1. Dynamique réelle
            J_dyn = jacobien_analytique_global(F, I, B, D_F)
            res['dynamique'].append(mesures_PR(J_dyn))
            
            # 2. Permutation spatiale
            p = np.random.default_rng(1000 + s).permutation(N)
            Fp, Ip, Bp = (X.ravel()[p].reshape(L, L) for X in (F, I, B))
            J_perm = jacobien_analytique_global(Fp, Ip, Bp, D_F)
            res['permuté'].append(mesures_PR(J_perm))
            
            # 3. Substitut de Fourier
            Ff, If, Bf = substitut_fourier(F, I, 2000 + s)
            J_four = jacobien_analytique_global(Ff, If, Bf, D_F)
            res['fourier'].append(mesures_PR(J_four))
            
        for cas, rows in res.items():
            m = {k: np.mean([r[k] for r in rows]) for k in rows[0]}
            print(f"{cas:>12} | {t:4d} | {m['PR_top1']/N:9.3f} | {m['PR_top5']/N:9.3f} | {m['PR_bot1']/N:9.3f} | {m['kappa']:8.2f}")
        print("-" * 70)
