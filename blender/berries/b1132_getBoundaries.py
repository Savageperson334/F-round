# getBoundaries
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/dataprocessing.py, line 67
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getBoundaries(yStart, xStart, stepSize):
    return {
        "top": yStart - stepSize,
        "bottom": yStart + stepSize,
        "left": xStart - stepSize,
        "right": xStart + stepSize
    }
