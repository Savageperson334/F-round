# resolve
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/gen_aa_icons.py, line 134
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def resolve(glyph, cps):
    """a glyph name, or a tuple of them: the first one the font has (the last one if none, reported missing)"""
    if isinstance(glyph, tuple):
        return next((g for g in glyph if g in cps), glyph[-1])
    return glyph
