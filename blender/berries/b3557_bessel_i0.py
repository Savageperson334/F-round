# bessel_i0
#
# Copied verbatim from https://github.com/romainguy/adrift
#   file tools/gen_dsp_tables.py, line 28
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def bessel_i0(x: float) -> float:
    term = 1.0
    total = 1.0
    half_x_sq = 0.25 * x * x
    k = 1
    while term > 1e-16 * total:
        term *= half_x_sq / (k * k)
        total += term
        k += 1
    return total
