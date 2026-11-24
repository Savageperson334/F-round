# variance
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/db/__init__.py, line 498
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_sum = sum


def avg(list):
    """ Returns the arithmetic mean of the given list of values.
        For example: mean([1,2,3,4]) = 10/4 = 2.5.
    """
    return float(_sum(list)) / (len(list) or 1)


def variance(list):
    """ Returns the variance of the given list of values.
        The variance is the average of squared deviations from the mean.
    """
    a = avg(list)
    return _sum([(x - a)**2 for x in list]) / (len(list) - 1 or 1)
