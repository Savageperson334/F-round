# xy_toupvp
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file examples/galaxy_specrend.py, line 84
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def xy_toupvp(xc, yc):
    up = (4 * xc) / ((-2 * xc) + (12 * yc) + 3);
    vp = (9 * yc) / ((-2 * xc) + (12 * yc) + 3);
    return(up, vp)
