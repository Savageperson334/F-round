# case_sensitive
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/vector/stemmer.py, line 319
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def case_sensitive(stem, word):
    """ Applies the letter case of the word to the stem:
        Ponies => Poni
    """
    ch = []
    for i in range(len(stem)):
        if word[i] == word[i].upper():
            ch.append(stem[i].upper())
        else:
            ch.append(stem[i])
    return "".join(ch)
