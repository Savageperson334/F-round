# cartesian_to_ternary
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/plotting/ternary.py, line 131
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_TERNARY_SQRT3 = 3.0 ** 0.5


def cartesian_to_ternary(x: float, y: float) -> tuple[float, float, float]:
    """Convert mpltern Cartesian data coordinates to (top, left, right) components."""
    t = float(y)
    r = ((1.0 - t) + _TERNARY_SQRT3 * float(x)) / 2.0
    l = (1.0 - t) - r
    return t, l, r
