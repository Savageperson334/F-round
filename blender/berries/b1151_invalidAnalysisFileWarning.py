# invalidAnalysisFileWarning
#
# Copied verbatim from https://github.com/bdavis222/dot-scanner
#   file dotscanner/strings.py, line 121
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def invalidAnalysisFileWarning(filepath):
    filename = filepath.split("/")[-1]
    return f'\nInvalid analysis file selected: "{filename}". A valid file has a .txt extension \
and contains density or lifetime data.'
