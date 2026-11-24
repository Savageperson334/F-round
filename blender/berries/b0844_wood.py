# wood
#
# Copied verbatim from https://github.com/agilescientific/bruges
#   file bruges/rockphysics/fluids.py, line 12
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def wood(Kf1, Kf2, Sf1):
    """
    Wood's equation, per equation 35b in Batzle and Wang (1992).
    """
    return 1 / ((Sf1 / Kf1) + ((1 - Sf1) / Kf2))
