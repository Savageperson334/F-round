# fmt
#
# Copied verbatim from https://github.com/steven65026502/QGIS-S111-Viewer
#   file scripts/validate_spatial_stats.py, line 231
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def fmt(value, digits=9):
    if value is None or not math.isfinite(float(value)):
        return "nan"
    return f"{float(value):.{digits}f}"
