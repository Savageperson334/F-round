# nice_ticks
#
# Copied verbatim from https://github.com/ohlincha/crosstitrate
#   file crosstitrate/gui/widgets.py, line 126
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Laboratories, geochemistry, chemistry and microscopes
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def nice_ticks(lo, hi, n=6):
    span = hi - lo
    if span <= 0 or not math.isfinite(span):
        return [lo]
    raw = span / max(n, 1)
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    ticks, x = [], math.ceil(lo / step) * step
    while x <= hi + step * 1e-9:
        ticks.append(0.0 if abs(x) < step * 1e-9 else x)
        x += step
    return ticks
