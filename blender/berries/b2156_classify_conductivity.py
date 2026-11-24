# classify_conductivity
#
# Copied verbatim from https://github.com/highonicee/open-materials-explorer
#   file fetch_materials.py, line 11
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def classify_conductivity(bandgap: float) -> str:
    if bandgap is None:
        return "Unknown"
    elif bandgap < 0.1:
        return "Conductor"
    elif bandgap < 2:
        return "Semiconductor"
    elif bandgap < 4:
        return "Wide Bandgap"
    else:
        return "Insulator"
