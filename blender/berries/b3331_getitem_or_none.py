# getitem_or_none
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/gui/sparrow/snapshots.py, line 64
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getitem_or_none(items, i):
    try:
        return items[i]
    except IndexError:
        return None
