# attack
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file examples/effects/ladder/make_tables.py, line 37
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

Q = 1 << 23


def lookup(fn, k):
    """The 65-entry interpolated lookup the original ColdFire handler used."""
    if k == 127:
        return fn(127)
    v = fn(2 * (k // 2))
    return (v + fn(min(127, 2 * (k // 2) + 2))) // 2 if k & 1 else v


def stage_samples(k):   # ATK/DEC time curve: 1 ms .. 10 s, squared
    return 44100 * .001 * (1 + 99 * max(0, k - 1) / 126) ** 2


def attack(k):
    """Charge coefficient alpha (to 2x full scale, peak at full scale): bits 0-22
    mantissa, bit 23 set when the mantissa is alpha * 2^31 rather than * 2^23."""
    if not k:
        return Q - 1
    v = lookup(lambda k: max(1, round((1 << 31) * -math.expm1(-math.log(2) / stage_samples(k)))), k)
    return v >> 8 if v >= Q else v | Q
