# lame_mu
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/seismic/wavefd.py, line 409
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lame_mu(svel, dens):
    r"""
    Calculate the Lame parameter :math:`\mu` from S wave velocity
    (:math:`\beta`) and the density (:math:`\rho`).

    .. math::

        \mu = \beta^2 \rho

    Parameters:

    * svel : float or array
        The S wave velocity
    * dens : float or array
        The density

    Returns:

    * mu : float or array
        The Lame parameter

    Examples::

        >>> print lame_mu(1000, 2700)
        2700000000
        >>> import numpy as np
        >>> sv = np.array([1000, 1700], dtype='float64')
        >>> dens = np.array([2700, 3100], dtype='float64')
        >>> mu = lame_mu(sv, dens)
        >>> print "[ {:g}  {:g} ]".format(mu[0], mu[1])
        [ 2.7e+09  8.959e+09 ]

    """
    mu = dens * svel ** 2
    return mu
