# sid_dac_bits
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/melodee/upstream/tools/gen_tables.py, line 148
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def sid_dac_bits(bits, r2r, term):
    """reSID 1.0 dac.cc build_dac_table: the voltage each bit of an R-2R ladder gives on its own, 2R / R = r2r,
    term: terminated (8580) or not (6581); any code is the sum of its bits (superposition)"""
    vbit = []
    for set_bit in range(bits):
        vn, r, r2 = 1.0, 1.0, r2r
        rn = r2 if term else math.inf
        for _ in range(set_bit):                    # the "tail" below the bit, by parallel substitution
            rn = r + r2 if rn == math.inf else r + r2 * rn / (r2 + rn)
        if rn == math.inf:                          # source transformation for the bit's voltage
            rn = r2
        else:
            rn = r2 * rn / (r2 + rn)
            vn = vn * rn / r2
        for _ in range(set_bit + 1, bits):          # up to the output, by repeated source transformation
            rn += r
            i = vn / rn
            rn = r2 * rn / (r2 + rn)
            vn = rn * i
        vbit.append(vn * ((1 << bits) - 1))
    return vbit
