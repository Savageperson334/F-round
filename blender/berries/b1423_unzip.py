# unzip
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/tree.py, line 101
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def unzip(i, iterable):
    """ Returns the item at the given index from inside each tuple in the list.
    """
    return [x[i] for x in iterable]
