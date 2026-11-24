# pitch
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/c64-music-extraction/notation/midi_score.py, line 85
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pitch(key):
    name = 'c cis d dis e f fis g gis a ais b'.split()[key % 12]
    marks = key // 12 - 4  # MIDI 60 is c' (middle C).
    return name + ("'" * marks if marks >= 0 else ',' * -marks)
