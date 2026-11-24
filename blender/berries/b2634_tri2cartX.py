# tri2cartX
#
# Copied verbatim from https://github.com/marcoalopez/ternary_plots
#   file mpl_ternary.py, line 28
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tri2cartX(upper_apex, right_apex, left_apex):
    """ Converts ternary to Cartesian x coordinates."""
    return 0.5 * (upper_apex + 2 * right_apex) / (upper_apex + right_apex + left_apex)
