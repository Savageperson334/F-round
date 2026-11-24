# translation
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/glm.py, line 51
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def translate(M, x, y=None, z=None):
    """Translate by an offset (x, y, z) .

    Parameters
    ----------
    M : array
        Original transformation (4x4).
    x : float
        X coordinate of a translation vector.
    y : float | None
        Y coordinate of translation vector. If None, `x` will be used.
    z : float | None
        Z coordinate of translation vector. If None, `x` will be used.

    Returns
    -------
    M : array
        Updated transformation (4x4). Note that this function operates
        in-place.
    """
    y = x if y is None else y
    z = x if z is None else z
    T = np.array([[1.0, 0.0, 0.0, x],
                  [0.0, 1.0, 0.0, y],
                  [0.0, 0.0, 1.0, z],
                  [0.0, 0.0, 0.0, 1.0]], dtype=M.dtype).T
    M[...] = np.dot(M, T)
    return M


def translation(x, y=None, z=None):
    """Translate by an offset (x, y, z) .

    Parameters
    ----------
    x : float
        X coordinate of a translation vector.
    y : float | None
        Y coordinate of translation vector. If None, `x` will be used.
    z : float | None
        Z coordinate of translation vector. If None, `x` will be used.

    Returns
    -------
    M : array
        Translation matrix
    """

    M = np.eye(4, dtype=np.float32)
    return translate(M,x,y,z)
