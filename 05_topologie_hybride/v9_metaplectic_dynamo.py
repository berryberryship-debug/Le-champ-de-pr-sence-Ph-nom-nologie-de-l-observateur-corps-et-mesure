import numpy as np

L = 41; N = L * L
alpha, beta = 0.25, 0.05

# Paramètres du "Double Courant" (2 nA)
g = 0.6          # Doublé (0.3 -> 0.6)
D_F = 0.1
D_I = 8.0        # Doublé (4.0 -> 8.0)
gamma, S = 1.0, 0.0

def lap(Z):
    return (np.roll(Z,1,0)+np.roll(Z,-1,0)
            +np.roll(Z,1,1)+np.roll(Z,-1,1)-4*Z)

def diagnostique_dynamo(F_h, I_h, t0, t1):
    """Mesure le couplage ∇F·∇I : le transfert Implié -> Boléen."""
    F = F_h[t0:t1].reshape(-1, L, L)
    I = I_h[t0:t1].reshape(-1, L, L)
    gFx, gFy = np.gradient(F, axis=(1,2))
    gIx, gIy = np.gradient(I, axis=(1,2))
    num = np.mean(gFx*gIx + gFy*gIy)
    den = np.sqrt(np.mean(gFx**2+gFy**2) * np.mean(gIx**2+gIy**2)) + 1e-12
    return num/den

def simuler_double(seed=42, T_total=500):
    rng = np.random.default_rng(seed)
    F = rng.uniform(-0.5, 0.5, (L, L))
    I = rng.uniform(-0.5, 0.5, (L, L))
    B = (F + 0.5*I > S).astype(float)
    
    Q_h, F_h, I_h = [], [], []
    for t in range(T_total):
        Q = 2.0*B - 1.0
        Fn = (1-alpha)*F + alpha*np.tanh(I + g*Q + D_F*lap(F))
        In = (1-beta)*I + beta*np.tanh(Fn + D_I*lap(I) - gamma*I**3)
        Bn = (Fn + 0.5*In > S).astype(float)
        F, I, B = Fn, In, Bn
        Q_h.append(Q.ravel()); F_h.append(F.ravel()); I_h.append(I.ravel())
    
    return np.array(Q_h), np.array(F_h), np.array(I_h)

if __name__ == "__main__":
    Q_h, F_h, I_h = simuler_double()
    
    print("=== RÉGIME DOUBLE COURANT : g=0.6, D_I=8.0 ===")
    print("Fenêtre       ω̄_Σ       ⟨∇F·∇I⟩ (Dynamo)")
    print("-" * 45)
    
    for t0, t1, lbl in [(0,10,"Ultra-court"), (10,60,"Transitoire"), (450,500,"Asymptotique")]:
        w = np.mean(np.abs(np.diff(Q_h[t0:t1], axis=0)))/2.0
        dyn = diagnostique_dynamo(F_h, I_h, t0, t1)
        print(f"{lbl:12s}  {w:.4f}      {dyn:+.4f}")
