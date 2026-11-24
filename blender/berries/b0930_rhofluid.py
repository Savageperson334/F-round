# rhofluid
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Fluidsubs_from_ezygeo-ai_for_checking.ipynb (its code cells joined in order; line 151 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rhofluid(sw, so, rhoo, rhow):

    rho1 = ((1-so) * rhow) + (so * rhoo)
    rho2 = ((sw) * rhow) + ((1 - sw) * rhoo)
    return rho1, rho2
