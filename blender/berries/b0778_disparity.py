# disparity
#
# Copied verbatim from https://github.com/XiaokangLiuCUG/DeepMorph
#   file Triassic results and codes/recovery simulations.py, line 55
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Laboratories, geochemistry, chemistry and microscopes
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def disparity(survivor_taxa_coo):
    sum_of_ranges = (np.max(survivor_taxa_coo[:,0]) - np.min(survivor_taxa_coo[:,0])) + (np.max(survivor_taxa_coo[:,1]) - np.min(survivor_taxa_coo[:,1]))
    sum_of_variances = np.var(survivor_taxa_coo[:,0]) + np.var(survivor_taxa_coo[:,1])
    sum_of_centroid_dis = np.sum(((survivor_taxa_coo[:,0] - np.mean(survivor_taxa_coo[:,0]))**2 + (survivor_taxa_coo[:,1] - np.mean(survivor_taxa_coo[:,1]))**2)**0.5) / survivor_taxa_coo.shape[0] 
    return [sum_of_ranges, sum_of_variances, sum_of_centroid_dis]
