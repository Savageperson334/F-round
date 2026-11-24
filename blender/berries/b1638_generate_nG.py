# generate_nG
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 241
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def generate_nG(oligo_length):
    '''Generate GGGGG...GGG'''
    return 'G'*int(oligo_length)
