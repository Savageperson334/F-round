# split_token_by_words
#
# Copied verbatim from https://github.com/suralmasha/RuTranscript
#   file src/ru_transcript/tools/main_tools.py, line 146
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def split_token_by_words(token: str, words: list[str]) -> list[str]:
    """
    Split a stressed token by word lengths while preserving stress marks.

    param token: Stressed token that may contain '+' marks.
    param words: Text words matching the token without stress marks.
    return: Stressed token parts aligned to the given words.
    """
    result = []
    token_index = 0

    for word in words:
        part = []
        letters_seen = 0
        while token_index < len(token) and (letters_seen < len(word) or token[token_index] == '+'):
            char = token[token_index]
            part.append(char)
            token_index += 1
            if char != '+':
                letters_seen += 1
        result.append(''.join(part))

    return result
