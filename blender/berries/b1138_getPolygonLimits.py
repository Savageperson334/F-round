# getPolygonLimits
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/dataprocessing.py, line 228
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getPolygonLimits(polygon):
    polygonXMin, polygonXMax = float("inf"), float("-inf")
    polygonYMin, polygonYMax = float("inf"), float("-inf")

    for coordPair in polygon:
        y, x = coordPair
        polygonYMin = min(y, polygonYMin)
        polygonYMax = max(y, polygonYMax)
        polygonXMin = min(x, polygonXMin)
        polygonXMax = max(x, polygonXMax)

    polygonYMin = int(round(polygonYMin, 0))
    polygonYMax = int(round(polygonYMax, 0))
    polygonXMin = int(round(polygonXMin, 0))
    polygonXMax = int(round(polygonXMax, 0))

    return polygonXMin, polygonXMax, polygonYMin, polygonYMax
