# cos_angular_separation
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file src/sky_math.py, line 22
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def cos_angular_separation(ra1, dec1, ra2, dec2):
    """
    Cosine of the great-circle separation (spherical law of cosines),
    clipped into [-1, 1]. Use when the cosine itself feeds a further
    computation (e.g. the law-of-cosines heliocentric distance); use
    angular_separation_deg() when you want the angle.
    """
    c = (np.sin(dec1) * np.sin(dec2)
         + np.cos(dec1) * np.cos(dec2) * np.cos(ra1 - ra2))
    return np.clip(c, -1.0, 1.0)
