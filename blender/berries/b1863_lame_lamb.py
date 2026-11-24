# lame_lamb
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/seismic/wavefd.py, line 369
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lame_lamb(pvel, svel, dens):
    r"""
    Calculate the Lame parameter :math:`\lambda` P and S wave velocities
    (:math:`\alpha` and :math:`\beta`) and the density (:math:`\rho`).

    .. math::

        \lambda = \alpha^2 \rho - 2\beta^2 \rho

    Parameters:

    * pvel : float or array
        The P wave velocity
    * svel : float or array
        The S wave velocity
    * dens : float or array
        The density

    Returns:

    * lambda : float or array
        The Lame parameter

    Examples::

        >>> print lame_lamb(2000, 1000, 2700)
        5400000000
        >>> import numpy as np
        >>> pv = np.array([2000, 3000], dtype='float64')
        >>> sv = np.array([1000, 1700], dtype='float64')
        >>> dens = np.array([2700, 3100], dtype='float64')
        >>> lamb = lame_lamb(pv, sv, dens)
        >>> print "[ {:g}  {:g} ]".format(lamb[0], lamb[1])
        [ 5.4e+09  9.982e+09 ]

    """
    lamb = dens*pvel**2 - 2*dens*svel**2
    return lamb
