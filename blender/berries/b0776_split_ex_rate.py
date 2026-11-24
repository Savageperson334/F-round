# split_ex_rate
#
# Copied verbatim from https://github.com/XiaokangLiuCUG/DeepMorph
#   file Triassic results and codes/recovery simulations.py, line 26
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Laboratories, geochemistry, chemistry and microscopes
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def split_ex_rate(total_rate,num_taxa,selectivity):
    split_rate = np.array([])
#     for i in range(num_taxa):
#         split_rate = np.append(split_rate,2*(i+1)*total_rate /(num_taxa*(num_taxa+1)))
    split_rate = np.linspace(1/(100*(1+selectivity)), selectivity/(100*(1+selectivity)), 200,endpoint=True)
    return split_rate
