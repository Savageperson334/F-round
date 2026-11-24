# handle_count_field
#
# Copied verbatim from https://github.com/Pouzor/homelable
#   file backend/app/schemas/utils.py, line 62
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def handle_count_field(side: str) -> str:
    """The `nodes` column storing a side's handle count."""
    return f"{side}_handles"
