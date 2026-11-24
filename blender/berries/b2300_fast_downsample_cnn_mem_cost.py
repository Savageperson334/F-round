# fast_downsample_cnn_mem_cost
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/print_size_presentation.py, line 13
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

base_w = 975


def fast_downsample_cnn_mem_cost(input_h, batch_size=32, in_gb=False):
    h = (input_h/30)*30
    w = (input_h/30)*base_w


    params_mem = 0
    activation_mem = 0

    while h > 30:
        # Param cost
        params_mem += (3*3*1*16 + 16)
        activation_mem += h*w*16 + h*0.5*w*0.5*16
        h *= 0.5
        w *= 0.5

    # multiply by 4 because there are 4 bytes per param (32bit float = 4 bytes)
    params_mem *= 4
    activation_mem *= (4*batch_size )

    if in_gb:
        params_mem /= 1000000000
        activation_mem /= 1000000000

    return activation_mem, params_mem
