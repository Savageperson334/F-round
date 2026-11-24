# replace_stress_before
#
# Copied verbatim from https://github.com/suralmasha/RuTranscript
#   file src/ru_transcript/tools/stress_tools.py, line 99
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def replace_stress_before(text: str | list[str]) -> list[str]:
    """
    Move the accent to the position before the stressed vowel.

    param text: Input text as a string or a list of characters.
    return: List of characters with the accent moved before the stressed vowel.
    """
    if isinstance(text, str):
        text = list(text)

    text_copy = text.copy()
    for i, char in enumerate(text):
        if char == '+':
            text_copy.pop(i)  # remove the old accent
            text_copy.insert(i - 1, '+')  # insert it before the vowel
    return text_copy
