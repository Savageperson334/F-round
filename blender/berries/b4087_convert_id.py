# convert_id
#
# Copied verbatim from https://github.com/yukiyuqichen/His-Geo
#   notebook his_geo/data/Modern/history_mapping.ipynb (its code cells joined in order; line 24 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convert_id(id):
    id = str(id).rstrip('0')
    if len(id) == 5 or len(id) == 3 or len(id) == 1:
        id = id + '0'
    id = int(id)
    return id
