# hyperbola
#
# Copied verbatim from https://github.com/holodyne/slmsuite
#   file slmsuite/holography/analysis/fitfunctions.py, line 58
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def hyperbola(z, w0, z0, zr):
    r"""
    For fitting a hyperbola.

    .. math:: w(z) = w_0 \sqrt{1 + \left[\frac{z - z_0}{z_R}\right]^2}.

    Parameters
    ----------
    z : numpy.ndarray
        Distance.
    w0 : float
        Beamradius at :math:`z = z_0`.
    z0 : float
        Plane of focus :math:`z_0`, the center of the hyperbola.
    zr : float
        Rayleigh length :math:`z_R`, the depth of focus.

    Returns
    -------
    w : numpy.ndarray
        Hyperbola evaluated at all ``z``.
    """
    return w0 * np.sqrt(1 + np.square((z - z0) / zr))
