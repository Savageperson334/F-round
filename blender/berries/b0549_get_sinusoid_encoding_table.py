# get_sinusoid_encoding_table
#
# Copied verbatim from https://github.com/MuSAELab/hunee-b
#   file beessl/upstream/msm_mae/msm_mae/pos_embed.py, line 102
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Beehives and unusual agriculture
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def get_sinusoid_encoding_table(n_position, d_hid, cls_token=False): 
    ''' Sinusoid position encoding table ''' 
    # TODO: make it with torch instead of numpy 
    def get_position_angle_vec(position): 
        return [position / np.power(10000, 2 * (hid_j // 2) / d_hid) for hid_j in range(d_hid)] 

    sinusoid_table = np.array([get_position_angle_vec(pos_i) for pos_i in range(n_position)]) 
    sinusoid_table[:, 0::2] = np.sin(sinusoid_table[:, 0::2]) # dim 2i 
    sinusoid_table[:, 1::2] = np.cos(sinusoid_table[:, 1::2]) # dim 2i+1 

    if cls_token:
        sinusoid_table = np.concatenate([np.zeros([1, d_hid]), sinusoid_table], axis=0)
    return sinusoid_table
