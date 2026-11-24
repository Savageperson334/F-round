# trim
#
# Copied verbatim from https://github.com/LazoVelko/Braille-Translator
#   file alphaToBraille.py, line 38
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Braille and tactile information
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def trim(word):
    # Remove punctuation around a word. Example: cat." becomes cat
    while len(word) is not 0 and not word[0].isalnum():
        word = word[1:]
    while len(word) is not 0 and not word[-1].isalnum():
        word = word[:-1]
    return word
