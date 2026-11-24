# onset
#
# Copied verbatim from https://github.com/GRiMMBIENT/grimm
#   file tools/sampleio.py, line 196
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: genkigenki/Speak37, isod89/clipper-fm1, isod89/clipper-pro, jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def peak(x, floor=1e-9):
    return max(floor, max(map(abs, x)))


def onset(x, rel=0.02):
    """index of the first sample above rel x peak"""
    thr = rel * peak(x)
    return next((i for i, v in enumerate(x) if abs(v) > thr), 0)
