# get_ellipse_tangents_through_point
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 857
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


def get_ellipse_tangents_through_point(point, semi_major_axis, semi_minor_axis):
    """
        determines the points where the tangents to an ellipse with given semi major and semi minor axis that go through
        point touch the ellipse. returns none if point is inside the ellipse
    """
    theta = np.arctan2(semi_major_axis[1], semi_major_axis[0])
    point_r = rotate_vector_in_2d([point[0], point[1], 0], -theta)
    r_major = np.sqrt(semi_major_axis[0] ** 2 + semi_major_axis[1] ** 2)
    r_minor = np.sqrt(semi_minor_axis[0] ** 2 + semi_minor_axis[1] ** 2)
    divisor = point_r[1] ** 2 * r_major ** 2 + r_minor ** 2 * point_r[0] ** 2
    if (point_r[0] / r_major) ** 2 + (point_r[1] / r_minor) ** 2 <= 1:
        return None
    square_root_term = (r_minor ** 2 * point_r[0] * r_major ** 2 / divisor) ** 2 + \
                       (point_r[1] ** 2 * r_major ** 4 - r_minor ** 2 * r_major ** 4) / divisor
    tan_1_x = r_minor ** 2 * point_r[0] / divisor + np.sqrt(square_root_term)
    tan_2_x = r_minor ** 2 * point_r[0] / divisor - np.sqrt(square_root_term)
    tan_1_y = r_minor ** 2 / point_r[1] - (r_minor / r_major) ** 2 * tan_1_x * point_r[0] / point_r[1]
    tan_2_y = r_minor ** 2 / point_r[1] - (r_minor / r_major) ** 2 * tan_2_x * point_r[0] / point_r[1]
    tan_1_r = np.array([tan_1_x, tan_1_y, 0])
    tan_2_r = np.array([tan_2_x, tan_2_y, 0])
    tan_1 = rotate_vector_in_2d(tan_1_r, theta)
    tan_2 = rotate_vector_in_2d(tan_2_r, theta)
    return [[tan_1[0], tan_1[1], 0], [tan_2[0], tan_2[1], 0]]
