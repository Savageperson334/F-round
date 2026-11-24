# luminance_to_sqm
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/darksky.py, line 464
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

_L_NATURAL   = 0.252

_SQM_NATURAL = 22.08


def luminance_to_sqm(la_mcd_m2: float) -> float:
    """
    Falchi physical model (mcd/m² artificial luminance → mag/arcsec²).
        SQM = 22.08 − 2.5 × log10((La + 0.252) / 0.252)
    0.252 mcd/m² is the Falchi (2016) natural sky reference.
    At La = 0: SQM = 22.08; at La = 0.252: SQM ≈ 21.3 (Bortle 3).

    Returns the unrounded model value, matching `radiance_to_sqm`. Both branches are
    now full precision — the La <= 0 branch always was, so the two exits agree.
    """
    if la_mcd_m2 <= 0.0:
        return _SQM_NATURAL
    return _SQM_NATURAL - 2.5 * math.log10(
        (la_mcd_m2 + _L_NATURAL) / _L_NATURAL)
