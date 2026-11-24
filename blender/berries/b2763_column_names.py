# column_names
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/workflows/embed_buildings.py, line 477
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def column_names(num_bands: int) -> list[str]:
    """Feature column names for the mean reducer: f_0 .. f_{N-1}."""
    return [f"f_{i}" for i in range(num_bands)]
