# simplify_sparkline
#
# Copied verbatim from https://github.com/fogleman/axi
#   file examples/nes.py, line 23
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def simplify_sparkline(values, n):
    if not n:
        return values
    result = []
    previous = None
    for x, y in enumerate(values):
        if result:
            window = result[-n:]
            lo = min(window)
            hi = max(window)
            if y >= lo and y <= hi:
                result.append(result[-1])
                previous = y
                continue
        if previous is not None:
            result[-1] = previous
        result.append(y)
        previous = y
    return result
