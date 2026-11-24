# cnn_mem_cost
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/print_size_presentation.py, line 39
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

base_w = 975


def cnn_mem_cost(input_h, batch_size=32, in_gb=False):
    h = input_h
    w = (input_h/30)*base_w

    # Param cost
    #              conv1+bias         conv2+bias          conv3+bias         conv4+bias             conv5+bias             conv6+bias            conv7+bias
    params_mem = (3*3*1*64 + 64) + (3*3*64*64 + 64) + (3*3*64*128 + 128) + (3*3*128*128 + 128) + (3*3*128*256 + 256) + (3*3*256*256 + 256) + (3*3*256*256 + 256)

    # Mem cost
    c1 = h*w*64
    c2 = h*w*64
    p1 = (h*.5)*(w*.7)*64
    c3 = (h*.5)*(w*.7)*128
    c4 = (h*.5)*(w*.7)*128
    p2 = (h*.5*.5)*(w*.7*.7)*128
    c5 = (h*.5*.5)*(w*.7*.7)*256
    c6 = (h*.5*.5)*(w*.7*.7)*256
    c7 = (h*.5*.5)*(w*.7*.7)*256

    activation_mem = c1 + c2 + p1 + c3 + c4 + p2 + c5 + c6 + c7


    # multiply by 4 because there are 4 bytes per param (32bit float = 4 bytes)
    params_mem *= 4
    activation_mem *= (4*batch_size )

    if in_gb:
        params_mem /= 1000000000
        activation_mem /= 1000000000

    return activation_mem, params_mem
