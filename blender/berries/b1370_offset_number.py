# offset_number
#
# Copied verbatim from https://github.com/citiesskylines-csur/CSUR
#   file core/csur.py, line 20
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

EPS = 1e-6

LANEWIDTH = 3.75


def offset_number(x):
    if abs((x % LANEWIDTH) / LANEWIDTH - 0.5) < EPS:
        return "%d" % round(x / LANEWIDTH - 0.5)
    elif x % LANEWIDTH < EPS or x % LANEWIDTH > LANEWIDTH - EPS:
        return "%dP" % round(x / LANEWIDTH - 1)
    else:
        raise ValueError("Not standardized position of offset %.3f m" % x)
