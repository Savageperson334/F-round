# findIndexOfMaxElement
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/dataprocessing.py, line 36
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def findIndexOfMaxElement(array):
    maxIndex = 0
    maxElement = float("-inf")
    for index, element in enumerate(array):
        if element > maxElement:
            maxElement = element
            maxIndex = index
    return maxIndex
