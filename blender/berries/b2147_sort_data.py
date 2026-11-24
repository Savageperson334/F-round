# sort_data
#
# Copied verbatim from https://github.com/gvard/astrodata
#   file src/astrodata/stars/plot_sne_discoveries_numbers.py, line 82
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def sort_data(dats, all_nums_year):
    """Sort data"""
    all_data = []
    for i, dat in enumerate(dats):
        if i < len(all_nums_year):
            all_data.append([dat, all_nums_year[i]])
    all_data.sort(key=lambda row: row[0])
    dats_sorted, nums_sorted = zip(*all_data)
    dats_sorted = list(dats_sorted)
    nums_sorted = list(nums_sorted)
    return dats_sorted, nums_sorted
