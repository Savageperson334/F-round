# allFilesAreNumbered
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/files.py, line 147
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def allFilesAreNumbered(filenames):
    for filename in filenames:
        digitFound = False

        for char in reversed(filename):
            if char.isdigit():
                digitFound = True
                break

        if not digitFound:
            return False

    return True
