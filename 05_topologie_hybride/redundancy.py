"""
redundancy.py (ou v14_redundance.py)

Test d'encodage holographique et de redondance spatiale.
Ce script entraîne un classifieur (SVM) à prédire l'état topologique global 
d'un système (taille des domaines) en ne regardant qu'un patch local (ex: 7x7).

Pour éviter les fuites de données et les faux positifs :
- L'étiquette globale est calculée UNIQUEMENT en dehors du patch.
- Le patch ne contient QUE les champs continus (F, I) et leurs gradients.
- Le contrôle (surrogate de Fourier multivarié) préserve les spectres 
  individuels et croisés, mais détruit l'organisation spatiale locale.
"""

import numpy as np
from scipy.ndimage import label
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# =========================================================
# PARAMÈTRES PHYSIQUES & SIMULATION
# =========================================================
ALPHA, BETA, G, D_I, GAMMA, SEUIL = 0.25, 0.05, 0.3, 4.0, 1.0, 0.0
L = 21
D_F = 0.1
T_MAX = 150
N_ECHANTILLONS = 500

# =========================================================
# DYNAMIQUE F-I-B VECTORISÉE SUR TOUT LE LOT (BATCH)
# =========================================================
def laplacien_batch(Z):
    """Calcule le laplacien discret 2D sur un batch de forme (B, L, L)."""
    return (
        np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) +
        np.roll(Z, 1, axis=2) + np.roll(Z, -1, axis=2) - 4.0 * Z
    )

def simuler_batch(n_samples, seed=42):
    """Simule n_samples simultanément via vectorisation 3D (B, L, L)."""
    rng = np.random.default_rng(seed)
    F = rng.uniform(-0.5, 0.5, (n_samples, L, L))
    I = rng.uniform(-0.5, 0.5, (n_samples, L, L))
    B = (F + 0.5 * I > SEUIL).astype(np.float64)

    for _ in range(T_MAX):
        Q = 2.0 * B - 1.0
        lap_F = laplacien_batch(F)
        lap_I = laplacien_batch(I)

        F = (1.0 - ALPHA) * F + ALPHA * np.tanh(I + G * Q + D_F * lap_F)
        I = (1.0 - BETA) * I + BETA * np.tanh(F + D_I * lap_I - GAMMA * (I**3))
        B = (F + 0.5 * I > SEUIL).astype(np.float64)

    return F, I, B

# =========================================================
# ÉTIQUETTE DISJOINTE (Cible)
# =========================================================
def creer_masque_disjoint(taille_patch):
    r = taille_patch // 2
    cx, cy = L // 2, L // 2
    masque = np.ones((L, L), dtype=bool)
    idx_x = (np.arange(-r, r + 1) + cx) % L
    idx_y = (np.arange(-r, r + 1) + cy) % L
    masque[np.ix_(idx_x, idx_y)] = False
    return masque

def calculer_etiquettes(B_batch, taille_patch=7):
    """Calcule la taille moyenne des composantes connexes HORS du patch."""
    masque = creer_masque_disjoint(taille_patch)
    etiquettes = np.zeros(B_batch.shape[0])

    for i in range(B_batch.shape[0]):
        B_isole = (B_batch[i] > 0.5) & masque
        labeled, num_features = label(B_isole)
        if num_features > 0:
            tailles = np.bincount(labeled.ravel())[1:]
            etiquettes[i] = np.mean(tailles)
        else:
            etiquettes[i] = 0.0
    return etiquettes

# =========================================================
# CONTRÔLE : SURROGATE FOURIER MULTIVARIÉ
# =========================================================
def substitut_fourier_multivarie(F_batch, I_batch, seed=1000):
    """Randomise la phase spatiale (même phase pour F et I) pour préserver les spectres croisés."""
    rng = np.random.default_rng(seed)
    rand_phase_exp = np.exp(1j * rng.uniform(-np.pi, np.pi, F_batch.shape))

    def appliquer_surrogate(X):
        Xk = np.fft.fft2(X, axes=(-2, -1))
        return np.real(np.fft.ifft2(Xk * rand_phase_exp, axes=(-2, -1)))

    return appliquer_surrogate(F_batch), appliquer_surrogate(I_batch)

# =========================================================
# EXTRACTION DES FEATURES LOCALES (Patch)
# =========================================================
def extraire_features(F_batch, I_batch, taille_patch):
    """Extrait les valeurs locales, les gradients et les énergies locales."""
    r = taille_patch // 2
    cx, cy = L // 2, L // 2
    idx_x = (np.arange(-r, r + 1) + cx) % L
    idx_y = (np.arange(-r, r + 1) + cy) % L

    pF = F_batch[:, idx_x[:, None], idx_y]
    pI = I_batch[:, idx_x[:, None], idx_y]

    B_size = F_batch.shape[0]
    gFx = np.diff(pF, axis=1).reshape(B_size, -1)
    gFy = np.diff(pF, axis=2).reshape(B_size, -1)
    gIx = np.diff(pI, axis=1).reshape(B_size, -1)
    gIy = np.diff(pI, axis=2).reshape(B_size, -1)

    feats = [
        pF.reshape(B_size, -1), pI.reshape(B_size, -1),
        gFx, gFy, gIx, gIy,
        gFx**2, gFy**2, gIx**2, gIy**2,
    ]
    return np.concatenate(feats, axis=1)

# =========================================================
# PIPELINE D'ÉVALUATION
# =========================================================
if __name__ == "__main__":
    print(f"Génération vectorisée de {N_ECHANTILLONS} simulations...")
    F, I, B = simuler_batch(N_ECHANTILLONS, seed=0)

    print("Calcul des étiquettes disjointes...")
    etiquettes = calculer_etiquettes(B, taille_patch=7)
    mediane = np.median(etiquettes)
    y = (etiquettes > mediane).astype(int)

    print("Génération des substituts de Fourier...")
    F_fourier, I_fourier = substitut_fourier_multivarie(F, I, seed=42)

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    clf = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1.0, gamma="scale"))

    print(f"\n{'Taille':>8} | {'Features':>9} | {'Acc (Dyn)':>12} | {'Acc (Fourier)':>14} | {'Gain':>8}")
    print("-" * 62)

    for taille in [3, 5, 7]:
        X_dyn = extraire_features(F, I, taille)
        X_four = extraire_features(F_fourier, I_fourier, taille)

        acc_dyn = cross_val_score(clf, X_dyn, y, cv=cv, scoring="balanced_accuracy").mean()
        acc_four = cross_val_score(clf, X_four, y, cv=cv, scoring="balanced_accuracy").mean()

        print(f"{taille:3d}x{taille:<3d} | {X_dyn.shape[1]:9d} | {acc_dyn:12.3f} | {acc_four:14.3f} | {acc_dyn - acc_four:+8.3f}")
