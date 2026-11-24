# deal_time
#
# Copied verbatim from https://github.com/HuberTRoy/MusicBox
#   file MusicPlayer/widgets/addition.py, line 6
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def deal_time(x):
    x = str(x)
    if len(x) == 1:
        x = '0' + x

    return x
