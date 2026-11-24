# GPS_to_UTC
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 58
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def GPS_to_UTC(gps):
    offset = 315964800 + 16
    return gps + offset
