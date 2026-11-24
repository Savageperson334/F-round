# get_decl
#
# Copied verbatim from https://github.com/ETCBC/phono
#   notebook programs/phono.ipynb (its code cells joined in order; line 882 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_decl(lex_info):
    if lex_info is None:
        lex_info = ""
    parts = lex_info.split(",")
    return lex_info if len(parts) == 1 else parts[0]
