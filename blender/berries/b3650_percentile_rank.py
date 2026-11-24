# percentile_rank
#
# Copied verbatim from https://github.com/steven65026502/QGIS-S111-Viewer
#   file scripts/validate_spatial_stats.py, line 119
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from bisect import bisect_left
from bisect import bisect_right


def percentile_rank(values_sorted, probe):
    if len(values_sorted) == 1:
        return 100.0
    left = bisect_left(values_sorted, probe)
    right = bisect_right(values_sorted, probe) - 1
    rank = (left + right) / 2.0
    return (rank / (len(values_sorted) - 1)) * 100.0
