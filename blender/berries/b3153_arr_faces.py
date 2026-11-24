# arr_faces
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/geometry.py, line 25
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num


def arr_faces(obj):
    a = num.array(obj, dtype=num.int64)
    assert len(a.shape) == 2
    return a
