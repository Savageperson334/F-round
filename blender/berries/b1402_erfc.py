# erfc
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 1127
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import exp


def erfc(x):
    """ Returns the complementary error function at x.
    """
    z = abs(x)
    t = 1.0 / (1 + 0.5 * z)
    r = 0.0
    for y in (
      0.17087277,
     -0.82215223,
      1.48851587,
     -1.13520398,
      0.27886807,
     -0.18628806,
      0.09678418,
      0.37409196,
      1.00002368,
     -1.26551223):
        r = y + t * r
    r = t * exp(-z ** 2 + r)
    if x >= 0:
        return r
    return 2.0 - r
