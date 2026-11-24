# variance
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 711
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mean(iterable):
    """ Returns the arithmetic mean of the given list of values.
        For example: mean([1,2,3,4]) = 10/4 = 2.5.
    """
    a = iterable if isinstance(iterable, list) else list(iterable)
    return float(sum(a)) / (len(a) or 1)


def variance(iterable, sample=False):
    """ Returns the variance of the given list of values.
        The variance is the average of squared deviations from the mean.
    """
    # Sample variance = E((xi-m)^2) / (n-1)
    # Population variance = E((xi-m)^2) / n
    a = iterable if isinstance(iterable, list) else list(iterable)
    m = mean(a)
    return sum((x - m) ** 2 for x in a) / (len(a) - int(sample) or 1)
