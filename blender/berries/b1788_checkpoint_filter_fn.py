# checkpoint_filter_fn
#
# Copied verbatim from https://github.com/farjon/insect_detection
#   file pytorch_image_models/timm/models/cait.py, line 306
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def checkpoint_filter_fn(state_dict, model=None):
    if 'model' in state_dict:
        state_dict = state_dict['model']
    checkpoint_no_module = {}
    for k, v in state_dict.items():
        checkpoint_no_module[k.replace('module.', '')] = v
    return checkpoint_no_module
