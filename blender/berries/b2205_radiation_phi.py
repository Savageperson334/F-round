# radiation_phi
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/heart.py, line 3991
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def radiation_phi(azimuths_rad):
    """
    Radiation weights for seismic Sh- phase

    Returns
    -------
    array-like 3 x n_stations x 3
    """
    ca = num.cos(azimuths_rad)
    sa = num.sin(azimuths_rad)
    return num.array([-sa, ca, num.zeros_like(ca)])
