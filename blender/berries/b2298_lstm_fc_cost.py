# lstm_fc_cost
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/print_mem_page.py, line 49
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

base_w = 600


def lstm_fc_cost(input_h, batch_size=32):
    h = (input_h/30)*30 * 0.5*0.5
    w = (input_h/30)*base_w * 0.7*0.7

    # FC: h->128;  LSTMx3(512x2);  FC: 512x2->167
    # Param cost
    params = (h*128*256 + 128) + ((4*2*512*128 + 4*2*512*512) + (4*2*512*512 + 4*2*512*512) + (4*2*512*512 + 4*2*512*512)) + (512*2*167 + 167)

    # Mem Cost
    bridge = 128*w
    lstm_1 = 4*512*2*w + 512*2*w
    lstm_2 = 4*512*2*w + 512*2*w
    lstm_3 = 4*512*2*w + 512*2*w
    alphabet = 167*w

    mem = batch_size * (bridge + lstm_1 + lstm_2 + lstm_3 + alphabet)

    # *4 because 4 bytes per param
    return 4*(2*mem + params*3)
