# parole2penntreebank
#
# Copied verbatim from https://github.com/clips/pattern
#   file pattern/text/es/__init__.py, line 146
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

parole = {
    "AO": "JJ",   # primera
    "AQ": "JJ",   # absurdo
    "CC": "CC",   # e
    "CS": "IN",   # porque
    "DA": "DT",   # el
    "DD": "DT",   # ese
    "DI": "DT",   # mucha
    "DP": "PRP$", # mi, nuestra
    "DT": "DT",   # cuántos
    "Fa": ".",    # !
    "Fc": ",",    # ,
    "Fd": ":",    # :
    "Fe": "\"",   # "
    "Fg": ".",    # -
    "Fh": ".",    # /
    "Fi": ".",    # ?
    "Fp": ".",    # .
    "Fr": ".",    # >>
    "Fs": ".",    # ...
   "Fpa": "(",    # (
   "Fpt": ")",    # )
    "Fx": ".",    # ;
    "Fz": ".",    #
     "I": "UH",   # ehm
    "NC": "NN",   # islam
   "NCS": "NN",   # guitarra
   "NCP": "NNS",  # guitarras
    "NP": "NNP",  # Óscar
    "P0": "PRP",  # se
    "PD": "DT",   # ése
    "PI": "DT",   # uno
    "PP": "PRP",  # vos
    "PR": "WP$",  # qué
    "PT": "WP$",  # qué
    "PX": "PRP$", # mío
    "RG": "RB",   # tecnológicamente
    "RN": "RB",   # no
    "SP": "IN",   # por
   "VAG": "VBG",  # habiendo
   "VAI": "MD",   # había
   "VAN": "MD",   # haber
   "VAS": "MD",   # haya
   "VMG": "VBG",  # habiendo
   "VMI": "VB",   # habemos
   "VMM": "VB",   # compare
   "VMN": "VB",   # comparecer
   "VMP": "VBN",  # comparando
   "VMS": "VB",   # compararan
   "VSG": "VBG",  # comparando
   "VSI": "VB",   # será
   "VSN": "VB",   # ser
   "VSP": "VBN",  # sido
   "VSS": "VB",   # sea
     "W": "NN",   # septiembre
     "Z": "CD",   # 1,7
    "Zd": "CD",   # 1,7
    "Zm": "CD",   # £1,7
    "Zp": "CD",   # 1,7%
}


def parole2penntreebank(token, tag):
    """ Converts a Parole tag to a Penn Treebank II tag.
        For example: importantísimo/AQ => importantísimo/ADJ
    """
    return (token, parole.get(tag, tag))
