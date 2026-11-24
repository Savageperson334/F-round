# heading
#
# Copied verbatim from https://github.com/adamhuda172/neptune4-pen-plotter
#   file image_to_gcode.py, line 149
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def heading(p, at_end, reach=0.6):
    """Unit direction a stroke travels at its start (or end), measured over
    `reach` mm so pixel noise doesn't dominate."""
    q = p[::-1] if at_end else p
    dist = np.hypot(*(q - q[0]).T)
    far = q[min(np.searchsorted(dist, reach), len(q) - 1)]
    v = (q[0] - far) if at_end else (far - q[0])
    n = np.hypot(*v)
    return v / n if n else v
