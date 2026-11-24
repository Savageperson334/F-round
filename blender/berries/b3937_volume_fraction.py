# volume_fraction
#
# Copied verbatim from https://github.com/wwlysses/volumetric-fraction
#   notebook Volumetric Fraction.ipynb (its code cells joined in order; line 11 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Ferrofluids and magnetic materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def volume_fraction(wnp,pnp,wbf,pbf):
    r=(wnp/pnp)/(wnp/pnp + wbf/pbf)
    return r
