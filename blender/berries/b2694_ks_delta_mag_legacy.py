# ks_delta_mag_legacy
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file scripts/verify_moonwash_grid.py, line 36
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

_LEGACY_K_EXT = 0.172


def ks_delta_mag_legacy(illumination_pct, sep_deg, moon_alt_deg,
                        sky_sqm=21.6, moon_earth_dist_km=384_400.0):
    if illumination_pct <= 0 or moon_alt_deg <= 0:
        return 0.0
    illum  = illumination_pct / 100.0
    alpha  = math.degrees(math.acos(max(-1.0, min(1.0, 2.0 * illum - 1.0))))
    V_moon = -12.73 + 0.026 * alpha + 4e-9 * alpha**4
    I_moon = 10 ** (-0.4 * (V_moon + 16.57))
    I_moon *= (384_400.0 / moon_earth_dist_km) ** 2
    alt    = max(1.0, moon_alt_deg)
    X_moon = 1.0 / math.cos(math.radians(90.0 - alt))
    ext    = 10 ** (-0.4 * _LEGACY_K_EXT * X_moon)
    rho     = max(0.1, sep_deg)
    rho_rad = math.radians(rho)
    if rho > 10.0:
        f_rho = 10 ** 5.36 * (1.06 + math.cos(rho_rad) ** 2)
    else:
        f_rho = 6.2e7 / rho ** 2
    I_scatter = f_rho * ext * I_moon
    I_sky     = 10 ** ((27.78 - sky_sqm) / 2.5)
    return 2.5 * math.log10(1.0 + I_scatter / I_sky)
