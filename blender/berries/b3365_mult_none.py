# mult_none
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/model/event.py, line 82
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mult_none(a, b):
    if None in (a, b):
        return None
    else:
        return a*b
