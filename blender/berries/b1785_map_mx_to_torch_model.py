# map_mx_to_torch_model
#
# Copied verbatim from https://github.com/farjon/insect_detection
#   file pytorch_image_models/convert/convert_from_mxnet.py, line 74
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def map_mx_to_torch_model(mx_name):
    torch_name = mx_name.lower()
    if torch_name.startswith('se_'):
        torch_name = torch_name.replace('se_', 'se')
    elif torch_name.startswith('senet_'):
        torch_name = torch_name.replace('senet_', 'senet')
    elif torch_name.startswith('inceptionv3'):
        torch_name = torch_name.replace('inceptionv3', 'inception_v3')
    torch_name = 'gluon_' + torch_name
    return torch_name
