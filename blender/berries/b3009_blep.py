# blep
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/gen_lrry_tables.py, line 52
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rnd(x):
    return int(round(x))


def blep(M):
    fact = 1
    for i in range(2, M + 1):
        fact *= i
    t = []
    for i in range(M * 256 + 1):
        x = i / 256.0 - M / 2.0
        S = 0.0
        c = 1.0
        for k in range(M + 1):
            tt = x + M / 2.0 - k
            if tt > 0:
                S += (-1.0 if (k & 1) else 1.0) * c * (tt ** M)
            c = c * (M - k) / (k + 1)
        S /= fact
        t.append(rnd(S * 16777216.0))
    return t
