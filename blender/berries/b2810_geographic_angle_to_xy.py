# geographic_angle_to_xy
#
# Copied verbatim from https://github.com/mtomasini/PytheasSimulator
#   file src/pytheas_simulator/utilities.py, line 87
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def geographic_angle_to_xy(angle: float) -> np.ndarray:
    """From a geographic angle (with 0 degrees signifying North, 90 East, 180 South and 270 W) return x and y.

    Args:
        angle (float): geographic angle in degrees

    Returns:
        np.ndarray: array with dx (horizontal Eastward) and dy (vertical Northward)
    """
    angle_radians = np.deg2rad(angle)
    dx = np.sin(np.pi - angle_radians)
    dy = np.cos(angle_radians)

    return np.array([dx, dy])
