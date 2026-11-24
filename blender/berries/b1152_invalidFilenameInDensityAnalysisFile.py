# invalidFilenameInDensityAnalysisFile
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/strings.py, line 127
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def invalidFilenameInDensityAnalysisFile(lineArray):
    return f"Filename with valid extension not found in the following line in densities file:\n\
{' '.join(lineArray)}"
