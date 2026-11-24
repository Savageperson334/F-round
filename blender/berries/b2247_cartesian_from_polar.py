# cartesian_from_polar
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/models/distributions.py, line 225
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def cartesian_from_polar(phi, theta):
    """
    Embedded 3D unit vector from spherical polar coordinates.

    Parameters
    ----------
    phi, theta : float or numpy.array
        azimuthal and polar angle in radians.
        (phi-longitude, theta-latitude)
    Returns
    -------
    nhat : numpy.array
        unit vector(s) in direction (phi, theta).
    """
    x = num.sin(theta) * num.cos(phi)
    y = num.sin(theta) * num.sin(phi)
    z = num.cos(theta)
    return num.array([x, y, z])
