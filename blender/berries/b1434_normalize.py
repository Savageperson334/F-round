# normalize
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/en/wordnet/__init__.py, line 92
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

DIACRITICS = {
    "a": ("á", "ä", "â", "à", "å"),
    "e": ("é", "ë", "ê", "è"),
    "i": ("í", "ï", "î", "ì"),
    "o": ("ó", "ö", "ô", "ò", "ō", "ø"),
    "u": ("ú", "ü", "û", "ù", "ů"),
    "y": ("ý", "ÿ", "ý"),
    "s": ("š",),
    "c": ("ç", "č"),
    "n": ("ñ",),
    "z": ("ž",)
}


def normalize(word):
    """ Normalizes the word for synsets() or Sentiwordnet[] by removing diacritics
        (PyWordNet does not take unicode) and replacing spaces with underscores.
    """
    if not isinstance(word, str):
        word = str(word)
    if not isinstance(word, str):
        try:
            word = word.encode("utf-8", "ignore")
        except:
            pass
    for k, v in DIACRITICS.items():
        for v in v:
            word = word.replace(v, k)

    # Replace spaces with underscores
    word = word.replace(" ", "_")

    return word
