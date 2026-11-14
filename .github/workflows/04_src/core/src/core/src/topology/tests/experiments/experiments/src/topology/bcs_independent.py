import networkx as nx
import numpy as np

L_DEFAULT = 41

def _pas(a, b, L):
    return tuple(((b[k] - a[k] + L // 2) % L) - L // 2 for k in (0, 1))

def analyse_rang_networkx(B, val, conn, L=L_DEFAULT):
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
