# supplied
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/6502-disassembly/scripts/region-evidence/region_evidence.py, line 31
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def supplied(text):
    if not isinstance(text, str) or not text.strip():
        raise ValueError('evidence must be a nonempty supplied reference/description')
    return {'status': 'supplied-not-automatically-proved', 'reference': text}
