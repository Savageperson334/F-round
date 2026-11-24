# ternary_to_cartesian
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/plotting/ternary.py, line 139
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_TERNARY_SQRT3 = 3.0 ** 0.5


def ternary_to_cartesian(t: float, l: float, r: float) -> tuple[float, float]:
    """Inverse of :func:`cartesian_to_ternary`: mpltern Cartesian coordinates for a composition."""
    return _TERNARY_SQRT3 * (float(r) - float(l)) / 3.0, float(t)
