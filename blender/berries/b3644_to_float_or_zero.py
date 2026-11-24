# to_float_or_zero
#
# Copied verbatim from https://github.com/steven65026502/QGIS-S111-Viewer
#   file scripts/rebuild_direction_speed_gate_outputs.py, line 111
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Ocean currents and fluid dynamics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_float_or_zero(value) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return 0.0
    return result if result == result else 0.0
