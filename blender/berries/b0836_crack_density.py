# crack_density
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/anisotropy.py, line 292
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def crack_density(porosity, aspect):
    """
    Returns crack density from porosity and aspect ratio, phi and alpha
    respectively in the unnumbered equation between 15.40 and 15.41 in
    Dvorkin et al. 2014.

    Args:
        porosity (float): Fractional porosity.
        aspect (float): Aspect ratio.

    Returns:
        float: Crack density.
    """
    if porosity >= 1:
        porosity /= 100.

    return 3 * porosity / (4 * np.pi * aspect)
