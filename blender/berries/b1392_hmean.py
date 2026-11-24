# hmean
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 692
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def hmean(iterable):
    """ Returns the harmonic mean of the given list of values.
    """
    a = iterable if isinstance(iterable, list) else list(iterable)
    return float(len(a)) / sum(1.0 / x for x in a)
