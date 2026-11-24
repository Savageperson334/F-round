# interior_sliders
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file morphometrics/curves.py, line 80
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def interior_sliders(curve: list[int]) -> list[int]:
    """Sliding (interior) indices of one validated curve (endpoints pinned)."""
    return list(curve[1:-1])
