import numpy as np, networkx as nx
import compression_graphe_corrige as M
from compression_graphe_corrige import laplacien_graphe, compresser, N_NOEUDS, T
from compression_temoins import compresser_aleatoire
from balayage_mmin import une, step, sig, auc, spearman

rng_b = np.random.default_rng(12345)
def boot_auc(x, y, n=500):
    v=[]
    for _ in range(n):
        j = rng_b.integers(0, len(x), len(x)); a = auc(x[j], y[j])
        if not np.isnan(a): v.append(a)
    return (np.percentile(v,2.5), np.percentile(v,97.5)) if len(v)>50 else (np.nan,np.nan)

def seuil_par_lacune(d, lacune_min=1.0):
    s = np.sort(d); g = np.diff(s); i = np.argmax(g)
    return (0.5*(s[i]+s[i+1]), g[i]) if g[i] >= lacune_min else (None, g[i])

if __name__ == "__main__":
    print("=== A. Grille : seuil = milieu de la plus grande lacune de d_ret (lacune >= 1.0), IC95 bootstrap ===")
    print(f"{'D_I':>3} {'k':>3} | {'cond.':9s} {'seuil':>6} {'échecs':>7} {'AUC -m_min [IC95]':>22}")
    for DI in (1.0, 2.0, 4.0, 8.0):
        M.D_I = DI
        for k in (4, 6, 10, 14):
            res = [une(1000+s, k) for s in range(60)]
            for nom in ["pondérée","aléatoire"]:
                R = np.array([r[nom] for r in res]); mm, d = R[:,1], R[:,2]
                th, g = seuil_par_lacune(d)
                if th is None:
                    print(f"{DI:3.0f} {k:3d} | {nom:9s} {'-':>6} {'-':>7}   pas de bimodalité nette (lacune max {g:.2f})"); continue
                fail = (d>=th).astype(int)
                if fail.sum() < 5 or (1-fail).sum() < 5:
                    print(f"{DI:3.0f} {k:3d} | {nom:9s} {th:6.2f} {fail.sum():4d}/60   groupe trop petit (<5), AUC non calculée"); continue
                lo, hi = boot_auc(-mm, fail)
                print(f"{DI:3.0f} {k:3d} | {nom:9s} {th:6.2f} {fail.sum():4d}/60   {auc(-mm,fail):.2f} [{lo:.2f},{hi:.2f}]")

    print("\n=== B. Densité = degré du nœud dans A_c (D_I=4, k=10, 200 graines) ===")
    M.D_I = 4.0
    TEMPS = (0, 1, 5, 20, 50)
    def mean_sp(L):
        L = np.array([x for x in L if not np.isnan(x)])
        return (L.mean(), L.std(), len(L)) if len(L) else (np.nan, np.nan, 0)
    for nom in ["pondérée","aléatoire"]:
        sp_marge, sp_dev = [], {t: [] for t in TEMPS}; degs_var = []
        for seed in range(200):
            rng = np.random.default_rng(seed)
            A0 = nx.to_numpy_array(nx.random_regular_graph(10, N_NOEUDS, seed=seed)); Lp0 = laplacien_graphe(A0)
            F = rng.uniform(-.5,.5,N_NOEUDS); I = rng.uniform(-.5,.5,N_NOEUDS); B=(F+.5*I>0).astype(float)
            for _ in range(T): F,I,B = step(F,I,B,Lp0)
            F1,I1,_ = step(F,I,B,Lp0); refs = [(F.copy(),I.copy()), (F1,I1)]
            na = int(np.triu(A0,1).sum())
            Ac = compresser(A0,F,I, rng) if nom=="pondérée" else compresser_aleatoire(A0, na//2, rng)
            deg = Ac.sum(1); Lpc = laplacien_graphe(Ac); degs_var.append(deg.std())
            s = np.where(sig(F,I,B,Lp0)>=0,1.,-1.); m = s*sig(F,I,B,Lpc)
            sp_marge.append(spearman(deg, m))
            f,i,b = F.copy(),I.copy(),B.copy()
            for _ in range(T): f,i,b = step(f,i,b,Lpc)
            def dev(f,i):
                e = [np.sqrt((f-r[0])**2+(i-r[1])**2) for r in refs]
                return e[0] if np.linalg.norm(e[0])<=np.linalg.norm(e[1]) else e[1]
            traj = {0: dev(f,i)}
            for t in range(1, 201):
                f,i,b = step(f,i,b,Lp0)
                if t in TEMPS: traj[t] = dev(f,i)
            revenu = np.linalg.norm(dev(f,i)) < 1.0
            if revenu:
                for t in TEMPS: sp_dev[t].append(spearman(deg, traj[t]))
        mu, sd, n = mean_sp(sp_marge)
        print(f"\n[{nom}] écart-type du degré dans A_c, moyenne sur graines : {np.mean(degs_var):.2f}")
        print(f"  Spearman(degré, marge m_i) : moyenne {mu:+.2f} (sd {sd:.2f}, n={n} graines)")
        for t in TEMPS:
            mu, sd, n = mean_sp(sp_dev[t])
            lab = "fin compression" if t==0 else f"retour t={t}"
            print(f"  Spearman(degré, écart du nœud à la référence) à {lab:16s}: {mu:+.2f} (sd {sd:.2f}, n={n} graines revenues)")
