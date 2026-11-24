# apply_differences
#
# Copied verbatim from https://github.com/suralmasha/RuTranscript
#   file src/ru_transcript/tools/main_tools.py, line 21
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def apply_differences(words: list[str]) -> str:
    """
    Apply character-level differences from the second word to the first word.

    param words: A list containing two strings: [original_word, changed_word].
                  The changed_word may contain '+' symbols to ignore.
    return: A new string where differences from changed_word are applied to original_word.
    """
    original, changed = words
    # Remove '+' for comparison
    clean_changed = changed.replace('+', '')

    # Record positions where characters differ
    differences = {i: c2 for i, (c1, c2) in enumerate(zip(original, clean_changed, strict=True)) if c1 != c2}

    # Apply differences while skipping '+' symbols
    new_word = []
    skip_count = 0
    for i, c in enumerate(changed):
        if c == '+':
            skip_count += 1
            continue
        index = i - skip_count
        new_word.append(differences.get(index, c))

    return ''.join(new_word)
