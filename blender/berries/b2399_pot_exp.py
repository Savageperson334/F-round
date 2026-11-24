# pot_exp
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/melodee110/upstream/tools/gen_909_tables.py, line 52
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import struct


def f32(x):
    return struct.unpack("<f", struct.pack("<f", x))[0]


def pot_exp(lo, hi, pot):
    """er99_pot_to_value for an EXP pot, in float as 9W9 evaluates it"""
    ratio = f32(f32(hi) / f32(lo))
    t = f32(pot / 127.0)
    return f32(f32(lo) * f32(ratio ** t))
