# compute_syndrome
#
# Copied verbatim from https://github.com/daniestevez/gr-satellites
#   file python/bch15.py, line 35
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

exp_table = [8, 4, 2, 1, 12, 6, 3, 13, 10, 5, 14, 7, 15, 11, 9]


def compute_syndrome(p, j):
    # Syndrome calculation by polynomial evaluation
    s = 0
    n = 15
    for k in range(n - 1, -1, -1):
        if p & 1:
            s ^= exp_table[(k * j) % len(exp_table)]
        p >>= 1
    return s
