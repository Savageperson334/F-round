# tophat2d
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/fitfunctions.py, line 268
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def tophat2d(xy, x0, y0, R, a=1, c=0):
    r"""
    For fitting a 2D tophat distribution.

    .. math:: z(x,y) =  \left\{
                            \begin{array}{ll}
                                a + c, & x^2 + y^2 \leq R^2 \\
                                c, & \text{ otherwise}.
                            \end{array}
                        \right.

    Parameters
    ----------
    xy : numpy.ndarray
        Points to fit upon (x, y).
    x0, y0 : float
        Vector offset.
    R : float
        Active radius of the tophat.
    a : float
        Amplitude.
    c : float
        Offset.

    Returns
    -------
    z : numpy.ndarray
        Tophat fit evaluated at all ``(x,y)`` in ``xy``.
    """
    x = xy[0] - x0
    y = xy[1] - y0
    return np.where(np.square(x) + np.square(y) <= R * R, a + c, c)
