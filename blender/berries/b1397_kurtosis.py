# kurtosis
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 798
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


def moment(iterable, n=2, sample=False):
    """ Returns the n-th central moment of the given list of values
        (2nd central moment = variance, 3rd and 4th are used to define skewness and kurtosis).
    """
    if n == 1:
        return 0.0
    a = iterable if isinstance(iterable, list) else list(iterable)
    m = mean(a)
    return sum((x - m) ** n for x in a) / (len(a) - int(sample) or 1)


def kurtosis(iterable, sample=False):
    """ Returns the degree of peakedness of the given list of values:
        > 0.0 => sharper peak around mean(list) = more infrequent, extreme values,
        < 0.0 => wider peak around mean(list),
        = 0.0 => normal distribution,
        =  -3 => flat
    """
    a = iterable if isinstance(iterable, list) else list(iterable)
    return moment(a, 4, sample) / (moment(a, 2, sample) ** 2.0 or 1) - 3
