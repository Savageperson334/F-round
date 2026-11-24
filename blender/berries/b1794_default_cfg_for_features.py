# default_cfg_for_features
#
# Copied verbatim from https://github.com/farjon/insect_detection
#   file pytorch_image_models/timm/models/helpers.py, line 336
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from copy import deepcopy


def default_cfg_for_features(default_cfg):
    default_cfg = deepcopy(default_cfg)
    # remove default pretrained cfg fields that don't have much relevance for feature backbone
    to_remove = ('num_classes', 'crop_pct', 'classifier', 'global_pool')  # add default final pool size?
    for tr in to_remove:
        default_cfg.pop(tr, None)
    return default_cfg
