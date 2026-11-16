import numpy as np
import networkx as nx
from compression_graphe_corrige import (
    laplacien_graphe, compresser, pas_fib_graphe, N_NOEUDS, K_VOISINS, T
)
from compression_temoins import compresser_aleatoire

def step(F, I, B, Lp):
    Fn, In = pas_fib_graphe(F, I, B, Lp)
    return Fn, In, (Fn + 0.5 * In > 0).astype(float)

def a_priori(F, I, B, Lp0, Lpc):
    """Prédicteur instantané : inversions de signe après un pas de compression."""
    def sig(Lp):
        Fn, In = pas_fib_graphe(F, I, B, Lp)
        return Fn + 0.5 * In
    
    s0 = sig(Lp0)
    sc = sig(Lpc)
    
    signe_ref = np.where(s0 >= 0, 1.0, -1.0)
    m_i = signe_ref * sc
    
    return float(np.mean(m_i <= 0)), float(m_i.min())

def auc(x, y):
    a, b = x[y == 1], x[y == 0]
    if len(a) == 0 or len(b) == 0: return np.nan
    return (np.sum(a[:, None] > b[None, :]) + 0.5 * np.sum(a[:, None] == b[None, :])) / (len(a) * len(b))

def bootstrap_auc(x, y, n_boot=1000, seed=42):
    """Estime l'IC à 95% de l'AUC par bootstrap sur les graines."""
    rng = np.random.default_rng(seed)
    n = len(x)
    aucs = []
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        if len(np.unique(y[idx])) < 2: continue
        aucs.append(auc(x[idx], y[idx]))
    return np.percentile(aucs, [2.5, 97.5]) if aucs else [np.nan, np.nan]

def une_graine(seed):
    # SÉPARATION DES RNG
    rng_init = np.random.default_rng(seed)
    rng_pond = np.random.default_rng(seed + 10000)
    rng_alea = np.random.default_rng(seed + 20000)
    
    A0 = nx.to_numpy_array(nx.random_regular_graph(K_VOISINS, N_NOEUDS, seed=seed))
    Lp0 = laplacien_graphe(A0)
    
    F = rng_init.uniform(-0.5, 0.5, N_NOEUDS)
    I = rng_init.uniform(-0.5, 0.5, N_NOEUDS)
    B = (F + 0.5 * I > 0).astype(float)
    
    # Assemblage
    for _ in range(T):
        F, I, B = step(F, I, B, Lp0)
        
    # Références (2 phases du cycle)
    F_ref, I_ref, B_ref = F.copy(), I.copy(), B.copy()
    F1, I1, _ = step(F_ref, I_ref, B_ref, Lp0)
    X0 = np.concatenate([F_ref, I_ref])
    X1 = np.concatenate([F1, I1])
    
    na_total = int(np.triu(A0, 1).sum())
    na_comp = na_total // 2  # 50% des arêtes retirées
    
    out = {}
    
    # On prépare les deux compressions
    Ac_pond = compresser(A0, F_ref, I_ref, rng_pond, q=50)
    Ac_alea = compresser_aleatoire(A0, na_comp, rng_alea)
    
    for nom, Ac in {"pondérée": Ac_pond, "aléatoire": Ac_alea}.items():
        # Vérification de sécurité
        assert int(np.triu(Ac, 1).sum()) == na_comp, f"Mauvais nombre d'arêtes dans {nom}"
        
        Lpc = laplacien_graphe(Ac)
        rho, mmin = a_priori(F_ref, I_ref, B_ref, Lp0, Lpc)
        
        # Phase compressée
        f, i, b = F_ref.copy(), I_ref.copy(), B_ref.copy()
        for _ in range(T):
            f, i, b = step(f, i, b, Lpc)
            
        # Phase de retour (décompression = retour à Lp0)
        for _ in range(200):
            f, i, b = step(f, i, b, Lp0)
            
        X = np.concatenate([f, i])
        
        d0 = np.linalg.norm(X - X0)
        d1 = np.linalg.norm(X - X1)
        d_ret = min(d0, d1)
        
        out[nom] = (rho, mmin, d_ret, d0, d1)
    return out

if __name__ == "__main__":
    NS = 200
    print(f"Simulation sur {NS} graines (cela peut prendre quelques minutes)...")
    res = [une_graine(s) for s in range(NS)]
    
    print(f"\n{'Condition':10s} | {'Bloc':15s} | {'Échecs':6s} | {'AUC rho [IC95]':22s} | {'AUC -mmin [IC95]':22s}")
    print("-" * 85)
    
    for nom in ["pondérée", "aléatoire"]:
        for lab, sl in [("0-99 (Train)", slice(0, 100)), ("100-199 (Test)", slice(100, 200))]:
            R = np.array([r[nom] for r in res[sl]])
            rho, mmin, d_ret = R[:, 0], R[:, 1], R[:, 2]
            echec = (d_ret >= 2.0).astype(int)
            
            auc_rho = auc(rho, echec)
            ic_rho = bootstrap_auc(rho, echec)
            
            auc_mmin = auc(-mmin, echec)
            ic_mmin = bootstrap_auc(-mmin, echec)
            
            print(f"{nom:10s} | {lab:15s} | {echec.sum():3d}/100 | {auc_rho:.2f} [{ic_rho[0]:.2f},{ic_rho[1]:.2f}] | {auc_mmin:.2f} [{ic_mmin[0]:.2f},{ic_mmin[1]:.2f}]")

    # Comparaison globale
    print("\n--- Comparaison Globale ---")
    for nom in ["pondérée", "aléatoire"]:
        R = np.array([r[nom] for r in res])
        echec = (R[:, 2] >= 2.0).astype(int)
        print(f"{nom:10s} : Échecs globaux = {echec.sum()}/{NS} | Corr(rho, d_ret) = {np.corrcoef(R[:,0], R[:,2])[0,1]:+.3f}")
