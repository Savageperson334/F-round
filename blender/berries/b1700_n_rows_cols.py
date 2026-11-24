# n_rows_cols
#
# Copied verbatim from https://github.com/ericmjl/nxviz
#   file nxviz/facet.py, line 74
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def n_rows_cols(groups):
    """Return squarest n_rows and n_cols combination."""
    nrows = ncols = int(np.ceil(np.sqrt(len(groups))))
    return nrows, ncols
