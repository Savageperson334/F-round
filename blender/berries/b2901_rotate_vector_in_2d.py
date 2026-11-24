# rotate_vector_in_2d
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 780
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rotate_vector_in_2d(v, angle):  # rotate a 2d vector counter-clockwise
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    v_rotated = np.dot(rotation_matrix, v)
    return v_rotated
