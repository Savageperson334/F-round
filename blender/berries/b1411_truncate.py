# truncate
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/db/__init__.py, line 2683
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def truncate(string, length=100):
    """ Returns a (head, tail)-tuple, where the head string length is less than the given length.
        Preferably the string is split at a space, otherwise a hyphen ("-") is injected.
    """
    if len(string) <= length:
        return string, ""
    n, words = 0, string.split(" ")
    for i, w in enumerate(words):
        if n + len(w) > length:
            break
        n += len(w) + 1
    if i == 0 and len(w) > length:
        return (w[:length - 1] + "-",
                (w[length - 1:] + " " + " ".join(words[1:])).strip())
    return (" ".join(words[:i]),
            " ".join(words[i:]))
