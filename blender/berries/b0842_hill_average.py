# hill_average
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/bounds.py, line 62
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def reuss_bound(f, m):
    """
    The lower bound on the effective elastic modulus of a
    mixture of N material phases. This is defined at the harmonic
    average of the constituents. Same as Wood's equation for homogeneous mixed fluids.

    Args:
        f: list or array of N volume fractions (must sum to 1 or 100).
        m: elastic modulus of N constituents (list or array).

    Returns:
        mr: Reuss lower bound.
    """
    f = np.array(f).astype(float)

    if float(sum(f)) == 100.0:
        # fractions have been given in percent: scale to 1.
        f /= 100.0

    m = np.array(m)
    mr = 1.0 / np.sum(f / m)

    return mr


def voigt_bound(f, m):
    """
    The upper bound on the effective elastic modulus, mv of a
    mixture of N material phases. This is defined at the arithmetic
    average of the constituents.

    Args:
        f: list or array of N volume fractions (must sum to 1 or 100).
        m: elastic modulus of N constituents (list or array).

    Returns:
        mv: Voigt upper bound.

    """
    f = np.array(f).astype(float)

    if float(sum(f)) == 100.0:
        # fractions have been given in percent: scale to 1.
        f /= 100.0

    m = np.array(m)
    mv = np.sum(f * m)

    return mv


def hill_average(f, m):
    """
    The Hill average effective elastic modulus, mh of a
    mixture of N material phases. This is defined as the simple
    average of the Reuss (lower) and Voigt (upper) bounds.

    Args:
        f: list or array of N volume fractions (must sum to 1 or 100).
        m:elastic modulus of N constituents (list or array).

    Returns:
        mh: Hill average.
    """
    mv = voigt_bound(f, m)
    mr = reuss_bound(f, m)
    mh = (mv + mr) / 2.0

    return mh
