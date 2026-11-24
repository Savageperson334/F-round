# hernquist_vcirc
#
# Copied verbatim from https://github.com/jamiefarnes/negative-mass-simulator
#   file negmass_nbody/initialise/init.py, line 80
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Physics and space without tidy answers
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def hernquist_vcirc(r, a_scale=1.0, m=1.0, G=1.0):
    """Return a basic Hernquist circular orbital velocity.

    Args:
    r (numpy array): array of radii in spherical coordinates.
    a (float): Hernquist scale radius.
    m (numpy array): array of masses for all positive mass particles.
    G (float): gravitational constant.

    Returns:
    v_circ: basic Hernquist circular orbital velocity.
    """
    v_circ = (np.sqrt(G*m*r*((r+a_scale)**(-2))))
    return v_circ
