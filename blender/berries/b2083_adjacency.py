# adjacency
#
# Copied verbatim from https://github.com/graphoflife/GraphOfLife
#   file research/oee/checks/gliders.py, line 52
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Artificial life
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def adjacency(edges):
    adj = {}
    for x, y in edges:
        adj.setdefault(x, []).append(y)
        adj.setdefault(y, []).append(x)
    return adj
