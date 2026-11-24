# remove_extra_stresses
#
# Copied verbatim from https://github.com/suralmasha/RuTranscript
#   file src/ru_transcript/tools/stress_tools.py, line 88
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def remove_extra_stresses(string: str) -> str:
    """
    Keep only the first accent in the token and remove any additional accents.

    param string: Token that may contain multiple accents.
    return: Token with only the first accent retained.
    """
    first_plus_index = string.find('+')
    return string[: first_plus_index + 1] + string[first_plus_index + 1 :].replace('+', '')
