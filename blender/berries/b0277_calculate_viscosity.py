# calculate_viscosity
#
# Copied verbatim from https://github.com/GeoBen93/Viscosity_of_magmatic_melts
#   notebook magmatic_melt_viscosity_caluclator.ipynb (its code cells joined in order; line 102 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calculate_viscosity(T,A,B,C):
    viscosity = 10**(A + (B / (T - C)))
    return viscosity
