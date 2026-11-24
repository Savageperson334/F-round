# get_trace_normalization_factor
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/fomosto/psgrn_pscmp.py, line 678
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_trace_normalization_factor(mu, lame_lambda, nullification):
    '''
    Factor to be multiplied to elementary GF trace to have unit displacement.
    '''
    return 1. / ((2. * mu) + lame_lambda + (2. * lame_lambda * nullification))
