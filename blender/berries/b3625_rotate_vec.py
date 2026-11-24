# rotate_vec
#
# Copied verbatim from https://github.com/sphereman/ChemBlender_2_0
#   file _math.py, line 13
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_length(vector):
    length = np.linalg.norm(vector)
    return length


def normalize(vector):
    return vector/get_length(vector) if get_length(vector) else vector


def rotate_vec(vec, axis, angle):
    u = normalize(axis)
    x, y, z = u[0], u[1], u[2]
    cos = np.cos(angle)
    sin = np.sin(angle)
    R = np.array([[cos+x*x*(1-cos), x*y*(1-cos)-z*sin, x*z*(1-cos)+y*sin],
                  [x*y*(1-cos)+z*sin, cos+y*y*(1-cos), y*z*(1-cos)-x*sin],
                  [x*z*(1-cos)-y*sin, y*z*(1-cos)+x*sin, cos+z*z*(1-cos)],])
    return np.dot(R, vec)
