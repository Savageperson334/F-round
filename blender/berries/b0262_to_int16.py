# to_int16
#
# Copied verbatim from https://github.com/GRiMMBIENT/grimm
#   file tools/sampleio.py, line 352
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def peak(x, floor=1e-9):
    return max(floor, max(map(abs, x)))


def to_int16(x, norm=True):
    """mono float -> int16 list, peak normalised to 30000 (GR!MM: norm False, its level as it is)"""
    pk = peak(x)
    return [max(-32768, min(32767, int(v / pk * 30000 if norm else v * 32768))) for v in x]
