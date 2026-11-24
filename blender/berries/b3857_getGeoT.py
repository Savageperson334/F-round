# getGeoT
#
# Copied verbatim from https://github.com/uba/tathu
#   file tathu/utils.py, line 20
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getGeoT(extent, nlines, ncols):
    '''
    This function computes the resolution based on data dimensions.
    '''
    resx = (extent[2] - extent[0]) / ncols
    resy = (extent[3] - extent[1]) / nlines
    return [extent[0], resx, 0, extent[3] , 0, -resy]
