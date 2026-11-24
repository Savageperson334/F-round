# classify_salinity
#
# Copied verbatim from https://github.com/shikhovalf/Geochemistry-Interpretation-Tool
#   file app.py, line 107
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def classify_salinity(sr_ba):

    if sr_ba > 1:
        return "Marine–high salinity"

    elif 0.5 <= sr_ba <= 1:
        return "Brackish"

    else:
        return "Freshwater / restricted"
