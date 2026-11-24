# lame_lambda
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file fatiando/seismic/elastic_moduli.py, line 8
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lame_lambda(vp, vs, density):
    r"""
    Calculate Lamé's first parameter :math:`\lambda`.

    Defined in terms of the P and S wave velocities
    (:math:`v_P` and :math:`v_S`) and the density (:math:`\rho`).

    .. math::

        \lambda = v_P^2 \rho - 2v_S^2 \rho

    Units must be consistent. For example, if *vp* and *vs* are in m/s, the
    density must be kg/m³ (or g/m³, etc).

    Parameters:

    * vp : float or array
        The P wave velocity
    * vs : float or array
        The S wave velocity
    * density : float or array
        The density

    Returns:

    * lambda : float or array
        The Lamé parameter

    Examples::

        >>> print(lame_lambda(vp=2350, vs=1125, density=2500))
        7478125000
        >>> import numpy as np
        >>> vp = np.array([2000., 3000.])
        >>> vs = np.array([1000., 1700.])
        >>> density = np.array([2700., 3100.])
        >>> print(lame_lambda(vp, vs, density))
        [  5.40000000e+09   9.98200000e+09]

    """
    lamb = density*vp**2 - 2*density*vs**2
    return lamb
