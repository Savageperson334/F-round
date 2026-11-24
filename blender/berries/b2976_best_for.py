# best_for
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/comp_tables.py, line 30
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def best_for(tau_hops):
    """the coefficient m / 2^sh (m 1..255, sh 1..24) whose one-pole, per hop, has the time constant nearest to tau_hops"""
    k = 1 - math.exp(-1.0 / tau_hops)
    best = None
    for sh in range(1, 25):
        m = round(k * 2 ** sh)
        if m < 1 or m > 255 or m >= 2 ** sh:
            continue
        err = abs(-1 / math.log(1 - m / 2 ** sh) / tau_hops - 1)
        if best is None or err < best[0] - 1e-9:
            best = (err, m, sh)
    return best
