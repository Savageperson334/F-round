# ols
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/cost_fit.py, line 105
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def mean(x):
    return sum(x) / len(x)


def ols(xs, ys):
    """y = a + s x. -> (a, s, se_a, se_s, n, rms); the errors need two spare points, else None"""
    n = len(xs)
    mx, my = mean(xs), mean(ys)
    sxx = sum((x - mx) ** 2 for x in xs)
    if n < 2 or sxx < 1e-9:
        return None
    s = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    a = my - s * mx
    if n > 2:
        sse = sum((y - a - s * x) ** 2 for x, y in zip(xs, ys))
        sig = math.sqrt(sse / (n - 2))
    else:
        sig = None
    return dict(a=a, s=s, n=n, sig=sig, sxx=sxx, mx=mx,
                se_s=(sig / math.sqrt(sxx) if sig is not None else None),
                se_a=(sig * math.sqrt(1.0 / n + mx * mx / sxx) if sig is not None else None))
