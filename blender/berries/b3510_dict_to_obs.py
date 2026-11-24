# dict_to_obs
#
# Copied verbatim from https://github.com/quantumiracle/Reinforcement_Learning_for_Traffic_Light_Control
#   file 6.ddpg_for_single/common/vec_env/util.py, line 18
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def dict_to_obs(obs_dict):
    """
    Convert an observation dict into a raw array if the
    original observation space was not a Dict space.
    """
    if set(obs_dict.keys()) == {None}:
        return obs_dict[None]
    return obs_dict
