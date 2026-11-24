# psv_surface_ind
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/cake.py, line 1193
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

S = 2


def psv_surface_ind(in_mode, out_mode):
    '''
    Get indices to select the appropriate element from scatter matrix for free
    surface.
    '''

    return (int(in_mode == S), int(out_mode == S))
