# tune
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/sampler/pt.py, line 37
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def tune(scale, acc_rate):
    """
    Tunes the temperature scaling parameter
    according to the acceptance rate over the last tune_interval:

    Rate    Variance adaptation
    ----    -------------------
    <0.001        x 0.8
    <0.05         x 0.9
    <0.2          x 0.95
    >0.5          x 1.05
    >0.75         x 1.1
    >0.95         x 1.2

    """

    # Switch statement
    if acc_rate < 0.001:
        # reduce by 15 percent
        scale *= 0.85
    elif acc_rate < 0.05:
        # reduce by 10 percent
        scale *= 0.9
    elif acc_rate < 0.2:
        # reduce by 5 percent
        scale *= 0.95
    elif acc_rate > 0.95:
        # increase by 15 percent
        scale *= 1.15
    elif acc_rate > 0.75:
        # increase by 10
        scale *= 1.10
    elif acc_rate > 0.5:
        # increase by 5 percent
        scale *= 1.05

    return scale
