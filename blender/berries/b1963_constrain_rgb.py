# constrain_rgb
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file examples/galaxy_specrend.py, line 153
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def constrain_rgb(r, g, b):
    """
    If the requested RGB shade contains a negative weight for
    one of the primaries, it lies outside the colour gamut
    accessible from the given triple of primaries.  Desaturate
    it by adding white, equal quantities of R, G, and B, enough
    to make RGB all positive.  The function returns 1 if the
    components were modified, zero otherwise.
    """
    # Amount of white needed is w = - min(0, *r, *g, *b)
    w = -min([0, r, g, b]) # I think?

    # Add just enough white to make r, g, b all positive.
    if w > 0:
        r += w
        g += w
        b += w
    return(r,g,b)
