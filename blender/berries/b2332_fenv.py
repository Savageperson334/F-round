# fenv
#
# Copied verbatim from https://github.com/isod89/clipper-fm1
#   file tools/gen_clipper_sets.py, line 70
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: isod89/clipper-pro
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def fenv(f, formants):
    """vowel envelope at f: sum of resonance peaks (freq, bandwidth, dB)"""
    e = np.zeros_like(f)
    for fc, bw, db in formants:
        e += 10 ** (db / 20) / (1 + ((f - fc) / (bw / 2)) ** 2)
    return e
