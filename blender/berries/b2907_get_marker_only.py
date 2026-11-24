# get_marker_only
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/plthelpers.py, line 578
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_marker_only(i):
    markers = ["o", "D", "^", "s", ">"]
    return markers[i % len(markers)]
