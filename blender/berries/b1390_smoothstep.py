# smoothstep
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 628
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def smoothstep(a, b, x):
    """ Returns the Hermite interpolation (cubic spline) for x between a and b.
        The return value between 0.0-1.0 eases (slows down) as x nears a or b.
    """
    if x < a:
        return 0.0
    if x >= b:
        return 1.0
    x = float(x - a) / (b - a)
    return x * x * (3 - 2 * x)
