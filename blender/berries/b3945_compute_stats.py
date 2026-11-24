# compute_stats
#
# Copied verbatim from https://github.com/xandergos/terrain-diffusion
#   file figs/signed_sqrt_transform/visualize_stats.py, line 100
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Procedural and generated worlds
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def compute_stats(samples):
    """Compute mean and standard deviation for each sample"""
    means = []
    stds = []

    for sample in samples:
        means.append(np.mean(sample))
        stds.append(np.std(sample))

    return np.array(means), np.array(stds)
