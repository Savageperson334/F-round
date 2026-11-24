# classify_weathering
#
# Copied verbatim from https://github.com/shikhovalf/Geochemistry-Interpretation-Tool
#   file app.py, line 119
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def classify_weathering(na_k):

    if na_k > 1:
        return "Weak weathering"

    elif 0.5 <= na_k <= 1:
        return "Moderate weathering"

    else:
        return "Intense weathering"
