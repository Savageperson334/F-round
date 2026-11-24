# reflection_time
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/transform/nmo.py, line 12
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def reflection_time(t0, x, vnmo):
    """
    Calculate the travel-time of a reflected wave. Doesn't consider
    refractions or changes in velocity.

    The units must be consistent. E.g., if t0 is seconds and
    x is metres, vnmo must be m/s.

    Args:
        t0 (float): The 0-offset (normal incidence) travel-time.
        x (float): The offset of the receiver.
        vnmo (float): The NMO velocity.

    Returns:
        t (float): The reflection travel-time.
    """
    t = np.sqrt(t0**2 + x**2/vnmo**2)
    return t
