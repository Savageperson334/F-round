# print_information
#
# Copied verbatim from https://github.com/polimi-ispl/nah-khcnn
#   file src/test_module/plot_results.py, line 49
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def print_information(i, mode_test=[], freq_test=[], num_plate_test=[], boundary_test=[], plate_dimensions_test=[],
                      snr_test=[]):
    """
    Print and return all the information relate to a specified test case. If pass "" -> not print that information
    :param i: index to print information
    :param all the test set infotmation
    :return: information
    """
    information = ""
    if len(boundary_test) != 0:
        information += f"bound:\t{boundary_test[i]}\n"
    if len(freq_test) != 0:
        information += f"freq:\t{np.round(freq_test[i], 2)} Hz\n"
    if len(mode_test) != 0:
        information += f"mode:\t{mode_test[i]}\n"
    if len(num_plate_test) != 0:
        information += f"plate:\t{num_plate_test[i]}\n"
    if len(plate_dimensions_test) != 0:
        information += f"dim:\t{plate_dimensions_test[i]} m\n"
    if len(snr_test) != 0:
        information += f"snr:\t{snr_test[i]} dB\n"

    information += f"index:\t{i}\n"

    print(information)
    return information
