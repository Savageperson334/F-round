# ConvertLogCoordString
#
# Copied verbatim from https://github.com/mjucker/pv_atmos
#   file basic.py, line 22
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ConvertLogCoordString(pString, basis=1e3):
    """Logarithmic coordinate conversion in string form for Calculator filter.

    Output is the string to be used inside the Calculator filter:
    pString -- the coordinate to convert
    basis   -- basis (surface) pressure to normalize
    """
    expression = '-log10(abs(' + pString + ')/' + str(basis) + ')'
    return expression
