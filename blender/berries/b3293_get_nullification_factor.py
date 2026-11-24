# get_nullification_factor
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/fomosto/psgrn_pscmp.py, line 670
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_nullification_factor(mu, lame_lambda):
    '''
    Factor that needs to be multiplied to 2 of the tensile sources to
    eliminate two of the isotropic components.
    '''
    return -lame_lambda / (2. * mu + 2. * lame_lambda)
