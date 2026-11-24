# other_layers_mem_cost
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/print_size_presentation.py, line 101
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

base_w = 975


def other_layers_mem_cost(input_h, batch_size=32, in_gb=False):
    h = input_h * 0.5*0.5
    w = (input_h/30)*base_w * 0.7*0.7

    # dim-reduction 1:  h->128
    # dim-reduction 2: 512 ->167
    params_mem = (h*128*256 + 128)  + (512*2*167 + 167)

    bridge = 128*w
    alphabet = 167*w

    activation_mem = bridge + alphabet

    # multiply by 4 because there are 4 bytes per param (32bit float = 4 bytes)
    params_mem *= 4
    activation_mem *= (4*batch_size )

    if in_gb:
        params_mem /= 1000000000
        activation_mem /= 1000000000

    return activation_mem, params_mem
