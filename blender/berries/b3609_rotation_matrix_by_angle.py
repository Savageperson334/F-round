# rotation_matrix_by_angle
#
# Copied verbatim from https://github.com/sleeping-h/vector-fields
#   file custom_linalg.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life, fluid mechanics, fields and emergence
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rotation_matrix_by_angle(t):
    cos_t = np.cos(t)
    sin_t = np.sin(t)
    return np.array([[cos_t, -sin_t], [sin_t, cos_t]])
