# fill
#
# Copied verbatim from https://github.com/fatiando/fatiando
#   file cookbook/mesher_prismmesh_filter.py, line 13
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fill(i):
    if i % 2 == 0:
        return 1
    return -1
