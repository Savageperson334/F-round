# kp_to_g_scale
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/aurora.py, line 184
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def kp_to_g_scale(kp: float) -> str | None:
    """NOAA geomagnetic-storm scale for a Kp value (G1 at Kp 5 … G5 at Kp 9)."""
    if kp < 5:
        return None
    return f"G{min(5, int(kp) - 4)}"
