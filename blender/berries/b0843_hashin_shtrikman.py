# hashin_shtrikman
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/bounds.py, line 82
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from collections import namedtuple
import numpy as np


def hashin_shtrikman(f, k, mu, modulus='bulk'):
    """
    Hashin-Shtrikman bounds for a mixture of two constituents.
    The best bounds for an isotropic elastic mixture, which give
    the narrowest possible range of elastic modulus without
    specifying anything about the geometries of the constituents.

    Args:
        f: list or array of volume fractions (must sum to 1.00 or 100%).
        k: bulk modulus of constituents (list or array).
        mu: shear modulus of constituents (list or array).
        modulus: A string specifying whether to return either the
            'bulk' or 'shear' HS bound.

    Returns:
        namedtuple: The Hashin Shtrikman (lower, upper) bounds.

    :source: Berryman, J.G., 1993, Mixture theories for rock properties
             Mavko, G., 1993, Rock Physics Formulas.

    : Written originally by Xingzhou 'Frank' Liu, in MATLAB
    : modified by Isao Takahashi, 4/27/99,
    : Translated into Python by Evan Bianco
    """
    def z_bulk(k, mu):
        return (4/3.) * mu

    def z_shear(k, mu):
        return mu * (9 * k + 8 * mu) / (k + 2 * mu) / 6

    def bound(f, k, z):
        return 1 / sum(f / (k + z)) - z

    f = np.array(f)
    if sum(f) == 100:
        f /= 100.0

    func = {'shear': z_shear,
            'bulk': z_bulk}

    k, mu = np.array(k), np.array(mu)
    z_min = func[modulus](np.amin(k), np.amin(mu))
    z_max = func[modulus](np.amax(k), np.amax(mu))

    fields = ['lower_bound', 'upper_bound']
    HashinShtrikman = namedtuple('HashinShtrikman', fields)
    return HashinShtrikman(bound(f, k, z_min), bound(f, k, z_max))
