# intersects
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/tree.py, line 76
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def find(function, iterable):
    """ Returns the first item in the list for which function(item) is True, None otherwise.
    """
    for x in iterable:
        if function(x):
            return x


def intersects(iterable1, iterable2):
    """ Returns True if the given lists have at least one item in common.
    """
    return find(lambda x: x in iterable1, iterable2) is not None
