# nelm
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/skyglow.py, line 77
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def nelm(msas: float) -> float:
    """Naked-eye limiting magnitude at the zenith from sky brightness
    (Schaefer 1990, in the form Unihedron publishes for the SQM)."""
    return 7.93 - 5.0 * math.log10(10 ** (4.316 - msas / 5.0) + 1.0)
