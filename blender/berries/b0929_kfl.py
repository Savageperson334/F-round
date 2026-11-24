# kfl
#
# Copied verbatim from https://github.com/agilescientific/in-bruges
#   notebook notebooks_dev/Fluidsubs_from_ezygeo-ai_for_checking.ipynb (its code cells joined in order; line 71 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def kfl(sw, khc, kw):
    '''
    K Fluid (C) hpratama 2020

    Input:
    sw = Water Saturation
    khc = K Hydrocarbon
    kw = K Water

    '''
    return ((sw/kw) + ((1-sw)/khc))**-1
