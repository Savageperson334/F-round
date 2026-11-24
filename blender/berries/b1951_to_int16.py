# to_int16
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/sampleio.py, line 267
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-fm1, isod89/clipper-pro, jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def peak(x, floor=1e-9):
    return max(floor, max(map(abs, x)))


def to_int16(x):
    """mono float -> int16 list, peak normalised to 30000"""
    pk = peak(x)
    return [max(-32768, min(32767, int(v / pk * 30000))) for v in x]
