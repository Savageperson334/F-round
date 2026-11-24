# basic_truthy
#
# Copied verbatim from https://github.com/ringger/basicoco
#   file emulator/ast_nodes.py, line 13
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def basic_truthy(value) -> bool:
    """Convert a BASIC value to Python bool using CoCo semantics."""
    if isinstance(value, str):
        return len(value) > 0
    if isinstance(value, (int, float)):
        return bool(value)
    return value != 0
