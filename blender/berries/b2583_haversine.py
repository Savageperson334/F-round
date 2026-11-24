# haversine
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/inversion.py, line 320
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


def haversine(lat_rad_1,
              lat_rad_2,
              lon_rad_1,
              lon_rad_2,
              earth_radius=6.3781e3):
    """
    Calculates the distance on a sphere.
    """
    d = (
        2
        * earth_radius
        * np.arcsin(
            np.sqrt(
                hav(lat_rad_1 - lat_rad_2)
                + np.cos(lat_rad_1) * np.cos(lat_rad_2)
                * hav(lon_rad_1 - lon_rad_2)
            )
        )
    )
    return d
