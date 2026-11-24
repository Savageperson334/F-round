# extract_words
#
# Copied verbatim from https://github.com/LazoVelko/Braille-Translator
#   file alphaToBraille.py, line 15
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Braille and tactile information
#   the same function also appears in: firekim2/korean_to_braille
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def extract_words(string):
    # Split up a sentence based on whitespace (" ") and new line ("\n") chars.
    words = string.split(" ")
    result = []
    for word in words:
        temp = word.split("\n")
        for item in temp:
            result.append(item)
    return result
