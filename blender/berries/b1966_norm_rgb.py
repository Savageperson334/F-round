# norm_rgb
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file examples/galaxy_specrend.py, line 201
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def norm_rgb(r, g, b):
    """
    Normalise RGB components so the most intense (unless all
    are zero) has a value of 1.
    """
    greatest = max([r, g, b])

    if greatest > 0:
        r /= greatest
        g /= greatest
        b /= greatest
    return(r, g, b)
