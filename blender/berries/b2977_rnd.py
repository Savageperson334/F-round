# rnd
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/convert_twin.py, line 71
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rnd(num, den):
    """round half away from zero of num / den (den > 0)"""
    return (2 * num + den) // (2 * den) if num >= 0 else -((2 * -num + den) // (2 * den))
