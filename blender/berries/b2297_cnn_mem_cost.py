# cnn_mem_cost
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/print_mem_page.py, line 23
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

base_w = 600


def cnn_mem_cost(input_h, batch_size=32):
    h = (input_h/30)*30
    w = (input_h/30)*base_w

    # Param cost
    #params = (3*3*1*64 + 64) + (3*3*64*64 + 64) + (3*3*64*128 + 128) + (3*3*128*128 + 128) + (3*3*128*128 + 128)
    params = (3*3*1*64 + 64) + (3*3*64*64 + 64)

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

    #mem = batch_size * (c1 + c2 + p1 + c3 + c4 + p2 + c5 + c6 + c7)
    mem = batch_size * (c1 + c2)

    # *4 because 4 bytes per param
    return 4*(2*mem + params*3)
