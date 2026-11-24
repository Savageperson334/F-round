# get_node2coordinates
#
# Copied verbatim from https://github.com/lens-biophotonics/ZetaStitcher
#   file zetastitcher/gaussian_stitcher/qp/stitching.py, line 9
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Microscopy & small worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_node2coordinates(x, nodes, n_dims):
    node2coordinates = {}
    for idx, v in enumerate(nodes):
        node2coordinates[v] = x[idx*n_dims: (idx+1)*n_dims]
    return node2coordinates
