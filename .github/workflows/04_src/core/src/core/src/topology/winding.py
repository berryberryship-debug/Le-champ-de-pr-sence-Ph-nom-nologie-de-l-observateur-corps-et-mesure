import numpy as np
from collections import deque

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

def analyse_rang(B, val, conn, L=41):
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
    return (analyse_rang(Bm,1,4,L), analyse_rang(1-Bm,1,8,L))
