# expand_quadratics
#
# Copied verbatim from https://github.com/fogleman/axi
#   file axi/paths.py, line 144
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from math import hypot


def quadratic_path(x0, y0, x1, y1, x2, y2):
    n = int(hypot(x1 - x0, y1 - y0) + hypot(x2 - x1, y2 - y1))
    n = max(n, 4)
    points = []
    m = 1 / float(n - 1)
    for i in range(n):
        t = i * m
        u = 1 - t
        a = u * u
        b = 2 * u * t
        c = t * t
        x = a * x0 + b * x1 + c * x2
        y = a * y0 + b * y1 + c * y2
        points.append((x, y))
    return points


def expand_quadratics(path):
    result = []
    previous = (0, 0)
    for point in path:
        if len(point) == 2:
            result.append(point)
            previous = point
        elif len(point) == 4:
            x0, y0 = previous
            x1, y1, x2, y2 = point
            result.extend(quadratic_path(x0, y0, x1, y1, x2, y2))
            previous = (x2, y2)
        else:
            raise Exception('invalid point: %r' % point)
    return result
