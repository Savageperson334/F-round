# lerp
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 617
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lerp(a, b, t):
    """ Returns the linear interpolation between a and b at time t between 0.0-1.0.
        For example: lerp(100, 200, 0.5) => 150.
    """
    if t < 0.0:
        return a
    if t > 1.0:
        return b
    return a + (b - a) * t
