# colors
#
# Copied verbatim from https://github.com/lmizrahi/etas
#   file etas/_figstyle.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

TEAL = "#43AEBA"

DARK = "#3A3937"

PALETTE = [DARK, TEAL, "#E69F00", "#CC79A7", "#0072B2", "#D55E00",
           "#56B4E9"]


def colors(n):
    """``n`` colours: dark gray first, then the categorical colours."""
    return [PALETTE[i % len(PALETTE)] for i in range(n)]
