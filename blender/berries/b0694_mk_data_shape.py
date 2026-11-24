# mk_data_shape
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file sweeping/sweep_2D_modes.py, line 50
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mk_data_shape(ar_1, ar_2, mode="nested"):
    if mode == "nested":
        return len(ar_1), len(ar_2)
    elif mode == "nested_swap_order":
        return len(ar_2), len(ar_1)
    elif mode == "co-move" or mode == "position_list":
        return 1, len(ar_2)
    elif mode == "serpentine":
        return len(ar_1), len(ar_2)
    elif mode == "serpentine_swap_order":
        return len(ar_2), len(ar_1)
