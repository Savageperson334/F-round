# remove_unknown
#
# Copied verbatim from https://github.com/earthspecies/alp-data
#   notebook scripts/dataset_prep_notebooks/prep_barkley_canyon.ipynb (its code cells joined in order; line 462 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def remove_unknown(x: str):
    x = x.replace("Unknown,","")
    return x
