# get_split
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file beans/scripts/dcase.py, line 14
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_split(chunk_id, total_num_chunks):
    if chunk_id / total_num_chunks < .12:
        return 'train-low'
    elif chunk_id / total_num_chunks < .6:
        return 'train'
    elif chunk_id / total_num_chunks < .8:
        return 'valid'
    else:
        return 'test'
