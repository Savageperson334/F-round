# rotate
#
# Copied verbatim from https://github.com/anshdavid/Procedural-City-Generation
#   file procedural_city_generation/additional_stuff/rotate.py, line 3
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rotate(angle, vector):
    """
    Rotates a 2D Vector.

    Parameters
    ----------
    angle : float
        Angle in which the Vector is rotated in mathematically-positive direction
    vector : np.array(2, )
        Vector to be rotated
    """
    #Explicit case because it gets called very often
    if angle == 90:
        return np.array([-vector[1], vector[0]])

    angle=angle*np.pi/180
    matrix=np.array([np.cos(angle),
    np.sin(angle),
    -np.sin(angle),
    np.cos(angle)]).reshape(2, 2)

    matrix=np.dot(vector, matrix)
    return matrix
