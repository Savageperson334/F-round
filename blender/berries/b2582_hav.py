# hav
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/inversion.py, line 309
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def hav(theta):
    """Haversine of an angle, ``sin²(theta / 2)``.

    Parameters
    ----------
    theta : float or np.ndarray
        Angle in radians.
    """
    return np.square(np.sin(theta / 2))
