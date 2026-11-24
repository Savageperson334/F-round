# gf_inv
#
# Copied verbatim from https://github.com/daniestevez/gr-satellites
#   file python/bch15.py, line 29
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

exp_table = [8, 4, 2, 1, 12, 6, 3, 13, 10, 5, 14, 7, 15, 11, 9]

log_table = [3, 2, 6, 1, 9, 5, 11, 0, 14, 8, 13, 4, 7, 10, 12]


def gf_inv(x):
    if x == 0:
        raise ValueError
    return exp_table[-log_table[x-1] % len(exp_table)]
