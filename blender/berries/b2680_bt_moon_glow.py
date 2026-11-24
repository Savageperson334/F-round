# bt_moon_glow
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/milky_way.py, line 159
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_BT_CHAR_ALT    = 40.0

_BT_MAX_DEP     = 5.0

_BT_PHASE_GAMMA = 1.8


def bt_moon_glow(moon_alt_deg: float, illum_frac: float) -> float:
    """Moon sky glow with K&S phase correction and post-moonset fade (0–1 scale)."""
    max_dep = _BT_MAX_DEP * illum_frac
    if moon_alt_deg <= -max_dep:
        return 0.0
    fade    = (moon_alt_deg + max_dep) / max_dep if moon_alt_deg < 0 else 1.0
    eff_alt = max(moon_alt_deg, 0.0)
    phase_b = illum_frac ** _BT_PHASE_GAMMA
    return fade * phase_b / (1.0 + (eff_alt / _BT_CHAR_ALT) ** 2)
