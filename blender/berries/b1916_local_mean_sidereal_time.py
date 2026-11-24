# local_mean_sidereal_time
#
# Copied verbatim from https://github.com/franklinbaldo/digicomp
#   file vendor/moira/sidereal_time_reference.py, line 83
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

J2000 = 2451545.0

JULIAN_CENTURY = 36525.0


def earth_rotation_angle(jd_ut: float) -> float:
    """
    Compute the Earth Rotation Angle (ERA) in degrees.

    Implements the IAU 2000 linear model (IERS Conventions 2010 §5.4.2;
    SOFA ``iauEra00``):

        ERA = 360 * (0.7790572732640 + 1.00273781191135448 * D)  mod 360

    where D = JD(UT1) − 2451545.0.

    Args:
        jd_ut: Julian Day Number in UT1.

    Returns:
        ERA in degrees, normalised to [0, 360).

    Raises:
        Nothing — pure arithmetic.

    Side effects:
        None.
    """
    # SOFA iauEra00 evaluation order: the whole turns carried by the Julian
    # day fraction are taken exactly, and only the 0.0027378... excess rate
    # multiplies the long baseline.  Multiplying the full 1.0027378... rate by
    # D instead loses ~0.3 mas at -2000 to binary64 rounding.
    D = jd_ut - J2000
    era_turns = math.fmod(jd_ut, 1.0) + 0.7790572732640 + 0.00273781191135448 * D
    return (era_turns % 1.0) * 360.0


def _greenwich_mean_sidereal_time_at_tt(jd_ut1: float, jd_tt: float) -> float:
    """IAU 2006 GMST: ERA at UT1, equinox precession polynomial at TT.

    Source: SOFA/ERFA gmst06 (Capitaine et al. 2003). No clock conversion is
    performed here; the caller owns both coordinates.  The native
    counterpart is ``greenwich_mean_sidereal_time(jd_ut, jd_tt)``.
    """
    D = jd_tt - J2000           # TT days from J2000.0
    T = D / JULIAN_CENTURY       # Julian centuries

    # Earth Rotation Angle (ERA) — IAU 2000 definition of UT1
    era_deg = earth_rotation_angle(jd_ut1)

    # Polynomial correction (arcseconds → degrees)
    poly_arcsec = (  0.014506
                   + 4612.156534    * T
                   +    1.3915817   * T**2
                   -    0.00000044  * T**3
                   -    0.000029956 * T**4
                   -    0.0000000368* T**5)

    return (era_deg + poly_arcsec / 3600.0) % 360.0


def greenwich_mean_sidereal_time(jd_ut1: float, jd_tt: float) -> float:
    """Return mean sidereal time (degrees) for an explicitly paired UT1/TT instant."""
    for name, value in (("jd_ut1", jd_ut1), ("jd_tt", jd_tt)):
        if not math.isfinite(value) or abs(value) > 40_000_000.0:
            raise ValueError(f"{name} must be finite and representable")
    return _greenwich_mean_sidereal_time_at_tt(jd_ut1, jd_tt)


def local_mean_sidereal_time(jd_ut1: float, jd_tt: float, longitude_east_deg: float) -> float:
    """Mean sidereal degrees with longitude positive east; no nutation."""
    if not math.isfinite(longitude_east_deg) or abs(longitude_east_deg) > 360.0:
        raise ValueError("longitude_east_deg must be finite in [-360,360]")
    return (greenwich_mean_sidereal_time(jd_ut1, jd_tt) + longitude_east_deg) % 360.0
