# tmax_effective
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/util.py, line 1459
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tmax_effective(tmin, tmax, tduration, tposition):
    if None in (tmin, tmax, tduration, tposition):
        return tmax
    else:
        return tmin + (tmax - tmin) * tposition + tduration
