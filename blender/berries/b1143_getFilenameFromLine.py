# getFilenameFromLine
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/density.py, line 62
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def getFilenameFromLine(line):
    extensionStartIndex = line.find(".")
    extensionEndIndex = line[extensionStartIndex:].find(
        " ") + extensionStartIndex
    return line[:extensionEndIndex]
