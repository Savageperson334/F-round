# w_to_beta
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/sources.py, line 379
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as num

pi = num.pi


def w_to_beta(w, u_mapping=None, beta_mapping=None, n=1000):
    """
    Converts from  parameter w (Tape2015) to lune co-latitude
    """
    if beta_mapping is None:
        beta_mapping = num.linspace(0, pi, n)

    if u_mapping is None:
        u_mapping = (
            (3.0 / 4.0 * beta_mapping)
            - (1.0 / 2.0 * num.sin(2.0 * beta_mapping))
            + (1.0 / 16.0 * num.sin(4.0 * beta_mapping))
        )
    return num.interp(3.0 * pi / 8.0 - w, u_mapping, beta_mapping)
