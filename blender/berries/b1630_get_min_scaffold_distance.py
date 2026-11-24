# get_min_scaffold_distance
#
# Copied verbatim from https://github.com/douglaslab/pyOrigamiBreak
#   file autobreak/utilities.py, line 111
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Origami, folds and paper
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_min_scaffold_distance(scaffold_length, start_index, end_index, is_scaffold_circular=True):
    '''Get min distance between two positions on a circular oligo'''
    forward_distance  = (end_index - start_index) % scaffold_length 
    reverse_distance = scaffold_length - forward_distance
    if is_scaffold_circular:
        return min(forward_distance, reverse_distance)
    else:
        return abs(end_index - start_index)
