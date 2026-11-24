# k_ext_from_aod
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/moonlight.py, line 130
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

_AOD_CAP = 3.0

_MAG_PER_TAU = 2.5 * math.log10(math.e)

_TAU_ABS     = 0.016

_KS_K_EXT        = 0.172

_TAU_RAY     = 0.1066

_AOD_REF = _KS_K_EXT / _MAG_PER_TAU - _TAU_RAY - _TAU_ABS


def k_ext_from_aod(aod: "float | None") -> float:
    """V-band extinction coefficient (mag/airmass) for a given AOD; None → reference sky (0.172)."""
    tau_m = _AOD_REF if aod is None else min(max(0.0, aod), _AOD_CAP)
    return _MAG_PER_TAU * (_TAU_RAY + tau_m + _TAU_ABS)
