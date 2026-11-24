# calc_m_ssb
#
# Copied verbatim from https://github.com/volkanozsarac/OSW-6ICEES
#   notebook 2. Python.ipynb (its code cells joined in order; line 532 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calc_m_ssb(p, l, x = None):
    if x != None:
        moment = p*l*x/2 - p*x*x/2
    else:
        moment = []
        for x in [1*l/4, 2*l/4, 3*l/4]:
            moment.append(p*l*x/2 - p*x*x/2)
    return moment
