# radiance_to_sqm
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/darksky.py, line 450
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def radiance_to_sqm(radiance_nw: float) -> float:
    """
    VIIRS empirical regression (nW/cm²/sr → mag/arcsec²).
        SQM ≈ 21.7 − 2.5 × log10(L + 0.6)
    The 0.6 offset represents natural airglow in the VIIRS band.
    Accuracy: ±0.5–1.0 mag/arcsec² (one Bortle class).

    Returns the unrounded regression value. Quantise only at a display boundary
    (`_SQM_DISPLAY_DP`); `sqm_to_bortle`/`sqm_to_zone` take the full-precision value,
    since their thresholds are themselves fixed-decimal.
    """
    return 21.7 - 2.5 * math.log10(radiance_nw + 0.6)
