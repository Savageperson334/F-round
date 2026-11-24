# calculate_multiples
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook AUT/Dr. Javaherian/2nd project_ES_03-04_1st term (2).ipynb (its code cells joined in order; line 74 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def calculate_multiples(reflectivity, num_samples):
    first_order_multiples = np.zeros(num_samples)
    second_order_multiples = np.zeros(num_samples)
    third_order_multiples = np.zeros(num_samples)

    for i in range(1, len(reflectivity)):
        first_order_multiples[i] += reflectivity[i-1] * reflectivity[i]
    for i in range(2, len(reflectivity)):
        second_order_multiples[i] += reflectivity[i-2] * reflectivity[i-1] * reflectivity[i]
    for i in range(3, len(reflectivity)):
        third_order_multiples[i] += reflectivity[i-3] * reflectivity[i-2] * reflectivity[i-1] * reflectivity[i]

    return first_order_multiples[:num_samples], second_order_multiples[:num_samples], third_order_multiples[:num_samples]
