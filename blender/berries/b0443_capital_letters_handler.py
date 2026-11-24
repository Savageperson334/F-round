# capital_letters_handler
#
# Copied verbatim from https://github.com/LazoVelko/Braille-Translator
#   file alphaToBraille.py, line 64
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Braille and tactile information
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

CAPITAL = chr(10272)


def capital_letters_handler(word):
    # Put the capital escape code before each capital letter.
    if word == "":
        return word
    result = ""
    for char in word:
        if char.isupper():
            result += CAPITAL + char.lower()
        else:
            result += char.lower()
    return result
