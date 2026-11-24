# note_name
#
# Copied verbatim from https://github.com/etcetc000/kitbasher
#   file packs/pitch.py, line 21
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

NAMES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')


def note_name(note):
    n = math.floor(note + 1e-9)
    return f'{NAMES[n % 12]}{n // 12 - 2}{"+" if note - n > 0.25 else ""}'
