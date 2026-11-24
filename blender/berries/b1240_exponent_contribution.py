# exponent_contribution
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/c64-basic-v2-rnd-analysis/analysis/negative_seed_image.py, line 66
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def exponent_contribution(exponent: int, shifts: int) -> int:
    """Rounded integer added after reversing and normalizing the mantissa."""
    return ((exponent << shifts) + 0x80) >> 8
