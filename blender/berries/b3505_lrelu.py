# lrelu
#
# Copied verbatim from https://github.com/quantumiracle/Reinforcement_Learning_for_Traffic_Light_Control
#   file 6.ddpg_for_single/common/tf_util.py, line 31
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lrelu(x, leak=0.2):
    f1 = 0.5 * (1 + leak)
    f2 = 0.5 * (1 - leak)
    return f1 * x + f2 * abs(x)
