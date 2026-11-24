# parabola
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/fitfunctions.py, line 33
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def parabola(x, a, x0, y0):
    r"""
    For fitting a parabola.

    .. math:: y(x) = a(x - x_0)^2 + y_0

    Parameters
    ----------
    x : numpy.ndarray
        Some independent variable.
    a : float
        Strength of the parabola.
    x0 : float
        :math:`x` position of the vertex.
    y0 : float
        :math:`y` position of the vertex.

    Returns
    -------
    y : numpy.ndarray
        Parabola evaluated at all ``x``.
    """
    return a * np.square(x - x0) + y0
