# mk_data_dict
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file controlling/ranged_optimization.py, line 21
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def mk_z_array(center, span, num):
    return np.linspace(center - 0.5 * span, center + 0.5 * span, num)


def mk_data_dict(center, span, num, z_original):
    return {
        "z_original": z_original,
        "z0_coarse": center,
        "z0_fine": center,
        "z0": center,
        "z_coarse": mk_z_array(center, span, num),
        "f_coarse": np.zeros(num),
        "z_fine": mk_z_array(center, span, 2 * num),
        "f_fine": np.zeros(2 * num),
    }
