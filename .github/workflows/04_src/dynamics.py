import numpy as np

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
