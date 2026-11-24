# overlap_fraction
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/6502-code-reuse/scripts/reuse_align6502.py, line 465
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def overlap_fraction(a_start: int, a_end: int, b_start: int, b_end: int) -> float:
    overlap = max(0, min(a_end, b_end) - max(a_start, b_start))
    denominator = min(a_end - a_start, b_end - b_start)
    return overlap / denominator if denominator else 0.0
