# sqm_to_zone
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/darksky.py, line 488
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_LORENZ_ZONES = [
    (21.99, "1a"),
    (21.93, "1b"),
    (21.89, "2a"),
    (21.81, "2b"),
    (21.69, "3a"),
    (21.51, "3b"),
    (21.25, "4a"),
    (20.91, "4b"),
    (20.50, "5a"),
    (20.02, "5b"),
    (19.50, "6a"),
    (18.95, "6b"),
    (18.38, "7a"),
    (17.80, "7b"),
]


def sqm_to_zone(sqm: float) -> str:
    """Return the djlorenz light pollution zone label (e.g. '0', '1a', '3b')."""
    if sqm > 21.99:
        return "0"
    for min_sqm, label in _LORENZ_ZONES:
        if sqm >= min_sqm:
            return label
    return "7b"
