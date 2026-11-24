# check_color
#
# Copied verbatim from https://github.com/glumpy/glumpy
#   file glumpy/ext/png.py, line 318
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


def check_color(c, greyscale, which):
    """Checks that a colour argument for transparent or
    background options is the right form.  Returns the colour
    (which, if it's a bar integer, is "corrected" to a 1-tuple).
    """

    if c is None:
        return c
    if greyscale:
        try:
            l = len(c)
        except TypeError:
            c = (c,)
        if len(c) != 1:
            raise ValueError("%s for greyscale must be 1-tuple" %
                which)
        if not isinteger(c[0]):
            raise ValueError(
                "%s colour for greyscale must be integer" % which)
    else:
        if not (len(c) == 3 and
                isinteger(c[0]) and
                isinteger(c[1]) and
                isinteger(c[2])):
            raise ValueError(
                "%s colour must be a triple of integers" % which)
    return c
