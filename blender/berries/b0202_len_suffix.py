# len_suffix
#
# Copied verbatim from https://github.com/ETCBC/phono
#   notebook programs/phono.ipynb (its code cells joined in order; line 1270 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

undefs = {"NA", "unknown", "n/a", "absent"}


def len_suffix(v):
    if v is None:
        return 0
    if v in undefs:
        return 0
    return len(v.replace("=", "").replace("W", "").replace("J", ""))
