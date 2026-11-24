# compute_barycentric_coords
#
# Copied verbatim from https://github.com/computational-imaging/hsplat
#   file hsplat/utils.py, line 722
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def compute_barycentric_coords(point, triangle):
    """
    Computes the barycentric coordinates of a point with respect to a triangle.

    Parameters:
    point (np.ndarray): The point of shape [3] (x, y, z).
    triangle (np.ndarray): The triangle vertices of shape [3, 3].

    Returns:
    np.ndarray: Barycentric coordinates (alpha, beta, gamma).
    """
    # Extract vertices
    V0, V1, V2 = triangle[0], triangle[1], triangle[2]

    # Compute vectors
    v0 = V1 - V0
    v1 = V2 - V0
    v2 = point - V0

    # Compute dot products
    d00 = np.dot(v0, v0)
    d01 = np.dot(v0, v1)
    d11 = np.dot(v1, v1)
    d20 = np.dot(v2, v0)
    d21 = np.dot(v2, v1)

    # Compute denominators
    denom = d00 * d11 - d01 * d01

    # Barycentric coordinates
    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1 - v - w

    return np.array([u, v, w])
