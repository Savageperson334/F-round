# getYAndXFromCoordList
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/dataprocessing.py, line 269
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getYAndXFromCoordList(coordList):
    yList = []
    xList = []
    for coordPair in coordList:
        y, x = coordPair
        yList.append(y)
        xList.append(x)
    return yList, xList
