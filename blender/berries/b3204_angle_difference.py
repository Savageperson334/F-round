# angle_difference
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/orthodrome.py, line 969
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def angle_difference(angle_a, angle_b):
    '''
    Difference between two angles in [deg].

    :param angle_a: Angle A [deg].
    :param angle_b: Angle B [deg].

    :return: Difference between the two angles in [deg].
    :rtype: float
    '''
    return ((angle_a - angle_b) + 180.) % 360. - 180.
