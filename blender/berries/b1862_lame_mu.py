# lame_mu
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/seismic/elastic_moduli.py, line 52
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lame_mu(vs, density):
    r"""
    Calculate Lamé's second parameter :math:`\mu` (the shear modulus).

    Defined in terms of the S wave velocity (:math:`v_S`) and the density
    (:math:`\rho`).

    .. math::

        \mu = v_S^2 \rho

    Units must be consistent. For example, if *vs* is in m/s, the density must
    be kg/m³ (or g/m³, etc).

    Parameters:

    * vs : float or array
        The S wave velocity
    * density : float or array
        The density

    Returns:

    * mu : float or array
        The Lamé parameter

    Examples::

        >>> print(lame_mu(vs=1125, density=2500))
        3164062500
        >>> import numpy as np
        >>> vs = np.array([1000., 1700.])
        >>> density = np.array([2700., 3100.])
        >>> print(lame_mu(vs, density))
        [  2.70000000e+09   8.95900000e+09]

    """
    mu = density*vs**2
    return mu
