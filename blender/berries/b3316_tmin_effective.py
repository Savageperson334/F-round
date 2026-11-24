# tmin_effective
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/util.py, line 1452
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tmin_effective(tmin, tmax, tduration, tposition):
    if None in (tmin, tmax, tduration, tposition):
        return tmin
    else:
        return tmin + (tmax - tmin) * tposition
