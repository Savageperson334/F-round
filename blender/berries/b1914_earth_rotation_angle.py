# earth_rotation_angle
#
# Copied verbatim from https://github.com/franklinbaldo/digicomp
#   file vendor/moira/sidereal_time_reference.py, line 20
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

J2000 = 2451545.0


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
