# kolmogorov
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 1178
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import exp


def kolmogorov(x):
    """ Returns the approximation of Kolmogorov's distribution of the two-sample test.
        For a sample of size m and a sample of size n,
        it is the probability that the maximum deviation > x / sqrt(m+n).
    """
    if x < 0.27:
        return 1.0
    if x > 3.2:
        return 0.0
    x = -2.0 * x * x
    k = 0
    for i in reversed(range(1, 27 + 1, 2)): # 27 25 23 ... 1
        k = (1 - k) * exp(x * i)
    return 2.0 * k
