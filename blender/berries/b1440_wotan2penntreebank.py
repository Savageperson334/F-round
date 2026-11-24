# wotan2penntreebank
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/nl/__init__.py, line 97
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

wotan = {
    "Adj(": (("vergr", "JJR"), ("overtr", "JJS"), ("", "JJ")),
    "Adv(": (("deel", "RP"), ("", "RB")),
    "Art(": (("", "DT"),),
   "Conj(": (("", "CC"),),
     "Int": (("", "UH"),),
    "Misc": (("symb", "SYM"), ("vreemd", "FW")),
      "N(": (("eigen,ev", "NNP"), ("eigen,mv", "NNPS"), ("ev", "NN"), ("mv", "NNS")),
    "Num(": (("", "CD"),),
   "Prep(": (("inf", "TO"), ("", "IN")),
   "Pron(": (("bez", "PRP$"), ("", "PRP")),
   "Punc(": (("komma", ","), ("open", "("), ("sluit", ")"), ("schuin", "CC"), ("", ".")),
      "V(": (("hulp", "MD"), ("ott,3", "VBZ"), ("ott", "VBP"), ("ovt", "VBD"),
             ("verl", "VBN"), ("teg", "VBG"), ("", "VB"))
}


def wotan2penntreebank(token, tag):
    """ Converts a WOTAN tag to a Penn Treebank II tag.
        For example: bokkenrijders/N(soort,mv,neut) => bokkenrijders/NNS
    """
    for k, v in wotan.items():
        if tag.startswith(k):
            for a, b in v:
                if a in tag:
                    return (token, b)
    return (token, tag)
