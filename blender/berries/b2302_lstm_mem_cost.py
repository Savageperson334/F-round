# lstm_mem_cost
#
# Copied verbatim from https://github.com/isi-vista/VistaOCR
#   file src/print_size_presentation.py, line 72
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

base_w = 975


def lstm_mem_cost(input_h, batch_size=32, in_gb=False):
    h = input_h * 0.5*0.5
    w = (input_h/30)*base_w * 0.7*0.7

    # FC: h->128;  LSTMx3(512x2);  FC: 512x2->167
    # Param cost:  4(nh+h^2) where n=input dim, h=output dim/hidden-dim
    #   For bidirectional LSTM must mulitply by 2
    #   For bias, add an extra h
    #                   LSTM-1 (x=128, h=512)         LSTM-2  (x=512, h=512)        LSTM-3  (x=512, h=512)
    params_mem = 4*2*(128*512 + 512*512 + 512) + 4*2*(512*512 + 512*512 + 512) + 4*2*(512*512 + 512*512 + 512)

    # Mem Cost for LSTM activations: output and hidden cell state (times 2 because biderectional), times number of timesteps
    #       Cell-state   Hidden-state/output
    lstm_1 = 512*2*w + 512*2*w
    lstm_2 = 512*2*w + 512*2*w
    lstm_3 = 512*2*w + 512*2*w

    activation_mem = lstm_1 + lstm_2 + lstm_3

    # multiply by 4 because there are 4 bytes per param (32bit float = 4 bytes)
    params_mem *= 4
    activation_mem *= (4*batch_size )

    if in_gb:
        params_mem /= 1000000000
        activation_mem /= 1000000000

    return activation_mem, params_mem
