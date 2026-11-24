# default_supersample
#
# Copied verbatim from https://github.com/Flowm/satvis
#   file scripts/starmap/cubemap.py, line 226
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def default_supersample(size: int, width: int) -> int:
    """Samples per axis matched to the minification at the face centre, where it is hardest.

    A face-centre texel spans 2/N radians, i.e. size*pi/360 px/deg: 17.9 at 2048,
    against 40.8 at a corner.
    """
    ratio = (width / 360.0) / (size * np.pi / 360.0)
    # Capped at 4, because cost is quadratic; --supersample overrides it.
    return int(min(4, max(2, np.ceil(ratio))))
