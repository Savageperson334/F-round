# calc_m_midspan_ssb
#
# Copied verbatim from https://github.com/volkanozsarac/OSW-6ICEES
#   notebook 2. Python.ipynb (its code cells joined in order; line 524 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calc_m_midspan_ssb(p, l):
    midspan_moment = p*l**2/8
    return midspan_moment
