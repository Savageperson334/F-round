# median
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 699
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def median(iterable, sort=True):
    """ Returns the value that separates the lower half from the higher half of values in the list.
    """
    s = sorted(iterable) if sort is True else list(iterable)
    n = len(s)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    if n % 2 == 0:
        return float(s[(n // 2) - 1] + s[n // 2]) / 2
    return s[n // 2]
