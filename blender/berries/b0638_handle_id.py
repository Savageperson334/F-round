# handle_id
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/schemas/utils.py, line 80
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def handle_id(side: str, idx: int) -> str:
    """The source handle ID at a given slot index for a side."""
    return side if idx == 0 else f"{side}-{idx + 1}"
