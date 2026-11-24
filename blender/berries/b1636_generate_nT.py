# generate_nT
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 231
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def generate_nT(oligo_length):
    '''Generate TTTTT...TTT'''
    return 'T'*int(oligo_length)
