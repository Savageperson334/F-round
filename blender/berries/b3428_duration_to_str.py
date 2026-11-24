# duration_to_str
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/squirrel/model.py, line 1327
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def duration_to_str(t):
    if t > 24*3600:
        return '%gd' % (t / (24.*3600.))
    elif t > 3600:
        return '%gh' % (t / 3600.)
    elif t > 60:
        return '%gm' % (t / 60.)
    else:
        return '%gs' % t
