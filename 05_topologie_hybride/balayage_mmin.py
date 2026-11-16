import numpy as np, networkx as nx
import compression_graphe_corrige as M
from compression_graphe_corrige import laplacien_graphe, compresser, pas_fib_graphe, N_NOEUDS, T
from compression_temoins import compresser_aleatoire

SEUIL = 2.0

def step(F,I,B,Lp):
    F,I = pas_fib_graphe(F,I,B,Lp); return F,I,(F+.5*I>0).astype(float)

def sig(F,I,B,Lp):
    Fn,In = pas_fib_graphe(F,I,B,Lp); return Fn+.5*In

def auc(x,y):
    a,b = x[y==1], x[y==0]
    if len(a)==0 or len(b)==0: return np.nan
    return (np.sum(a[:,None]>b[None,:])+.5*np.sum(a[:,None]==b[None,:]))/(len(a)*len(b))

def rank(x): 
    r = np.empty(len(x)); r[np.argsort(x, kind="stable")] = np.arange(len(x)); return r

def spearman(x,y):
    if np.std(x)==0 or np.std(y)==0: return np.nan
    return np.corrcoef(rank(x), rank(y))[0,1]

def une(seed, k):
    rng = np.random.default_rng(seed)
    A0 = nx.to_numpy_array(nx.random_regular_graph(k, N_NOEUDS, seed=seed)); Lp0 = laplacien_graphe(A0)
    F = rng.uniform(-.5,.5,N_NOEUDS); I = rng.uniform(-.5,.5,N_NOEUDS); B=(F+.5*I>0).astype(float)
    
    # 1. Assemblage
    for _ in range(T): F,I,B = step(F,I,B,Lp0)
    
    # 2. Références (cycle de période 2)
    X0 = np.concatenate([F,I]); F1,I1,_ = step(F,I,B,Lp0); X1 = np.concatenate([F1,I1])
    
    na = int(np.triu(A0,1).sum()); out = {}
    
    # 3. Compressions
    Ac_pond = compresser(A0,F,I,rng)
    Ac_alea = compresser_aleatoire(A0, na//2, rng)
    
    for nom, Ac in {"pondérée": Ac_pond, "aléatoire": Ac_alea}.items():
        Lpc = laplacien_graphe(Ac)
        
        # 4. Prédicteur A Priori
        s = np.where(sig(F,I,B,Lp0)>=0,1.,-1.); m = s*sig(F,I,B,Lpc)
        
        # 5. Évolution (compression puis retour)
        f,i,b = F.copy(),I.copy(),B.copy()
        for _ in range(T): f,i,b = step(f,i,b,Lpc)
        for _ in range(200): f,i,b = step(f,i,b,Lp0)
        
        X = np.concatenate([f,i])
        
        # 6. Mesure
        d_ret = min(np.linalg.norm(X-X0), np.linalg.norm(X-X1))
        out[nom] = (float(np.mean(m<=0)), float(m.min()), d_ret)
        
    return out

# Le bloc ci-dessous ne s'exécute QUE si tu lances "python balayage_mmin.py" directement.
# Il ne tournera PAS quand les autres scripts l'importeront.
if __name__ == "__main__":
    print("Test de base de balayage_mmin.py...")
    M.D_I = 4.0
    res = [une(s, 10) for s in range(5)]
    for r in res:
        print(r)
