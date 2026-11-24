# psv_solid_ind
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/cake.py, line 1249
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

DOWN = 4

S = 2

UP = -4


def psv_solid_ind(in_direction, out_direction, in_mode, out_mode):
    '''
    Get indices to select the appropriate element from scatter matrix for
    solid-solid interface.
    '''

    return (
        (out_direction == DOWN)*2 + (out_mode == S),
        (in_direction == UP)*2 + (in_mode == S))
