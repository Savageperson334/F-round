# normalize
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/web/oauth/__init__.py, line 75
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_diacritics = {
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


def utf8(string):
    return isinstance(string, str) and string.encode("utf-8") or str(string)


def normalize(string):
    # Normalize accents (é => e) for services that have problems with utf-8
    # (used to be the case with Yahoo BOSS but this appears to be fixed now).
    string = utf8(string)
    for k, v in _diacritics.items():
        for v in v:
            string = string.replace(v, k)
    return string
