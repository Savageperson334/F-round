# radiation_theta
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/heart.py, line 3976
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def radiation_theta(takeoff_angles_rad, azimuths_rad):
    """
    Radiation weights for seismic Sv- phase

    Returns
    -------
    array-like 3 x n_stations
    """
    st = num.sin(takeoff_angles_rad)
    ct = num.cos(takeoff_angles_rad)
    sa = num.sin(azimuths_rad)
    ca = num.cos(azimuths_rad)
    return num.array([ct * ca, ct * sa, -st])
