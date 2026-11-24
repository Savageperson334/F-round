# deprocess_image
#
# Copied verbatim from https://github.com/JueLin/textureSynthesis-stylegan2-pytorch
#   file utils.py, line 43
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Textures and materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def deprocess_image(batch, in_high=1, in_low=-1, out_high=1, out_low=0):
    # from [in_low, in_high] to [0, 1] then to [out_low, out_high]
    assert in_high>in_low, "Invalid input range"
    assert out_high>out_low, "Invalid output range"
    return (batch-in_low)/(in_high-in_low)*(out_high-out_low)+out_low
