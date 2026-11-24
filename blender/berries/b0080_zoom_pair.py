# zoom_pair
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/plotting/view_zoom.py, line 23
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def zoom_pair(low: float, high: float, factor: float, anchor: float) -> tuple[float, float]:
    """Scale ``(low, high)`` by *factor* while keeping *anchor* in place."""
    return anchor - (anchor - low) * factor, anchor + (high - anchor) * factor
