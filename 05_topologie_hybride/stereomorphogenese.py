import numpy as np
import compression_graphe_corrige as M
from compression_graphe_corrige import laplacien_graphe, compresser, N_NOEUDS, T
from compression_temoins import compresser_aleatoire
from balayage_mmin import step, spearman

K_KNN, LAMBDA, SEUIL = 10, 0.6, 2.0

def knn_graph(P, k=K_KNN):
    D = np.linalg.norm(P[:,None]-P[None], axis=2); np.fill_diagonal(D, np.inf)
    A = np.zeros((len(P), len(P)))
    for i in range(len(P)): A[i, np.argsort(D[i])[:k]] = 1
    return np.maximum(A, A.T)

def longueur_moy(P, A):
    iu = np.triu(A,1)>0; D = np.linalg.norm(P[:,None]-P[None], axis=2); return D[iu].mean()

def relaxer(P, Ac, lbar, iters=80, eta=0.05, kappa=1.0, krep=0.5):
    P = P.copy(); l_rest, l_rep = LAMBDA*lbar, 0.5*lbar
    for _ in range(iters):
        diff = P[:,None]-P[None]; dist = np.linalg.norm(diff, axis=2) + 1e-9
        u = diff/dist[...,None]
        spring = -kappa*(Ac*(dist-l_rest))[...,None]*u
        rep = krep*(((dist<l_rep)*(l_rep-dist))*(1-np.eye(len(P))))[...,None]*u
        P += eta*(spring.sum(1)+rep.sum(1))
    return P

def delta_rel(A0, A1):
    E0, E1 = np.triu(A0,1)>0, np.triu(A1,1)>0
    return 1 - (E0&E1).sum()/E0.sum()

def une(seed):
    rng = np.random.default_rng(seed)
    P0 = rng.uniform(0,1,(N_NOEUDS,3)); A0 = knn_graph(P0); Lp0 = laplacien_graphe(A0)
    F = rng.uniform(-.5,.5,N_NOEUDS); I = rng.uniform(-.5,.5,N_NOEUDS); B=(F+.5*I>0).astype(float)
    for _ in range(T): F,I,B = step(F,I,B,Lp0)
    X0 = np.concatenate([F,I]); F1,I1,_ = step(F,I,B,Lp0); X1 = np.concatenate([F1,I1])
    na = int(np.triu(A0,1).sum()); lbar = longueur_moy(P0, A0); out = {}
    conds = {"pondérée": compresser(A0,F,I,rng), "aléatoire": compresser_aleatoire(A0, na//2, rng), "ressorts complets": A0}
    for nom, Ac in conds.items():
        P1 = relaxer(P0, Ac, lbar)
        Ad = knn_graph(P1)
        Lpc = laplacien_graphe(Ac); Lpd = laplacien_graphe(Ad)
        f,i,b = F.copy(),I.copy(),B.copy()
        for _ in range(T): f,i,b = step(f,i,b,Lpc)
        for _ in range(200): f,i,b = step(f,i,b,Lpd)
        X = np.concatenate([f,i])
        out[nom] = dict(drel=delta_rel(A0,Ad), dret=min(np.linalg.norm(X-X0), np.linalg.norm(X-X1)),
                        depl=np.sqrt(np.mean(np.sum((P1-P0)**2,1))), deg0=A0.sum(1).std(), degd=Ad.sum(1).std())
    return out

if __name__ == "__main__":
    M.D_I = 4.0; NS = 100
    print(f"Simulation sur {NS} graines (stéréomorphogenèse)...")
    res = [une(s) for s in range(NS)]
    rb = np.random.default_rng(7)
    print(f"{NS} graines, kNN 3D (k={K_KNN}), contraction λ={LAMBDA}, seuil d'échec {SEUIL}\n")
    print(f"{'condition':18s} {'Δ_relation':>14s} {'déplacement':>12s} {'échecs':>8s} {'d_ret médian':>13s} {'Spearman(Δ,d_ret)':>18s}")
    for nom in ["pondérée","aléatoire","ressorts complets"]:
        dr = np.array([r[nom]['drel'] for r in res]); dt = np.array([r[nom]['dret'] for r in res]); de = np.array([r[nom]['depl'] for r in res])
        print(f"{nom:18s} {dr.mean():7.3f}±{dr.std():.3f} {de.mean():12.3f} {int((dt>=SEUIL).sum()):5d}/{NS} {np.median(dt):13.2f} {spearman(dr,dt):18.2f}")
    print(f"\ndispersion des degrés : A0 {np.mean([r['pondérée']['deg0'] for r in res]):.2f} | A_d (pondérée) {np.mean([r['pondérée']['degd'] for r in res]):.2f}")
    d = np.array([r['pondérée']['drel']-r['aléatoire']['drel'] for r in res])
    bs = [d[rb.integers(0,NS,NS)].mean() for _ in range(2000)]
    print(f"Δ_relation pondérée − aléatoire (apparié) : {d.mean():+.3f}  IC95 bootstrap [{np.percentile(bs,2.5):+.3f}, {np.percentile(bs,97.5):+.3f}]")
