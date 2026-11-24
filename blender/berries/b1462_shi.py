# shi
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/__init__.py, line 94
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def shi(i, base="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
    """ Returns a short string hash for a given int.
    """
    s = []
    while i > 0:
        i, r = divmod(i, len(base))
        s.append(base[r])
    return "".join(reversed(s))
