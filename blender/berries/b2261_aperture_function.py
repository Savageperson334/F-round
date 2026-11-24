# aperture_function
#
# Copied verbatim from https://github.com/hyperspy/holospy
#   file holospy/reconstruct.py, line 199
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def aperture_function(r, apradius, rsmooth):
    """
    A smooth aperture function that decays from apradius-rsmooth to apradius+rsmooth.

    Parameters
    ----------
    r : ndarray
        Array of input data (e.g. frequencies)
    apradius : float
        Radius (center) of the smooth aperture. Decay starts at apradius - rsmooth.
    rsmooth : float
        Smoothness in halfwidth. rsmooth = 1 will cause a decay from 1 to 0 over 2 pixel.

    Returns
    -------
    numpy.ndarray
    """

    return 0.5 * (1.0 - np.tanh((abs(r) - apradius) / (0.5 * rsmooth)))
