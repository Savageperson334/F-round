# orientation_error_as_euler
#
# Copied verbatim from https://github.com/omron-sinicx/vive_tracking_ros
#   file src/vive_tracking_ros/math_utils.py, line 54
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Robots and tactile mechanisms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def skew(v):
    """
    Returns the 3x3 skew matrix.
    The skew matrix is a square matrix M{A} whose transpose is also its
    negative; that is, it satisfies the condition M{-A = A^T}.
    @type v: array
    @param v: The input array
    @rtype: array, shape (3,3)
    @return: The resulting skew matrix
    """
    skv = np.roll(np.roll(np.diag(np.asarray(v).flatten()), 1, 1), -1, 0)
    return (skv - skv.T)


def orientation_error_as_euler(quat_target, quat_source):
    """
    Calculates the orientation error between two quaternions
    quat_target is the desired orientation
    quat_source is the current orientation
    both with respect to the same fixed frame

    return vector part
    """
    qs = np.array(quat_source)
    qt = np.array(quat_target)

    ne = qs[3]*qt[3] + np.dot(qs[:3].T, qt[:3])
    ee = qs[3]*np.array(qt[:3]) - qt[3]*np.array(qs[:3]) + np.dot(skew(qs[:3]), qt[:3])
    ee *= np.sign(ne)  # disambiguate the sign of the quaternion
    return ee
