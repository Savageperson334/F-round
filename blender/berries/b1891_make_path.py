# make_path
#
# Copied verbatim from https://github.com/fogleman/axi
#   file examples/growth.py, line 109
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from collections import defaultdict


def make_path(pairs):
    lookup = defaultdict(list)
    for parent, child in pairs:
        lookup[parent].append(child)
    root = pairs[0][0]
    path = []
    stack = []
    stack.append(root)
    while stack:
        point = stack[-1]
        path.append(point)
        if not lookup[point]:
            stack.pop()
            continue
        child = lookup[point].pop()
        stack.append(child)
    return path
