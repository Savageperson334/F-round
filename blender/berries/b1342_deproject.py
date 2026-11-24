# deproject
#
# Copied verbatim from https://github.com/cbassa/stvid
#   file stvid/fourframe.py, line 1028
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def deproject(l0, b0, l, b):
    lt = l * np.pi / 180
    bt = b * np.pi / 180
    l0t = l0 * np.pi / 180
    b0t = b0 * np.pi / 180

    # To vector
    r = np.array([np.cos(lt) * np.cos(bt), np.sin(lt) * np.cos(bt), np.sin(bt)])

    # Rotation matrices
    cl, sl = np.cos(l0t), np.sin(l0t)
    Rl = np.array([[cl, sl, 0], [-sl, cl, 0], [0, 0, 1]])
    cb, sb = np.cos(b0t), np.sin(b0t)
    Rb = np.array([[cb, 0, sb], [0, 1, 0], [-sb, 0, cb]])

    # Apply rotations
    r = Rl.dot(r)
    r = Rb.dot(r)

    # Back to angles
    radius = np.arccos(r[0])
    position_angle = np.arctan2(r[1], r[2])

    # To offsets
    dl, db = radius * np.sin(position_angle), radius * np.cos(position_angle)

    return dl * 180 / np.pi, db * 180 / np.pi
