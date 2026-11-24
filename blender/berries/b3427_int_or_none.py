# int_or_none
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/model.py, line 180
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def int_or_none(x):
    if x is None:
        return None
    else:
        return int(x)
