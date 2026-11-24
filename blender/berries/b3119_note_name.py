# note_name
#
# Copied verbatim from https://github.com/psav/punchbox
#   file punchbox/__init__.py, line 41
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_name(val):
    mod = val % 12
    name = "{}{}".format(NOTE_NAMES[mod], (val / 12) - 2)
    return name
