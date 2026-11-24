# fit
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/bench_quick.py, line 46
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

BLOCK_US_PER_PCT = 725.0 / 100.0


def fit(points):
    """points [(keys, avg_percent)] -> (cost per voice, fixed) in us per block, least squares"""
    if len(points) < 2:
        return (None, None)
    n = len(points)
    sx = sum(k for k, _ in points)
    sy = sum(a * BLOCK_US_PER_PCT for _, a in points)
    sxx = sum(k * k for k, _ in points)
    sxy = sum(k * a * BLOCK_US_PER_PCT for k, a in points)
    d = n * sxx - sx * sx
    if not d:
        return (None, None)
    b = (n * sxy - sx * sy) / d
    return (b, (sy - b * sx) / n)
