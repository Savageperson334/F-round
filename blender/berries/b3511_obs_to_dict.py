# obs_to_dict
#
# Copied verbatim from https://github.com/quantumiracle/Reinforcement_Learning_for_Traffic_Light_Control
#   file 6.ddpg_for_single/common/vec_env/util.py, line 53
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def obs_to_dict(obs):
    """
    Convert an observation into a dict.
    """
    if isinstance(obs, dict):
        return obs
    return {None: obs}
