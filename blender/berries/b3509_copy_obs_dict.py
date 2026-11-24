# copy_obs_dict
#
# Copied verbatim from https://github.com/quantumiracle/Reinforcement_Learning_for_Traffic_Light_Control
#   file 6.ddpg_for_single/common/vec_env/util.py, line 11
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def copy_obs_dict(obs):
    """
    Deep-copy an observation dict.
    """
    return {k: np.copy(v) for k, v in obs.items()}
