# pad_to_multiple
#
# Copied verbatim from https://github.com/microsoft/haste
#   file hastelib/src/hastegeo/workflows/embed_buildings.py, line 334
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def pad_to_multiple(val: int, multiple: int) -> int:
    """Round *up* to next multiple."""
    return math.ceil(val / multiple) * multiple
