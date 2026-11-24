# predicative
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/de/inflect.py, line 560
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def predicative(adjective):
    """ Returns the predicative adjective (lowercase).
        In German, the attributive form preceding a noun is always used:
        "ein kleiner Junge" => strong, masculine, nominative,
        "eine schöne Frau" => mixed, feminine, nominative,
        "der kleine Prinz" => weak, masculine, nominative, etc.
        The predicative is useful for lemmatization.
    """
    w = adjective.lower()
    if len(w) > 3:
        for suffix in ("em", "en", "er", "es", "e"):
            if w.endswith(suffix):
                b = w[:max(-len(suffix), -(len(w) - 3))]
                if b.endswith("bl"): # plausibles => plausibel
                    b = b[:-1] + "el"
                if b.endswith("pr"): # propres => proper
                    b = b[:-1] + "er"
                return b
    return w
