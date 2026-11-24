# gamma
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 1039
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import exp
from math import log


def gammaln(x):
    """ Returns the natural logarithm of the gamma function at x.
    """
    x = x - 1.0
    y = x + 5.5
    y = (x + 0.5) * log(y) - y
    n = 1.0
    for i in range(6):
        x += 1
        n += (
          76.18009173,
         -86.50532033,
          24.01409822,
          -1.231739516e0,
           0.120858003e-2,
          -0.536382e-5)[i] / x
    return y + log(2.50662827465 * n)


def gamma(x):
    """ Returns the gamma function at x.
    """
    return exp(gammaln(x))
