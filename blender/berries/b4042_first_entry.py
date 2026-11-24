# first_entry
#
# Copied verbatim from https://github.com/ygd551/terra-incognita
#   file ros1_ws/scripts/tile_coverage.py, line 58
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def first_entry(track, tiles, half=12.5):
    """Sim time each tile was first entered (inf if never)."""
    d = np.abs(track[:, None, 1:] - tiles[None])                                  # (N, T, 3)
    inside = (d[..., 0] < half) & (d[..., 1] < half) & (d[..., 2] < 6.0)
    return np.where(inside.any(0), track[inside.argmax(0), 0], np.inf)
