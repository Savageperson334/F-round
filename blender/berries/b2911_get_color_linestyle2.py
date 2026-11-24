# get_color_linestyle2
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/plthelpers.py, line 600
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_color_linestyle2(i):
    colors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7"]
    markers = ["-", "--", ":", "-."]
    return markers[i % len(markers)] + colors[i // len(markers)]
