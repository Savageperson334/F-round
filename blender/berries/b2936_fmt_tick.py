# fmt_tick
#
# Copied verbatim from https://github.com/ohlincha/crosstitrate
#   file crosstitrate/gui/widgets.py, line 140
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Laboratories, geochemistry, chemistry and microscopes
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def fmt_tick(v, span):
    if span >= 50:
        return f"{v:.0f}"
    decimals = max(1, min(6, 1 - math.floor(math.log10(span / 5)))) if span > 0 else 2
    text = f"{v:.{decimals}f}"
    return text.rstrip("0").rstrip(".") if "." in text else text
