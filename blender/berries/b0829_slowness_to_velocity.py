# slowness_to_velocity
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/petrophysics/petrophysics.py, line 112
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def slowness_to_velocity(slowness):
    """
    Convert a slowness log in µs per unit depth, to velocity in unit depth
    per second.

    Args:
        slowness (ndarray): A value or sequence of values.

    Returns:
        ndarray: The velocity.
    """
    return 1e6 / np.array(slowness)
