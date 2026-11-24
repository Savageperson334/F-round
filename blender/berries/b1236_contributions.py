# contributions
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/c64-basic-v2-rnd-analysis/analysis/canonical_seed_domain.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MAX_INTERMEDIATE_EXPONENT = 0x98

MIN_INTERMEDIATE_EXPONENT = 0x7F


def contributions(shifts: int) -> tuple[int, ...]:
    return tuple(sorted({
        ((exponent << shifts) + 0x80) >> 8
        for exponent in range(MIN_INTERMEDIATE_EXPONENT, MAX_INTERMEDIATE_EXPONENT + 1)
    }))
