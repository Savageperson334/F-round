# phase_name_from_angle
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/sky_events.py, line 39
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

INTERMEDIATE_NAMES = ["Waxing Crescent", "Waxing Gibbous", "Waning Gibbous", "Waning Crescent"]

PRINCIPAL_PHASES = [
    (0,   "New Moon"),
    (90,  "First Quarter"),
    (180, "Full Moon"),
    (270, "Third Quarter"),
    (360, "New Moon"),
]

PRINCIPAL_WINDOW_DEG = 6.1


def phase_name_from_angle(angle_deg: float) -> str:
    """Phase name for a sun–moon elongation angle (0° = new, 180° = full)."""
    a = angle_deg % 360.0
    for p_angle, p_name in PRINCIPAL_PHASES:
        if abs(a - p_angle) <= PRINCIPAL_WINDOW_DEG:
            return p_name
    return INTERMEDIATE_NAMES[int(a // 90.0)]
