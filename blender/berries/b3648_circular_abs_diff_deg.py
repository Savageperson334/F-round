# circular_abs_diff_deg
#
# Copied verbatim from https://github.com/steven65026502/QGIS-S111-Viewer
#   file scripts/validate_spatial_stats.py, line 106
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def circular_abs_diff_deg(a, b):
    diff = abs(a - b)
    return min(diff, 360.0 - diff)
