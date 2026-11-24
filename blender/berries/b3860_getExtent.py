# getExtent
#
# Copied verbatim from https://github.com/uba/tathu
#   file tathu/utils.py, line 52
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getExtent(gt, shape):
    '''
    This function returns the extent based on the given GDAL
    geo-transform parameters and dimensions.
    '''
    llx = gt[0]
    lly = gt[3] + ((shape[0]) * gt[5])
    urx = gt[0] + ((shape[1])  * gt[1])
    ury = gt[3]
    return (llx, lly, urx, ury)
