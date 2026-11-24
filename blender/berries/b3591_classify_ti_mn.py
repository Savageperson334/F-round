# classify_ti_mn
#
# Copied verbatim from https://github.com/shikhovalf/Geochemistry-Interpretation-Tool
#   file app.py, line 146
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def classify_ti_mn(ti_mn):

    if ti_mn >= 110:
        return "Continental (alluvial)"

    elif 20 <= ti_mn < 110:
        return "Nearshore, high detrital input"

    elif 7 <= ti_mn < 20:
        return "Shallow marine, variable salinity"

    else:
        return "Open marine / distal"
