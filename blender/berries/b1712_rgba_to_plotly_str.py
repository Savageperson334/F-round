# rgba_to_plotly_str
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/backends/plotly_backend.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def rgba_to_plotly_str(color) -> str:
    """Convert an RGBA tuple to a plotly-compatible color string."""
    if isinstance(color, str):
        return color
    if isinstance(color, (tuple, list, np.ndarray)):
        if len(color) == 4:
            r, g, b = [int(c * 255) if c <= 1 else int(c) for c in color[:3]]
            a = color[3]
            return f"rgba({r},{g},{b},{a})"
        elif len(color) == 3:
            r, g, b = [int(c * 255) if c <= 1 else int(c) for c in color]
            return f"rgb({r},{g},{b})"
    return str(color)
