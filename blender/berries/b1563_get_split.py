# get_split
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file beans/scripts/hainan_gibbons.py, line 23
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_split(file_id):
    # 1:5:3:3
    if file_id == 0:
        return 'train-low'
    elif 1 <= file_id <= 5:
        return 'train'
    elif 6 <= file_id <= 8:
        return 'valid'
    else:
        return 'test'
