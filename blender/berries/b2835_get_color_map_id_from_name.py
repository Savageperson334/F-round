# get_color_map_id_from_name
#
# Copied verbatim from https://github.com/nion-software/nionswift
#   file nion/swift/model/ColorMaps.py, line 147
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def get_color_map_id_from_name(name: str) -> str:
    color_map_id = name.lower()
    color_map_id = re.sub(r"[^\w\s]", '', color_map_id)
    color_map_id = re.sub(r"\s+", '-', color_map_id)
    return color_map_id
