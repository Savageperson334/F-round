# alpha4
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/aa_raster.py, line 37
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def alpha4(v, gamma=1.0):
    """0..255 coverage -> 0..15; gamma < 1 makes thin light-on-dark text bolder."""
    return min(15, int(round(15.0 * ((v / 255.0) ** gamma))))
