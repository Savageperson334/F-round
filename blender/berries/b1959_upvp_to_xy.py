# upvp_to_xy
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file examples/galaxy_specrend.py, line 79
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def upvp_to_xy(up, vp):
    xc = (9 * up) / ((6 * up) - (16 * vp) + 12)
    yc = (4 * vp) / ((6 * up) - (16 * vp) + 12)
    return(xc, yc)
