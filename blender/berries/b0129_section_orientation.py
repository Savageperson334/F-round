# section_orientation
#
# Copied verbatim from https://github.com/CassGut/Kinova-Gen-3-Robotic-Arm-Pick-and-Place-Controller-Tutorial
#   file PICK_PLACE/Python Pick and Place Files/kinova_pick_and_place_code.py, line 522
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def section_orientation(x, y):
    # Calculate the angle in radians from the positive x-axis
    angle_rad = np.arctan2(y, x)

    # Convert the angle to degrees
    angle_deg = np.degrees(angle_rad)

    # Adjust the angle range from [0, 360]
    if angle_deg < 0:
        angle_deg += 360

    # Determine and return the circle section based on the angle
    if 45 <= angle_deg < 135:
        return np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, -1]])
    elif 135 <= angle_deg < 225:
        return np.array([[0, -1, 0],
                         [-1, 0, 0],
                         [0, 0, -1]])
    elif 225 <= angle_deg < 315:
        return np.array([[1, 0, 0],
                         [0, -1, 0],
                         [0, 0, -1]])
    else:  # Covers both 315 to 360 and 0 to 45 degrees
        return np.array([[0, 1, 0],
                         [1, 0, 0],
                         [0, 0, -1]])
