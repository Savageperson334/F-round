# labelsToTransitions
#
# Copied verbatim from https://github.com/rsandler00/plotly-scientific-plots
#   file plotly_scientific_plots/plot_subcomponents.py, line 227
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def labelsToTransitions(labels,
                        mode='all', # 'all', 'starts', 'stops'
                        ):
    '''
    gets transition points from labels
    Returns:
        transition_points: list of transition points
        transition_values: list same size as transition_points of actual values of labels at those points
    '''
    if mode == 'all':
        diff = np.diff(labels) != 0
    transition_points = list(np.where(diff)[0]+1)
    transition_points = [0] + transition_points + [len(diff)]
    transition_values = labels[transition_points]
    return transition_points, transition_values
