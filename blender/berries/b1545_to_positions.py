# to_positions
#
# Copied verbatim from https://github.com/danmysak/ipa-parser
#   file src/ipaparser/_code/strings.py, line 35
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import unicodedata

StringPosition = str

StringPositions = tuple[StringPosition, ...]


def to_positions(string: str) -> StringPositions:
    start_indices = [index for index in range(len(string)) if index == 0 or not unicodedata.combining(string[index])]
    return tuple(string[start:end] for start, end in zip(start_indices, start_indices[1:] + [len(string)]))
