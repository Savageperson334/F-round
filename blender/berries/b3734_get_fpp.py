# get_fpp
#
# Copied verbatim from https://github.com/tfenz/TE_SR_WAN_simulation
#   file src/utility/utility.py, line 58
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_fpp(links, divisor: int = 4, min_fpp: int = 3):
    """ flows per pair is dependent on the size of the links"""
    flows_per_pair = max(int(len(links) / divisor), min_fpp)
    return flows_per_pair
