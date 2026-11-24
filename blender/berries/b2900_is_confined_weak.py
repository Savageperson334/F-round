# is_confined_weak
#
# Copied verbatim from https://github.com/nu-radio/radiotools
#   file radiotools/helper.py, line 716
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sky, weather, satellites and unobservable phenomena
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def is_confined_weak(x, y, station_positions, delta_confinement=0):
    """ returns True if core (x, y coordinate) is confined within stations
        given by 'station_positions'. If the 'delta_confinement' parameter is
        given, the stations need this minimum distance to the core for the core
        to be confined. The criterion is weaker than in isConfined(). Here, at
        least one station has to be above, below, left or right the core position."""
    is_confined = (
        np.bool(np.sum([((x - delta_confinement) > sp_x) for (sp_x, sp_y, sp_z) in station_positions])) and
        np.bool(np.sum([((x + delta_confinement) < sp_x) for (sp_x, sp_y, sp_z) in station_positions])) and
        np.bool(np.sum([((y - delta_confinement) > sp_y) for (sp_x, sp_y, sp_z) in station_positions])) and
        np.bool(np.sum([((y + delta_confinement) < sp_y) for (sp_x, sp_y, sp_z) in station_positions])))
    return is_confined
