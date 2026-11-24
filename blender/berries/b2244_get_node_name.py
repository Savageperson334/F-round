# get_node_name
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/bem/sources.py, line 58
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_node_name(prefix: str, suffix):
    if prefix:
        return f"{prefix}_{suffix}_node"
    else:
        return f"{suffix}_node"
