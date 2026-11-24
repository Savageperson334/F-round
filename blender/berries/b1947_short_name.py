# short_name
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/gen_vocab.py, line 628
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def short_name(name):
    """a bank's name in at most 6 characters: DAD JOKES 1 -> DAD 1, PERCUSSION -> PERC, SPELLING -> SPELL"""
    m = re.fullmatch(r"DAD JOKES (\d+)", name)
    if m:
        return "DAD " + m[1]
    return {"PERCUSSION": "PERC", "SPELLING": "SPELL", "MANTRAS": "MANTRA", "NUMBERS": "NUMBER"}.get(name, name[:6])
