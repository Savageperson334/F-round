# loss_parser
#
# Copied verbatim from https://github.com/geonm/EnhanceNet-Tensorflow
#   file utils.py, line 41
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def loss_parser(str_loss):
    '''
    NOTE!!! str_loss should be like 'mse,perceptual,texture,adv'...
    '''
    selected_loss_array = str_loss.split(',')
    return selected_loss_array
