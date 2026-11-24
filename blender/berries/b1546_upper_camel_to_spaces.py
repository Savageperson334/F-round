# upper_camel_to_spaces
#
# Copied verbatim from https://github.com/danmysak/ipa-parser
#   file src/ipaparser/_code/features/feature.py, line 13
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def upper_camel_to_spaces(string: str) -> str:
    result: list[str] = []
    for index, character in enumerate(string):
        if character.isupper():
            if index > 0:
                result.append(' ')
            result.append(character.lower())
        else:
            result.append(character)
    return ''.join(result)
