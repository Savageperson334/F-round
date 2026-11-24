# mean
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/__init__.py, line 1915
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mean(iterable, length=None):
    """ Returns the arithmetic mean of the values in the given iterable or iterator.
    """
    if length is None:
        if not hasattr(iterable, "__len__"):
            iterable = list(iterable)
        length = len(iterable)
    return sum(iterable) / float(length or 1)
