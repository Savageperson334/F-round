# get_known_marker_size
#
# Copied verbatim from https://github.com/nion-software/nionswift
#   file nion/swift/model/LinePlotDisplay.py, line 240
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

DEFAULT_MARKER_SIZE = 6.0


def get_known_marker_size(marker_size: float | None) -> float:
    """Return the marker size in points if it is finite and above zero, or else the default."""
    return marker_size if marker_size is not None and math.isfinite(marker_size) and marker_size > 0 else DEFAULT_MARKER_SIZE
