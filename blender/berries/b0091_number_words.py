# number_words
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/learning/guard.py, line 103
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_SCALES = ((10**9, "billion"), (10**6, "million"), (1000, "thousand"))

_ONES = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

_TENS = ["_", "_", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def _under_thousand(n: int) -> list[str]:
    words: list[str] = []
    if n >= 100:
        words += [_ONES[n // 100], "hundred"]
        n %= 100
    if n >= 20:
        words.append(_TENS[n // 10])
        n %= 10
        if n:
            words.append(_ONES[n])
    elif n:
        words.append(_ONES[n])
    return words


def number_words(n: int) -> str:
    """English words for a non-negative integer below 10**12, "and" omitted."""
    if n == 0:
        return "zero"
    words: list[str] = []
    for scale, name in _SCALES:
        if n >= scale:
            words += [*_under_thousand(n // scale), name]
            n %= scale
    words += _under_thousand(n)
    return " ".join(words)
