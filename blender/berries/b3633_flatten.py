# flatten
#
# Copied verbatim from https://github.com/sraddon/SUMO-V2X-Communication-Research-Platooning-and-CIM
#   file src/simlib.py, line 5
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def flatten(l):
    # A basic function to flatten a list
    return [item for sublist in l for item in sublist]
