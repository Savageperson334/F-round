# nelm_from_sqm
#
# Copied verbatim from https://github.com/mbeher2200/DarkHours
#   file darkhours/moonlight.py, line 136
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def nelm_from_sqm(sqm: float) -> float:
    """
    Naked-eye limiting magnitude for a sky of surface brightness sqm
    (mag/arcsec²), via the standard Schaefer-derived conversion
    (Unihedron form): NELM = 7.93 − 5·log10(10^(4.316 − SQM/5) + 1).
    """
    return 7.93 - 5.0 * math.log10(10 ** (4.316 - sqm / 5.0) + 1.0)
