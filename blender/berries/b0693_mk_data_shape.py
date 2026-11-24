# mk_data_shape
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file sweeping/sweep_1D_modes.py, line 13
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mk_data_shape(ar_1, mode="nested"):
    if mode == "nested" or mode == "position_list":
        return (len(ar_1),)
