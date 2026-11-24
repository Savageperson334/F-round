# create_volume_data
#
# Copied verbatim from https://github.com/superstar54/weas-widget
#   file src/weas_widget/utils.py, line 255
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def create_volume_data(data, cell=[[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
    """
    Convert a 3D nested list (data.values) into a structured volume data format.

    Parameters:
        data (dict): A dictionary containing a 3D list `values`.
        cell (list, optional): The transformation matrix for the cell. Default is identity matrix.

    Returns:
        dict: A dictionary with dimensions, flattened values, cell, and origin.
    """
    # Get the dimensions of the 3D data
    dims = [len(data), len(data[0]), len(data[0][0])]

    # Flatten the 3D data into a 1D list
    values = np.array(data).flatten().tolist()

    return {"dims": dims, "values": values, "cell": cell, "origin": [0, 0, 0]}
