# isinteger
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/ext/png.py, line 2256
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def isinteger(x):
    try:
        return int(x) == x
    except (TypeError, ValueError):
        return False
