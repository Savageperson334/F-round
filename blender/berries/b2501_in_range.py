# in_range
#
# Copied verbatim from https://github.com/kitzeslab/bioacoustics-cookbook
#   notebook data_selection/filter_files_by_dates_and_times.ipynb (its code cells joined in order; line 51 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def in_range(x,r): #helper function
    if x>=r[0] and x<=r[1]:
        return True
    return False
