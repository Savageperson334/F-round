# smallest_angular_distance_nolimits
#
# Copied verbatim from https://github.com/CassGut/Kinova-Gen-3-Robotic-Arm-Pick-and-Place-Controller-Tutorial
#   file PICK_PLACE/Python Pick and Place Files/smallest_angular_distance.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def smallest_angular_distance_nolimits(initial_angle, final_angle):
        initial_angle = (initial_angle +360) % 360
        final_angle = (final_angle +360) % 360    
        cw = np.abs((initial_angle - final_angle + 360) % 360)
        ccw = np.abs((final_angle - initial_angle + 360) % 360)
        if ccw < cw:
            return ccw
        else:
            return -cw
