# cos
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/fitfunctions.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cos(x, b, a, c, k=1):
    r"""
    For fitting an offset sinusoid.

    .. math:: y(x) = c + \frac{a}{2} \left[1+\cos(kx-b) \right].

    Parameters
    ----------
    x : numpy.ndarray
        Phase in radians.
    b : float
        Phase offset.
    a : float
        Peak amplitude.
    c : float
        Amplitude offset.
    k : float
        Phase scale factor. Default is 1.

    Returns
    -------
    y : numpy.ndarray
        Cosine fit evaluated at all ``x``.
    """
    return a * 0.5 * (1 + np.cos(k * x - b)) + c
