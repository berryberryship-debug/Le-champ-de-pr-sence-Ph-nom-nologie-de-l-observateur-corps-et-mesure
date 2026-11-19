#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simulation exploratoire du couplage géométrie-topologie-dynamique sur graphe.

Conditions comparées :

1. ponderee :
   compression sélective heuristique dépendant de F et I,
   relaxation géométrique et reconstruction kNN ;

2. aleatoire :
   compression aléatoire uniforme de même densité,
   relaxation géométrique et reconstruction kNN ;

3. ressorts_complets :
   conservation de toutes les arêtes initiales,
   relaxation géométrique et reconstruction kNN ;

4. intact_sans_relaxation :
   aucune perturbation géométrique ou topologique,
   évolution dynamique sur le graphe initial.

Le modèle est exploratoire. Il ne constitue pas une mesure biologique,
phénoménologique ou physique de la conscience.
"""

from __future__ import annotations

import json
from typing import Dict, List, Tuple

import numpy as np


try:
    from .compression_temoins import (
        compresser_aleatoire,
        compresser_ponderee,
    )

    from .dynamique_double_courant import (
        laplacien_graphe,
        spearman,
        step,
    )

except ImportError:
    from compression_temoins import (
        compresser_aleatoire,
        compresser_ponderee,
    )

    from dynamique_double_courant import (
        laplacien_graphe,
        spearman,
        step,
    )


# ============================================================================
# PARAMÈTRES OPÉRATIONNELS
# ============================================================================

K_KNN = 10
N_NOEUDS = 128
N_GRAINES = 100

T_INITIAL = 100
T_COMPRESSE = 100
T_FINAL = 200

LAMBDA_CONTRACTION = 0.6
SEUIL_ECHEC = 2.0

RELAX_ITERATIONS = 80
RELAX_ETA = 0.05
RELAX_KAPPA = 1.0
RELAX_KREP = 0.5

ALPHA = 0.25
BETA = 0.05
G = 0.6
D_F = 0.1
D_I = 8.0
GAMMA = 1.0
SEUIL_B = 0.0


# ============================================================================
# CONSTRUCTION DU GRAPHE kNN
# ============================================================================

def knn_graph(
    points: np.ndarray,
    k: int = K_KNN,
) -> np.ndarray:
    """
    Construit un graphe kNN dirigé, puis le symétrise par union.

    Le degré final n'est donc pas nécessairement égal à k.
    """
    P = np.asarray(
        points,
        dtype=float,
    )

    if P.ndim != 2:
        raise ValueError(
            "points doit être une matrice 2D."
        )

    if not np.all(
        np.isfinite(P)
    ):
        raise ValueError(
            "points contient des valeurs non finies."
        )

    n_nodes = P.shape[0]

    if n_nodes < 2:
        raise ValueError(
            "Au moins deux points sont nécessaires."
        )

    k = int(k)

    if not (
        1 <= k < n_nodes
    ):
        raise ValueError(
            "k doit être compris entre 1 et n_nodes - 1."
        )

    distances = np.linalg.norm(
        P[:, None, :]
        - P[None, :, :],
        axis=2,
    )

    np.fill_diagonal(
        distances,
        np.inf,
    )

    adjacency = np.zeros(
        (
            n_nodes,
            n_nodes,
        ),
        dtype=float,
    )

    for node in range(
        n_nodes
    ):
        neighbours = np.argsort(
            distances[node]
        )[:k]

        adjacency[
            node,
            neighbours,
        ] = 1.0

    # Symétrisation par union.
    adjacency = np.maximum(
        adjacency,
        adjacency.T,
    )

    np.fill_diagonal(
        adjacency,
        0.0,
    )

    return adjacency


def longueur_moyenne(
    points: np.ndarray,
    adjacency: np.ndarray,
) -> float:
    """
    Calcule la longueur moyenne des arêtes non orientées.
    """
    P = np.asarray(
        points,
        dtype=float,
    )

    A = np.asarray(
        adjacency,
        dtype=float,
    )

    if P.ndim != 2:
        raise ValueError(
            "points doit être une matrice 2D."
        )

    if A.shape != (
        len(P),
        len(P),
    ):
        raise ValueError(
            "adjacency ne correspond pas au nombre de points."
        )

    edges = np.argwhere(
        np.triu(
            A,
            1,
        )
        > 0.0
    )

    if len(edges) == 0:
        raise ValueError(
            "Le graphe ne contient aucune arête."
        )

    edge_lengths = np.linalg.norm(
        P[edges[:, 0]]
        - P[edges[:, 1]],
        axis=1,
    )

    return float(
        np.mean(
            edge_lengths
        )
    )


# ============================================================================
# RELAXATION GÉOMÉTRIQUE
# ============================================================================

def relaxer(
    points: np.ndarray,
    adjacency: np.ndarray,
    longueur_reference: float,
    iterations: int = RELAX_ITERATIONS,
    eta: float = RELAX_ETA,
    kappa: float = RELAX_KAPPA,
    krep: float = RELAX_KREP,
) -> np.ndarray:
    """
    Relaxation géométrique discrète par forces élastiques et répulsives.

    La force élastique cherche à rapprocher la longueur des arêtes de :

        L_repos = LAMBDA_CONTRACTION * longueur_reference

    Ce modèle ne contient pas de terme de vitesse ni de mémoire
    constitutive ; le terme « visco-élastique » n'est donc pas utilisé.
    """
    P = np.asarray(
        points,
        dtype=float,
    ).copy()

    A = np.asarray(
        adjacency,
        dtype=float,
    )

    if P.ndim != 2:
        raise ValueError(
            "points doit être une matrice 2D."
        )

    n_nodes = len(P)

    if A.shape != (
        n_nodes,
        n_nodes,
    ):
        raise ValueError(
            "adjacency ne correspond pas aux points."
        )

    if not np.all(
        np.isfinite(P)
    ) or not np.all(
        np.isfinite(A)
    ):
        raise ValueError(
            "points ou adjacency contient des valeurs non finies."
        )

    iterations = int(
        iterations
    )

    if iterations < 0:
        raise ValueError(
            "iterations doit être non négatif."
        )

    longueur_reference = float(
        longueur_reference
    )

    if longueur_reference <= 0.0:
        raise ValueError(
            "longueur_reference doit être strictement positive."
        )

    longueur_repos = (
        LAMBDA_CONTRACTION
        * longueur_reference
    )

    longueur_repulsion = (
        0.5
        * longueur_reference
    )

    identity = np.eye(
        n_nodes,
        dtype=float,
    )

    for _ in range(
        iterations
    ):
        differences = (
            P[:, None, :]
            - P[None, :, :]
        )

        distances = np.linalg.norm(
            differences,
            axis=2,
        )

        distances_safe = (
            distances
            + 1e-12
        )

        directions = (
            differences
            / distances_safe[:, :, None]
        )

        # Force de rappel élastique.
        spring_force = (
            -float(kappa)
            * (
                A
                * (
                    distances
                    - longueur_repos
                )
            )[:, :, None]
            * directions
        )

        # Répulsion à courte portée, sans auto-interaction.
        repulsion_amplitude = (
            (
                distances
                < longueur_repulsion
            )
            * (
                longueur_repulsion
                - distances
            )
            * (
                1.0
                - identity
            )
        )

        repulsion_force = (
            float(krep)
            * repulsion_amplitude[:, :, None]
            * directions
        )

        total_force = (
            np.sum(
                spring_force,
                axis=1,
            )
            + np.sum(
                repulsion_force,
                axis=1,
            )
        )

        P += (
            float(eta)
            * total_force
        )

        if not np.all(
            np.isfinite(P)
        ):
            raise FloatingPointError(
                "La relaxation produit des coordonnées non finies."
            )

    return P


# ============================================================================
# MESURES TOPOLOGIQUES
# ============================================================================

def delta_relationnelle(
    adjacency_initiale: np.ndarray,
    adjacency_finale: np.ndarray,
) -> float:
    """
    Fraction des arêtes initiales qui ne sont plus présentes.

        Delta_perte =
            1 - |E_initiale inter E_finale| / |E_initiale|

    Cette métrique est directionnelle et n'est pas une distance symétrique
    entre graphes.
    """
    A0 = np.asarray(
        adjacency_initiale,
        dtype=float,
    )

    A1 = np.asarray(
        adjacency_finale,
        dtype=float,
    )

    if A0.shape != A1.shape:
        raise ValueError(
            "Les deux graphes doivent avoir la même forme."
        )

    edges_initiales = (
        np.triu(
            A0,
            1,
        )
        > 0.0
    )

    edges_finales = (
        np.triu(
            A1,
            1,
        )
        > 0.0
    )

    n_initial = int(
        np.sum(
            edges_initiales
        )
    )

    if n_initial == 0:
        return 0.0

    n_preservees = int(
        np.sum(
            edges_initiales
            & edges_finales
        )
    )

    return float(
        1.0
        - n_preservees
        / n_initial
    )


def delta_gain(
    adjacency_initiale: np.ndarray,
    adjacency_finale: np.ndarray,
) -> float:
    """
    Fraction des arêtes finales qui n'étaient pas présentes initialement.
    """
    A0 = np.asarray(
        adjacency_initiale,
        dtype=float,
    )

    A1 = np.asarray(
        adjacency_finale,
        dtype=float,
    )

    edges_initiales = (
        np.triu(
            A0,
            1,
        )
        > 0.0
    )

    edges_finales = (
        np.triu(
            A1,
            1,
        )
        > 0.0
    )

    n_finales = int(
        np.sum(
            edges_finales
        )
    )

    if n_finales == 0:
        return 0.0

    n_preservees = int(
        np.sum(
            edges_initiales
            & edges_finales
        )
    )

    return float(
        1.0
        - n_preservees
        / n_finales
    )


def distance_jaccard(
    adjacency_initiale: np.ndarray,
    adjacency_finale: np.ndarray,
) -> float:
    """
    Distance de Jaccard entre les ensembles d'arêtes.
    """
    A0 = np.asarray(
        adjacency_initiale,
        dtype=float,
    )

    A1 = np.asarray(
        adjacency_finale,
        dtype=float,
    )

    E0 = (
        np.triu(
            A0,
            1,
        )
        > 0.0
    )

    E1 = (
        np.triu(
            A1,
            1,
        )
        > 0.0
    )

    intersection = int(
        np.sum(
            E0
            & E1
        )
    )

    union = int(
        np.sum(
            E0
            | E1
        )
    )

    if union == 0:
        return 0.0

    return float(
        1.0
        - intersection
        / union
    )


# ============================================================================
# DYNAMIQUE F-I-B
# ============================================================================

def initialiser_champs(
    n_nodes: int,
    seed: int,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Initialise les champs F, I et B.
    """
    rng = np.random.default_rng(
        int(seed)
    )

    F = rng.uniform(
        -0.5,
        0.5,
        size=n_nodes,
    )

    I = rng.uniform(
        -0.5,
        0.5,
        size=n_nodes,
    )

    B = (
        F
        + 0.5 * I
        > SEUIL_B
    ).astype(float)

    return F, I, B


def evoluer(
    F: np.ndarray,
    I: np.ndarray,
    B: np.ndarray,
    adjacency: np.ndarray,
    n_steps: int,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Fait évoluer F, I et B sur un graphe.

    La convention laplacienne est :

        L = A - D

    Le terme diffusif est donc appliqué sous la forme :

        D_F * (L @ F)
        D_I * (L @ I)
    """
    n_steps = int(
        n_steps
    )

    if n_steps < 0:
        raise ValueError(
            "n_steps doit être non négatif."
        )

    laplacian = laplacien_graphe(
        adjacency
    )

    field_f = np.asarray(
        F,
        dtype=float,
    ).copy()

    field_i = np.asarray(
        I,
        dtype=float,
    ).copy()

    field_b = np.asarray(
        B,
        dtype=float,
    ).copy()

    for _ in range(
        n_steps
    ):
        field_f, field_i, field_b = step(
            field_f,
            field_i,
            field_b,
            laplacian,
            alpha=ALPHA,
            beta=BETA,
            g=G,
            d_f=D_F,
            d_i=D_I,
            gamma=GAMMA,
            seuil=SEUIL_B,
        )

    return field_f, field_i, field_b


# ============================================================================
# CONFIGURATION DES CONDITIONS
# ============================================================================

def construire_conditions(
    adjacency_initiale: np.ndarray,
    F: np.ndarray,
    I: np.ndarray,
    rng: np.random.Generator,
) -> Dict[
    str,
    Tuple[np.ndarray, bool, bool],
]:
    """
    Construit les quatre conditions expérimentales.

    Chaque valeur est :

        (graphe_intermediaire, appliquer_relaxation, appliquer_knn)
    """
    n_edges = int(
        np.sum(
            np.triu(
                adjacency_initiale,
                1,
            )
        )
    )

    n_edges_compressed = (
        n_edges
        // 2
    )

    adjacency_weighted = compresser_ponderee(
        adjacency_initiale,
        F,
        I,
        n_edges_compressed,
        rng,
    )

    adjacency_random = compresser_aleatoire(
        adjacency_initiale,
        n_edges_compressed,
        rng,
    )

    return {
        # Compression sélective F-I, puis géométrie et kNN.
        "ponderee": (
            adjacency_weighted,
            True,
            True,
        ),

        # Compression aléatoire de même densité, puis géométrie et kNN.
        "aleatoire": (
            adjacency_random,
            True,
            True,
        ),

        # Aucune suppression d'arêtes, mais relaxation et reconstruction kNN.
        "ressorts_complets": (
            adjacency_initiale.copy(),
            True,
            True,
        ),

        # Aucun changement géométrique ou topologique.
        "intact_sans_relaxation": (
            adjacency_initiale.copy(),
            False,
            False,
        ),
    }


# ============================================================================
# UNE RÉPLICATION
# ============================================================================

def une_simulation(
    seed: int,
) -> Dict[
    str,
    Dict[str, float],
]:
    """
    Exécute une réplication complète sur les quatre conditions.
    """
    rng = np.random.default_rng(
        int(seed)
    )

    points_initials = rng.uniform(
        0.0,
        1.0,
        size=(
            N_NOEUDS,
            3,
        ),
    )

    adjacency_initiale = knn_graph(
        points_initials,
        K_KNN,
    )

    longueur_reference = longueur_moyenne(
        points_initials,
        adjacency_initiale,
    )

    # État dynamique commun avant intervention.
    F, I, B = initialiser_champs(
        N_NOEUDS,
        seed + 100_000,
    )

    F, I, B = evoluer(
        F,
        I,
        B,
        adjacency_initiale,
        T_INITIAL,
    )

    X_initial = np.concatenate(
        [
            F,
            I,
        ]
    )

    # État de référence après un seul pas supplémentaire.
    F_one, I_one, _ = evoluer(
        F,
        I,
        B,
        adjacency_initiale,
        1,
    )

    X_un_pas = np.concatenate(
        [
            F_one,
            I_one,
        ]
    )

    conditions = construire_conditions(
        adjacency_initiale,
        F,
        I,
        rng,
    )

    resultats: Dict[
        str,
        Dict[str, float],
    ] = {}

    for nom, (
        adjacency_intermediaire,
        appliquer_relaxation,
        appliquer_knn,
    ) in conditions.items():

        # Partie géométrique.
        if appliquer_relaxation:
            points_finaux = relaxer(
                points_initials,
                adjacency_intermediaire,
                longueur_reference,
            )
        else:
            points_finaux = points_initials.copy()

        # Reconstruction topologique.
        if appliquer_knn:
            adjacency_finale = knn_graph(
                points_finaux,
                K_KNN,
            )
        else:
            adjacency_finale = adjacency_intermediaire.copy()

        # Dynamique pendant la phase intermédiaire.
        f, i, b = evoluer(
            F,
            I,
            B,
            adjacency_intermediaire,
            T_COMPRESSE,
        )

        # Dynamique après la géométrie/topologie finale.
        f, i, b = evoluer(
            f,
            i,
            b,
            adjacency_finale,
            T_FINAL,
        )

        X_final = np.concatenate(
            [
                f,
                i,
            ]
        )

        # Définition opérationnelle préspécifiée de la distance de retour.
        distance_retour = min(
            float(
                np.linalg.norm(
                    X_final
                    - X_initial
                )
            ),
            float(
                np.linalg.norm(
                    X_final
                    - X_un_pas
                )
            ),
        )

        deplacement_moyen = float(
            np.sqrt(
                np.mean(
                    np.sum(
                        (
                            points_finaux
                            - points_initials
                        )
                        ** 2,
                        axis=1,
                    )
                )
            )
        )

        degres_initiaux = np.sum(
            adjacency_initiale,
            axis=1,
        )

        degres_finaux = np.sum(
            adjacency_finale,
            axis=1,
        )

        resultats[nom] = {
            "delta_relationnelle": delta_relationnelle(
                adjacency_initiale,
                adjacency_finale,
            ),
            "delta_gain": delta_gain(
                adjacency_initiale,
                adjacency_finale,
            ),
            "distance_jaccard": distance_jaccard(
                adjacency_initiale,
                adjacency_finale,
            ),
            "distance_retour": distance_retour,
            "deplacement_moyen": deplacement_moyen,
            "dispersion_degres_initiale": float(
                np.std(
                    degres_initiaux
                )
            ),
            "dispersion_degres_finale": float(
                np.std(
                    degres_finaux
                )
            ),
            "n_aretes_initiales": float(
                np.sum(
                    np.triu(
                        adjacency_initiale,
                        1,
                    )
                )
            ),
            "n_aretes_finales": float(
                np.sum(
                    np.triu(
                        adjacency_finale,
                        1,
                    )
                )
            ),
        }

    return resultats


# ============================================================================
# BOOTSTRAP
# ============================================================================

def intervalle_bootstrap_moyenne(
    valeurs: np.ndarray,
    seed: int = 7,
    n_bootstrap: int = 2_000,
) -> Tuple[float, float]:
    """
    Calcule un intervalle percentile bootstrap à 95 % de la moyenne.

    L'intervalle porte sur les réplications numériques, pas sur des sujets
    biologiques ou des participants expérimentaux.
    """
    values = np.asarray(
        valeurs,
        dtype=float,
    ).reshape(-1)

    if len(values) == 0:
        raise ValueError(
            "valeurs ne peut pas être vide."
        )

    rng = np.random.default_rng(
        int(seed)
    )

    bootstrap_means = np.empty(
        int(n_bootstrap),
        dtype=float,
    )

    for index in range(
        int(n_bootstrap)
    ):
        sample = values[
            rng.integers(
                0,
                len(values),
                size=len(values),
            )
        ]

        bootstrap_means[index] = np.mean(
            sample
        )

    return (
        float(
            np.percentile(
                bootstrap_means,
                2.5,
            )
        ),
        float(
            np.percentile(
                bootstrap_means,
                97.5,
            )
        ),
    )


# ============================================================================
# AFFICHAGE
# ============================================================================

def afficher_resultats(
    resultats: List[
        Dict[
            str,
            Dict[str, float],
        ]
    ],
) -> None:
    """
    Affiche un résumé des réplications.
    """
    conditions = [
        "ponderee",
        "aleatoire",
        "ressorts_complets",
        "intact_sans_relaxation",
    ]

    print(
        "=== Simulation exploratoire "
        "géométrie-topologie-dynamique ==="
    )

    print(
        f"Réplications : {len(resultats)}"
    )

    print(
        f"Nœuds : {N_NOEUDS}"
    )

    print(
        f"kNN initial : {K_KNN}"
    )

    print(
        f"Contraction lambda : {LAMBDA_CONTRACTION}"
    )

    print(
        f"Seuil opérationnel d'échec : {SEUIL_ECHEC}"
    )

    print()

    print(
        f"{'condition':28s}"
        f"{'Delta perte':>14s}"
        f"{'Delta gain':>14s}"
        f"{'Jaccard':>12s}"
        f"{'deplacement':>14s}"
        f"{'echecs':>10s}"
        f"{'d_ret médiane':>16s}"
    )

    for condition in conditions:
        delta_perte = np.asarray(
            [
                result[condition][
                    "delta_relationnelle"
                ]
                for result in resultats
            ],
            dtype=float,
        )

        delta_gain_values = np.asarray(
            [
                result[condition][
                    "delta_gain"
                ]
                for result in resultats
            ],
            dtype=float,
        )

        jaccard = np.asarray(
            [
                result[condition][
                    "distance_jaccard"
                ]
                for result in resultats
            ],
            dtype=float,
        )

        displacement = np.asarray(
            [
                result[condition][
                    "deplacement_moyen"
                ]
                for result in resultats
            ],
            dtype=float,
        )

        return_distance = np.asarray(
            [
                result[condition][
                    "distance_retour"
                ]
                for result in resultats
            ],
            dtype=float,
        )

        failures = int(
            np.sum(
                return_distance
                >= SEUIL_ECHEC
            )
        )

        print(
            f"{condition:28s}"
            f"{np.mean(delta_perte):14.3f}"
            f"{np.mean(delta_gain_values):14.3f}"
            f"{np.mean(jaccard):12.3f}"
            f"{np.mean(displacement):14.3f}"
            f"{failures:6d}/{len(resultats):<3d}"
            f"{np.median(return_distance):16.3f}"
        )

    # Comparaison appariée : perte relationnelle.
    weighted_delta = np.asarray(
        [
            result["ponderee"][
                "delta_relationnelle"
            ]
            for result in resultats
        ],
        dtype=float,
    )

    random_delta = np.asarray(
        [
            result["aleatoire"][
                "delta_relationnelle"
            ]
            for result in resultats
        ],
        dtype=float,
    )

    difference_delta = (
        weighted_delta
        - random_delta
    )

    low_delta, high_delta = (
        intervalle_bootstrap_moyenne(
            difference_delta
        )
    )

    print()

    print(
        "Comparaison appariée pondérée - aléatoire"
    )

    print(
        "Delta perte moyen : "
        f"{np.mean(difference_delta):+.3f}"
    )

    print(
        "IC bootstrap 95 % : "
        f"[{low_delta:+.3f}, {high_delta:+.3f}]"
    )

    # Comparaison appariée : distance de retour.
    weighted_return = np.asarray(
        [
            result["ponderee"][
                "distance_retour"
            ]
            for result in resultats
        ],
        dtype=float,
    )

    random_return = np.asarray(
        [
            result["aleatoire"][
                "distance_retour"
            ]
            for result in resultats
        ],
        dtype=float,
    )

    difference_return = (
        weighted_return
        - random_return
    )

    low_return, high_return = (
        intervalle_bootstrap_moyenne(
            difference_return
        )
    )

    print()

    print(
        "Distance de retour moyenne "
        "pondérée - aléatoire : "
        f"{np.mean(difference_return):+.3f}"
    )

    print(
        "IC bootstrap 95 % : "
        f"[{low_return:+.3f}, {high_return:+.3f}]"
    )

    print()

    print(
        "Statut : réplications numériques exploratoires."
    )


# ============================================================================
# PROGRAMME PRINCIPAL
# ============================================================================

def main() -> None:
    """
    Lance les réplications et exporte les résultats en JSON.
    """
    resultats = [
        une_simulation(
            seed
        )
        for seed in range(
            N_GRAINES
        )
    ]

    afficher_resultats(
        resultats
    )

    with open(
        "resultats_stereomorphogenese.json",
        "w",
        encoding="utf-8",
    ) as output_file:
        json.dump(
            resultats,
            output_file,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    main()
