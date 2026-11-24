# deg2km
#
# Copied verbatim from https://github.com/krischer/jane
#   file src/jane/documents/utils.py, line 6
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def deg2km(degrees):
    """
    Utility function converting degrees to kilometers.
    """
    radius = 6371.0
    return degrees * (2.0 * radius * math.pi / 360.0)
