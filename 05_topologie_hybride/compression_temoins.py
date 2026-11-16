import numpy as np

def compresser_aleatoire(A, n_aretes, rng):
    iu = np.array(np.nonzero(np.triu(A, 1))).T
    if not 0 <= n_aretes <= len(iu):
        raise ValueError("Nombre d'arêtes invalide.")
    choix = iu[rng.choice(len(iu), size=n_aretes, replace=False)]
    Ac = np.zeros_like(A)
    Ac[choix[:, 0], choix[:, 1]] = 1
    Ac[choix[:, 1], choix[:, 0]] = 1
    return Ac
