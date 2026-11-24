# predicative
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/it/inflect.py, line 443
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

adjective_predicative = {
       "bei": "bello",
       "bel": "bello",
     "bell'": "bello",
     "begli": "bello",
      "buon": "buono",
     "buon'": "buona",
      "gran": "grande",
    "grand'": "grande",
    "grandi": "grande",
       "san": "santo",
     "sant'": "santa"
}


def predicative(adjective):
    """ Returns the predicative adjective.
    """
    w = adjective.lower()
    if w in adjective_predicative:
        return adjective_predicative[w]
    if w.endswith("ari"):
        return w + "o"
    if w.endswith(("ali", "ili", "esi", "nti", "ori")):
        return w[:-1] + "e"
    if w.endswith("isti"):
        return w[:-1] + "a"
    if w.endswith(("che", "ghe")):
        return w[:-2] + "a"
    if w.endswith(("chi", "ghi")):
        return w[:-2] + "o"
    if w.endswith("i"):
        return w[:-1] + "o"
    if w.endswith("e"):
        return w[:-1] + "a"
    return adjective
