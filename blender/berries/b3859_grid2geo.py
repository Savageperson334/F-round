# grid2geo
#
# Copied verbatim from https://github.com/uba/tathu
#   file tathu/utils.py, line 40
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def grid2geo(lin, col, geoT):
    '''
    This function returns the spatial location of a grid point.
    \param geoTransform A list of 6 coefficients describing an affine transformation to georeference a grid.
    \param col The grid point column.
    \param row The grid point row.
    \return The spatial location.
    '''
    x = col * geoT[1] + geoT[0]
    y = lin * geoT[5] + geoT[3]
    return x, y
