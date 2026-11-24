# pdf
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 1159
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import exp
from math import pi
from math import sqrt


def pdf(x, mean=0.0, stdev=1.0):
    """ Returns the probability density function at x:
        the likelihood of x in a distribution with given mean and standard deviation.
    """
    u = float(x - mean) / abs(stdev)
    return (1 / (sqrt(2 * pi) * abs(stdev))) * exp(-u * u / 2)
