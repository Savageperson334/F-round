# vonmises_fisher
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/models/distributions.py, line 245
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


def vonmises_fisher(lats, lons, lats0, lons0, sigma=1.0):
    """
    Von-Mises Fisher distribution function.

    Parameters
    ----------
    lats : float or array_like
        Spherical-polar latitude [deg][-pi/2 pi/2] to evaluate function at.
    lons : float or array_like
        Spherical-polar longitude [deg][-pi pi] to evaluate function at
    lats0 : float or array_like
        latitude [deg] at the center of the distribution (estimated values)
    lons0 : float or array_like
        longitude [deg] at the center of the distribution (estimated values)
    sigma : float
        Width of the distribution.

    Returns
    -------
    float or array_like
        log-probability of the VonMises-Fisher distribution.

    Notes
    -----
    Wikipedia:
        https://en.wikipedia.org/wiki/Von_Mises-Fisher_distribution
        modified from: https://github.com/williamjameshandley/spherical_kde
    """

    def logsinh(x):
        """Compute log(sinh(x)), stably for large x.<
        Parameters
        ----------
        x : float or numpy.array
            argument to evaluate at, must be positive
        Returns
        -------
        float or numpy.array
            log(sinh(x))
        """
        if num.any(x < 0):
            raise ValueError("logsinh only valid for positive arguments")
        return x + num.log(1.0 - num.exp(-2.0 * x)) - num.log(2.0)

    # transform to [0-pi, 0-2pi]
    lats_t = 90.0 - lats
    lons_t = num.mod(lons, 360.0)
    lats0_t = 90.0 - lats0
    lons0_t = num.mod(lons0, 360.0)

    x = cartesian_from_polar(phi=num.deg2rad(lons_t), theta=num.deg2rad(lats_t))
    x0 = cartesian_from_polar(phi=num.deg2rad(lons0_t), theta=num.deg2rad(lats0_t))

    norm = -num.log(4.0 * num.pi * sigma**2) - logsinh(1.0 / sigma**2)
    return norm + num.tensordot(x, x0, axes=[[0], [0]]) / sigma**2
