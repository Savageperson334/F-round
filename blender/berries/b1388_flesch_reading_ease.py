# flesch_reading_ease
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/metrics.py, line 349
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def flesch_reading_ease(string):
    """ Returns the readability of the string as a value between 0.0-1.0:
        0.30-0.50 (difficult) => 0.60-0.70 (standard) => 0.90-1.00 (very easy).
    """
    def count_syllables(word, vowels="aeiouy"):
        n = 0
        p = False # True if the previous character was a vowel.
        for ch in word.endswith("e") and word[:-1] or word:
            v = ch in vowels
            n += int(v and not p)
            p = v
        return n
    if not isinstance(string, str):
        raise TypeError("%s is not a string" % repr(string))
    if len(string) < 3:
        return 1.0
    if len(string.split(" ")) < 2:
        return 1.0
    string = string.strip()
    string = string.strip("\"'().")
    string = string.lower()
    string = string.replace("!", ".")
    string = string.replace("?", ".")
    string = string.replace(",", " ")
    string = " ".join(string.split())
    y = [count_syllables(w) for w in string.split() if w != ""]
    w = max(1, len([w for w in string.split(" ") if w != ""]))
    s = max(1, len([s for s in string.split(".") if len(s) > 2]))
    #R = 206.835 - 1.015 * w/s - 84.6 * sum(y)/w
    # Use the Farr, Jenkins & Patterson algorithm,
    # which uses simpler syllable counting (count_syllables() is the weak point here).
    R = 1.599 * sum(1 for v in y if v == 1) * 100 / w - 1.015 * w / s - 31.517
    R = max(0.0, min(R * 0.01, 1.0))
    return R
