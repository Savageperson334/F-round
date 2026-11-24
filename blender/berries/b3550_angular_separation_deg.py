# angular_separation_deg
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file src/sky_math.py, line 34
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def angular_separation_deg(ra1, dec1, ra2, dec2):
    """
    Great-circle separation in degrees via the haversine formula,
    which stays accurate at small separations where the law of
    cosines loses precision.
    """
    a = (np.sin((dec2 - dec1) / 2.0) ** 2
         + np.cos(dec1) * np.cos(dec2) * np.sin((ra2 - ra1) / 2.0) ** 2)
    return 2.0 * np.degrees(np.arcsin(np.sqrt(np.clip(a, 0.0, 1.0))))
