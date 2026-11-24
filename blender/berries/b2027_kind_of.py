# kind_of
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file gol_atlas.py, line 193
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def kind_of(values: np.ndarray) -> str:
    """What a column's logarithmic axis is, read off its values."""
    v = values[np.isfinite(values)]
    if not len(v):
        return "share"
    integral = bool(np.all(v == np.round(v)))
    if v.min() >= 0 and v.max() <= 1 and not integral:
        return "share"
    if v.min() > 0:
        return "pos"
    if v.min() >= 0:
        return "count"
    return "signed"
