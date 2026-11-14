import numpy as np
import networkx as nx
from collections import deque
import csv
import os
import sys

# ==========================================
# 1. DYNAMIQUE
# ==========================================
STEPS = 500
ALPHA = 0.25; BETA = 0.05; GAIN = 0.3
D_F = 0.1; SEUIL = 0.0; GAMMA = 1.0

def _laplacien(Z):
    return (np.roll(Z,1,0)+np.roll(Z,-1,0)
            +np.roll(Z,1,1)+np.roll(Z,-1,1)-4*Z)

def simuler(seed, D_I, L=41):
    rng = np.random.RandomState(seed)
    I = rng.uniform(-0.2, 0.2, (L, L))
    F = np.zeros((L, L))
    B = rng.randint(0, 2, (L, L))
    for _ in range(STEPS):
        Q = 2.0*B - 1.0
        F_new = (1-ALPHA)*F + ALPHA*np.tanh(I + GAIN*Q + D_F*_laplacien(F))
        I_new = (1-BETA)*I + BETA*np.tanh(F_new + D_I*_laplacien(I) - GAMMA*I**3)
        B_new = (F_new + 0.5*I_new - SEUIL > 0).astype(int)
        I, F, B = I_new, F_new, B_new
    return B

# ==========================================
# 2. TOPOLOGIE - IMPLÉMENTATION A (BFS)
# ==========================================
DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]
DIR8 = DIR4 + [(1,1),(1,-1),(-1,1),(-1,-1)]

def cle_arete(x,y,dx,dy,L):
    if (dx,dy)==(1,0): return ("x",x,y)
    if (dx,dy)==(-1,0): return ("x",(x-1)%L,y)
    if (dx,dy)==(0,1): return ("y",x,y)
    return ("y",x,(y-1)%L)

def cle_gen(x,y,dx,dy,nx,ny,L):
    if dx==0 or dy==0: return cle_arete(x,y,dx,dy,L)
    return ("d",frozenset(((x,y),(nx,ny))))

def calculer_rang(vecteurs):
    if not vecteurs: return 0
    base=[]
    for x in vecteurs:
        if x==(0,0): continue
        libre=True
        for u in base:
            if x[0]*u[1]-x[1]*u[0]==0: libre=False; break
        if libre:
            base.append(x)
            if len(base)==2: return 2
    return len(base)

def analyse_rang_A(B, val, conn, L=41):
    dirs=DIR4 if conn==4 else DIR8
    vis=np.zeros_like(B,dtype=bool)
    tous_vecteurs=[]
    for i in range(L):
        for j in range(L):
            if vis[i,j] or B[i,j]!=val: continue
            coord={(i,j):(0,0)}
            q=deque([(i,j)]); vis[i,j]=True
            edges=set(); vec=[]
            while q:
                x,y=q.popleft(); X,Y=coord[(x,y)]
                for dx,dy in dirs:
                    nx,ny=(x+dx)%L,(y+dy)%L
                    if B[nx,ny]!=val: continue
                    e=cle_gen(x,y,dx,dy,nx,ny,L)
                    if e in edges: continue
                    edges.add(e)
                    nX,nY=X+dx,Y+dy
                    if not vis[nx,ny]:
                        vis[nx,ny]=True
                        coord[(nx,ny)]=(nX,nY)
                        q.append((nx,ny))
                    else:
                        oX,oY=coord[(nx,ny)]
                        dX,dY=nX-oX,nY-oY
                        if dX%L==0 and dY%L==0:
                            wx,wy=dX//L,dY//L
                            if wx or wy: vec.append((wx,wy))
            tous_vecteurs.extend(vec)
    return calculer_rang(tous_vecteurs)

def classe_4_8(Bm, L=41):
    return (analyse_rang_A(Bm,1,4,L), analyse_rang_A(1-Bm,1,8,L))

# ==========================================
# 3. TOPOLOGIE - IMPLÉMENTATION B (NETWORKX)
# ==========================================
def _pas(a, b, L):
    return tuple(((b[k] - a[k] + L // 2) % L) - L // 2 for k in (0, 1))

def analyse_rang_B(B, val, conn, L=41):
    cells = set((i, j) for i in range(L) for j in range(L) if B[i, j] == val)
    if not cells: return 0
    G = nx.Graph()
    G.add_nodes_from(cells)
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if conn == 8:
        offsets += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for (i, j) in cells:
        for di, dj in offsets:
            ni, nj = (i + di) % L, (j + dj) % L
            if (ni, nj) in cells:
                G.add_edge((i, j), (ni, nj))
    tous_cycles = []
    for comp in nx.connected_components(G):
        sub = G.subgraph(comp)
        for cyc in nx.cycle_basis(sub):
            dx_tot = dy_tot = 0
            for k in range(len(cyc)):
                a = cyc[k]
                b = cyc[(k + 1) % len(cyc)]
                dx, dy = _pas(a, b, L)
                dx_tot += dx
                dy_tot += dy
            if dx_tot % L == 0 and dy_tot % L == 0:
                wx, wy = dx_tot // L, dy_tot // L
                if wx != 0 or wy != 0:
                    tous_cycles.append((wx, wy))
    if not tous_cycles: return 0
    base = []
    for v in tous_cycles:
        if v == (0, 0): continue
        libre = True
        for u in base:
            if v[0] * u[1] - v[1] * u[0] == 0:
                libre = False; break
        if libre:
            base.append(v)
            if len(base) == 2: return 2
    return len(base)

def classe_4_8_B(Bm, L=41):
    return (analyse_rang_B(Bm, 1, 4, L), analyse_rang_B(1 - Bm, 1, 8, L))

# ==========================================
# 4. EXPÉRIENCE : RÉPLICATION
# ==========================================
def run_replication():
    CSV_IN = 'v719_resultats.csv'
    if not os.path.exists(CSV_IN):
        print(f"[SKIP] Fichier {CSV_IN} introuvable. Impossible de faire la réplication.")
        return

    graines = []
    try:
        with open(CSV_IN) as f:
            for row in csv.DictReader(f):
                if int(row['degen']) == 1 or row['sig_star'] == '': continue
                graines.append({'seed': int(row['seed']), 'rho': float(row['rho']), 'cls_csv': (int(row['cls_rmaj']), int(row['cls_rmin']))})
    except Exception as e:
        print(f"[ERREUR] Lecture CSV : {e}")
        return

    print(f"\n--- RÉPLICATION ({len(graines)} graines) ---")
    n_diff = 0
    for i, g in enumerate(graines):
        B = np.asarray(simuler(g['seed'], 4.0)).astype(int)
        p = B.mean()
        Bm = B if p >= 0.5 else 1 - B
        recalcul_A = classe_4_8(Bm)
        cls_B = classe_4_8_B(Bm)
        if recalcul_A != cls_B or recalcul_A != g['cls_csv']:
            n_diff += 1
    print(f"Divergences A vs B vs CSV : {n_diff}")

# ==========================================
# 5. EXPÉRIENCE : CONTRÔLES NÉGATIFS
# ==========================================
def run_controles():
    print("\n--- CONTRÔLES NÉGATIFS (L=41 et L=61) ---")
    CAS = ((1, 4), (0, 8))
    for L in (41, 61):
        print(f"\nTaille L = {L}")
        print(f"{'p':>5} {'cas':>9} {'diverg':>7} {'rang>0':>7}")
        for p in (0.50, 0.55, 0.58, 0.59, 0.60, 0.62, 0.70):
            for val, conn in CAS:
                div = nz = 0
                for s in range(50):
                    M = (np.random.default_rng(s).random((L, L)) < p).astype(int)
                    a, b = analyse_rang_A(M, val, conn, L), analyse_rang_B(M, val, conn, L)
                    div += (a != b); nz += (a > 0)
                print(f"{p:>5} {str((val,conn)):>9} {div:>7} {nz:>7}")

# ==========================================
# 6. LANCEMENT
# ==========================================
if __name__ == "__main__":
    print("=== LANCEMENT DES TESTS V8 ===")
    run_controles()
    run_replication()
    print("\nTerminé.")
