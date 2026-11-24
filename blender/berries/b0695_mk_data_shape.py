# mk_data_shape
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file sweeping/sweep_3D_modes.py, line 37
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mk_data_shape(ar_1, ar_2, ar_3, mode="nested"):
    if mode == "nested":
        return len(ar_1), len(ar_2), len(ar_3)

    elif mode == "co-move" or mode == "position_list":
        return 1, 1, len(ar_3)

    elif mode == "1,2_co-move":
        return 1, len(ar_2), len(ar_3)

    elif mode == "2,3_co-move":
        return len(ar_1), 1, len(ar_3)
