# smoothstep
#
# Copied verbatim from https://github.com/kiyotakali/Miru
#   file miru-mobile/android/gen_petals.py, line 19
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Obscure computers, languages, unusual interfaces
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, v))


def smoothstep(e0, e1, x):
    t = clamp((x - e0) / (e1 - e0))
    return t * t * (3 - 2 * t)
