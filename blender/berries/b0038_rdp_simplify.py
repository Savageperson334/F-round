# rdp_simplify
#
# Copied verbatim from https://github.com/Animesh-Varma/BambuScribe
#   file backend/algorithms.py, line 650
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def rdp_simplify(points, epsilon=0.01):
    if len(points) <= 2:
        return points
    p1, p2 = points[0], points[-1]
    dx, dy = p2['x'] - p1['x'], p2['y'] - p1['y']
    line_len_sq = dx * dx + dy * dy

    dmax = 0.0
    index = 0
    if line_len_sq == 0:
        for i in range(1, len(points) - 1):
            d = math.hypot(points[i]['x'] - p1['x'], points[i]['y'] - p1['y'])
            if d > dmax:
                index, dmax = i, d
    else:
        sqrt_len = math.sqrt(line_len_sq)
        for i in range(1, len(points) - 1):
            cross = abs((points[i]['x'] - p1['x']) * dy - (points[i]['y'] - p1['y']) * dx)
            d = cross / sqrt_len
            if d > dmax:
                index, dmax = i, d

    if dmax > epsilon:
        res1 = rdp_simplify(points[:index + 1], epsilon)
        res2 = rdp_simplify(points[index:], epsilon)
        return res1[:-1] + res2
    else:
        return [points[0], points[-1]]
