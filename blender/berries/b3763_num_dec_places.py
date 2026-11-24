# num_dec_places
#
# Copied verbatim from https://github.com/timpol/pysoplot
#   file src/pysoplot/misc.py, line 116
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def num_dec_places(n):
    """Return number of decimal digits in string representation of a decimal
    number.
    """
    s = str(n).rstrip("0")
    try:
        nd = s.split('.')[1]
    except IndexError:
        return 0
    return len(nd)
