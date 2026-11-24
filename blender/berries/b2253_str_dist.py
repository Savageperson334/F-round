# str_dist
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/plotting/common.py, line 170
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

km = 1000.0


def str_dist(dist):
    """
    Return string representation of distance.
    """
    if dist < 10.0:
        return "%g m" % dist
    elif 10.0 <= dist < 1.0 * km:
        return "%.0f m" % dist
    elif 1.0 * km <= dist < 10.0 * km:
        return "%.1f km" % (dist / km)
    else:
        return "%.0f km" % (dist / km)
