# getLeftEdgeOfTrailingNumber
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/files.py, line 58
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getLeftEdgeOfTrailingNumber(string, index):
    if index == 0:
        return 0

    while index >= 0:
        if string[index].isdigit():
            index -= 1
        else:
            return index + 1
    return index + 1
