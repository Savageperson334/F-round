# effective_zhr
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/targets.py, line 309
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def effective_zhr(peak_zhr: float, days_from_peak: float, b_rise: float, b_decline: float) -> float:
    """IMO/NASA-MEO-style asymmetric log-linear decay: ZHR(t) = peak_zhr * 10^(-B*|t|).

    b_rise applies before peak (t < 0), b_decline at/after peak (t >= 0) — real
    showers commonly rise faster approaching peak than they decline afterward.

    CAVEAT: the canonical IMO/meteor-science formulation uses solar longitude
    (λ☉) as the time axis, not calendar days. This module already keys every
    shower's peak off peak_month/peak_day (see _resolve_peak_year_offset), so
    using calendar-day offset here is a deliberate simplification consistent
    with the rest of the module. Solar longitude advances ~0.9856°/day on
    average, so B values (per degree of solar longitude) carry over to
    per-day within ~1.5% error most of the year — except near perihelion
    (early January), where Earth moves ~3.4% faster than the mean rate,
    relevant to Quadrantids (peak Jan 3) and marginally Ursids (peak Dec 22).
    """
    if peak_zhr <= 0:
        return 0.0
    b = b_rise if days_from_peak < 0 else b_decline
    return peak_zhr * (10 ** (-b * abs(days_from_peak)))
