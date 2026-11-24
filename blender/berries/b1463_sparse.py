# sparse
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/__init__.py, line 869
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def sparse(v):
    """ Returns the vector with features that have weight 0 removed.
    """
    for f, w in list(v.items()):
        if w == 0:
            del v[f]
    return v
