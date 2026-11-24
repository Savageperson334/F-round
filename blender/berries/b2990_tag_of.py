# tag_of
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/cost_fit.py, line 124
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tag_of(val, se):
    if se is None:
        return "ONE RUN"
    if abs(val) < 2 * se or val == 0:
        return "BELOW NOISE"
    r = se / abs(val)
    return "GOOD" if r < 0.10 else "OK" if r < 0.25 else "LOW"
