# direction_from_displacement
#
# Copied verbatim from https://github.com/mtomasini/PytheasSimulator
#   file src/pytheas_simulator/utilities.py, line 130
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def direction_from_displacement(displacement: np.ndarray) -> float:
    """
    Calculates the absolute direction of a displacement in given as a vector (x, y).

    Args:
        displacement (np.ndarray): Array containing displacement (in km) in the x and y axis.

    Returns:
        float: Angle of displacement with respect to the North (in degrees).
    """
    bearing_rad = np.arctan2(displacement[1], displacement[0])
    bearing = (90 - np.rad2deg(bearing_rad)) % 360

    return bearing
