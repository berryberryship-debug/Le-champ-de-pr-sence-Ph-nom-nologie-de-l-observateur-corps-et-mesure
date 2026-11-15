"""
V13.2 (corrigé) — Rapport de participation (PR) des modes singuliers du Jacobien F-I-B,
avec deux contrôles et statistiques appariées.
 
Corrections par rapport à la V13.2 précédente :
  * conditions initiales de V8 (F=0, I dans ±0.2, B aléatoire) et temps jusqu'à 500 ;
  * substitut de Fourier à symétrie hermitienne et phase COMMUNE à F et I : spectres de F et de I,
    spectre croisé et normes ||F||, ||Lap F|| conservés exactement ;
  * B du substitut : densité conservée (--B-mode quantile, défaut) ou Θ(F+0.5I−S) (--B-mode theta) ;
  * comparaisons appariées par graine (moyenne, écart-type, IC95 bootstrap, taille d'effet, signes) ;
  * Jacobien vérifié contre les différences finies (--verif).
 
Ce que ça mesure : l'étalement spatial des modes les plus amplifiés / les plus contractés du
Jacobien (B figé). Pas la redondance de l'information.
 
Usage :
  python v13_2_holographie_PR.py --verif
  python v13_2_holographie_PR.py                         # L=21, 10 graines, t = 5, 100, 500
  python v13_2_holographie_PR.py --seeds 20 --B-mode theta
  (L=41 : SVD denses 3362x3362, très lent ; commencer par L=21)
"""
import argparse, csv, os
import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
 
ALPHA, BETA, G, D_I, GAMMA, SEUIL = 0.25, 0.05, 0.3, 4.0, 1.0, 0.0
 
 
def lap(Z):
    return np.roll(Z, 1, 0) + np.roll(Z, -1, 0) + np.roll(Z, 1, 1) + np.roll(Z, -1, 1) - 4.0 * Z
 
 
def pas_fib(F, I, B, D_F):
    Q = 2.0 * B - 1.0
    Fn = (1 - ALPHA) * F + ALPHA * np.tanh(I + G * Q + D_F * lap(F))
    In = (1 - BETA) * I + BETA * np.tanh(Fn + D_I * lap(I) - GAMMA * I ** 3)
    return Fn, In
 
 
def trajectoire(seed, L, D_F, temps):
    """Conditions initiales de V8 ; retourne {t: (F, I, B)} = état après t pas."""
    rng = np.random.RandomState(seed)
    I = rng.uniform(-0.2, 0.2, (L, L)); F = np.zeros((L, L)); B = rng.randint(0, 2, (L, L)).astype(float)
    out = {}
    for t in range(max(temps) + 1):
        if t in temps: out[t] = (F.copy(), I.copy(), B.copy())
        F, I = pas_fib(F, I, B, D_F)
        B = (F + 0.5 * I - SEUIL > 0).astype(float)
    return out
 
 
# ------------------------------------------------------------------ Jacobien
def matrice_laplacienne(L):
    N = L * L; idx = np.arange(N).reshape(L, L); rows, cols = [], []
    for s in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rows.append(idx.ravel()); cols.append(np.roll(idx, s, axis=(0, 1)).ravel())
    r, c = np.concatenate(rows), np.concatenate(cols)
    return sp.coo_matrix((np.ones(len(r)), (r, c)), shape=(N, N)).tocsr() - 4.0 * sp.identity(N, format='csr')
 
 
def jacobien(F, I, B, D_F):
    """J = d(F_{t+1}, I_{t+1}) / d(F_t, I_t), B_t figé (Θ non différentiable)."""
    L = F.shape[0]; N = L * L; Lp = matrice_laplacienne(L); Id = sp.identity(N, format='csr')
    a = I + G * (2 * B - 1) + D_F * lap(F)
    Fn = (1 - ALPHA) * F + ALPHA * np.tanh(a)
    b = Fn + D_I * lap(I) - GAMMA * I ** 3                    # F_{t+1}, pas F_t
    sa = sp.diags((1.0 / np.cosh(a) ** 2).ravel()); sb = sp.diags((1.0 / np.cosh(b) ** 2).ravel())
    dFF = (1 - ALPHA) * Id + ALPHA * D_F * (sa @ Lp)
    dFI = ALPHA * sa
    dIF = BETA * (sb @ dFF)
    dII = (1 - BETA) * Id + BETA * (sb @ (dFI + D_I * Lp - 3 * GAMMA * sp.diags((I ** 2).ravel())))
    return sp.bmat([[dFF, dFI], [dIF, dII]], format='csr')
 
 
def verif():
    L = 7; N = L * L; rng = np.random.default_rng(0)
    F = rng.uniform(-.5, .5, (L, L)); I = rng.uniform(-.5, .5, (L, L)); B = (F + .5 * I > 0).astype(float)
    for D_F in (0.0, 0.1, 0.4):
        Jf = np.zeros((2 * N, 2 * N)); eps = 1e-6
        for c in range(2 * N):
            dF = np.zeros(N); dI = np.zeros(N); (dF if c < N else dI)[c % N] = eps
            Fp, Ip = pas_fib(F + dF.reshape(L, L), I + dI.reshape(L, L), B, D_F)
            Fm, Im = pas_fib(F - dF.reshape(L, L), I - dI.reshape(L, L), B, D_F)
            Jf[:, c] = np.concatenate([(Fp - Fm).ravel(), (Ip - Im).ravel()]) / (2 * eps)
        Ja = jacobien(F, I, B, D_F).toarray()
        print(f"D_F={D_F}: erreur relative Frobenius = {np.linalg.norm(Ja - Jf) / np.linalg.norm(Jf):.2e}")
 
 
# ------------------------------------------------------------------ mesures
def pr(w):
    s1, s2 = np.sum(w), np.sum(w ** 2)
    return (s1 * s1) / s2 if s2 > 0 else np.nan
 
 
def mesures_PR(J, N, n_modes=5):
    _, s, Vt = la.svd(J.toarray(), full_matrices=False)
    poids = lambda v: v[:N] ** 2 + v[N:] ** 2
    hi = [pr(poids(v)) for v in Vt[:n_modes]]
    lo = [pr(poids(v)) for v in Vt[::-1][:n_modes]]
    kappa = np.inf if s[-1] < 1e-12 else s[0] / s[-1]
    return {'PR_top1': hi[0] / N, 'PR_top5': float(np.mean(hi)) / N,
            'PR_bot1': lo[0] / N, 'PR_bot5': float(np.mean(lo)) / N,
            'log10_kappa': float(np.log10(kappa)) if np.isfinite(kappa) else np.nan}
 
 
# ------------------------------------------------------------------ contrôles
def substitut_permutation(F, I, B, seed):
    p = np.random.RandomState(seed).permutation(F.size)
    return tuple(X.ravel()[p].reshape(F.shape) for X in (F, I, B))
 
 
def substitut_fourier(F, I, B, seed, mode='quantile'):
    """Même décalage de phase (hermitien) sur F et I : spectres, spectre croisé, ||F||, ||Lap F|| conservés."""
    L = F.shape[0]
    th = np.angle(np.fft.fft2(np.random.RandomState(seed).standard_normal((L, L)))); th[0, 0] = 0.0
    ph = np.exp(1j * th)
    Fs = np.real(np.fft.ifft2(np.fft.fft2(F) * ph)); Is = np.real(np.fft.ifft2(np.fft.fft2(I) * ph))
    S_sur = Fs + 0.5 * Is
    if mode == 'theta':
        Bs = (S_sur - SEUIL > 0).astype(float)
    else:                                                    # densité de B conservée
        d = float(B.mean())
        Bs = np.zeros_like(B) if d <= 0 else np.ones_like(B) if d >= 1 else (S_sur > np.quantile(S_sur, 1 - d)).astype(float)
    return Fs, Is, Bs
 
 
# ------------------------------------------------------------------ statistiques appariées
def stats_apparie(diff, n_boot=2000, seed=7):
    x = np.asarray(diff, float); x = x[np.isfinite(x)]; n = len(x)
    if n < 2: return dict(n=n, moy=np.nan, sd=np.nan, lo=np.nan, hi=np.nan, dz=np.nan, pos=0)
    rng = np.random.RandomState(seed)
    bm = np.sort([x[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
    sd = x.std(ddof=1)
    return dict(n=n, moy=x.mean(), sd=sd, lo=bm[int(0.025 * n_boot)], hi=bm[int(0.975 * n_boot) - 1],
                dz=x.mean() / sd if sd > 1e-12 else np.inf, pos=int((x > 0).sum()))
 
 
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--verif', action='store_true')
    ap.add_argument('--L', type=int, default=21)
    ap.add_argument('--seeds', type=int, default=10)
    ap.add_argument('--times', default='5,100,500')
    ap.add_argument('--D_F', type=float, default=0.1)
    ap.add_argument('--B-mode', choices=['quantile', 'theta'], default='quantile')
    ap.add_argument('--out', default='results/v13_2_pr.csv')
    a = ap.parse_args()
    if a.verif: verif(); return
 
    L = a.L; N = L * L; temps = tuple(int(t) for t in a.times.split(','))
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    print(f"L={L} (N={N}) | graines 0..{a.seeds-1} | D_F={a.D_F} | B-mode={a.B_mode}")
    mets = ['PR_top1', 'PR_top5', 'PR_bot1', 'PR_bot5', 'log10_kappa']
    lignes = []
    for s in range(a.seeds):
        traj = trajectoire(s, L, a.D_F, temps)
        for t in temps:
            F, I, B = traj[t]
            cas = {'dyn': (F, I, B),
                   'fourier': substitut_fourier(F, I, B, 2000 + s, a.B_mode),
                   'perm': substitut_permutation(F, I, B, 1000 + s)}
            for nom, (Fx, Ix, Bx) in cas.items():
                m = mesures_PR(jacobien(Fx, Ix, Bx, a.D_F), N)
                m.update(seed=s, t=t, cas=nom, densB=float(Bx.mean()), lapF=float(np.linalg.norm(lap(Fx))))
                lignes.append(m)
        print(f"  graine {s+1}/{a.seeds} faite", flush=True)
 
    with open(a.out, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['seed', 't', 'cas', 'densB', 'lapF'] + mets); w.writeheader(); w.writerows(lignes)
 
    for t in temps:
        sel = lambda cas: sorted([r for r in lignes if r['t'] == t and r['cas'] == cas], key=lambda r: r['seed'])
        d, fo, pe = sel('dyn'), sel('fourier'), sel('perm')
        print(f"\n=== t = {t} ===")
        print(f"densité B (moy) : dyn {np.mean([r['densB'] for r in d]):.3f} | fourier {np.mean([r['densB'] for r in fo]):.3f} "
              f"| perm {np.mean([r['densB'] for r in pe]):.3f}")
        print(f"||Lap F|| (moy) : dyn {np.mean([r['lapF'] for r in d]):.3f} | fourier {np.mean([r['lapF'] for r in fo]):.3f} "
              f"| perm {np.mean([r['lapF'] for r in pe]):.3f}")
        print(f"{'mesure':>12} | {'dyn':>7} | {'dyn-fourier [IC95] dz  +/n':>40} | {'dyn-perm [IC95] dz  +/n':>38}")
        for k in mets:
            vals = lambda rows: np.array([r[k] for r in rows])
            s1 = stats_apparie(vals(d) - vals(fo)); s2 = stats_apparie(vals(d) - vals(pe))
            fmt = lambda q: f"{q['moy']:+.3f} [{q['lo']:+.3f},{q['hi']:+.3f}] {q['dz']:+.2f} {q['pos']}/{q['n']}"
            print(f"{k:>12} | {np.nanmean(vals(d)):7.3f} | {fmt(s1):>40} | {fmt(s2):>38}")
    print(f"\nDétail par graine : {a.out}")
    print("Lecture : dyn-fourier ~ 0 (IC95 contenant 0) => l'étalement des modes est expliqué par les spectres. "
          "Le test ne mesure pas la redondance de l'information.")
 
 
if __name__ == "__main__":
    main()
 
