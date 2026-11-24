# decay_batch_exp
#
# Copied verbatim from https://github.com/farjon/insect_detection
#   file pytorch_image_models/benchmark.py, line 464
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Moths insects and insect traps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def decay_batch_exp(batch_size, factor=0.5, divisor=16):
    out_batch_size = batch_size * factor
    if out_batch_size > divisor:
        out_batch_size = (out_batch_size + 1) // divisor * divisor
    else:
        out_batch_size = batch_size - 1
    return max(0, int(out_batch_size))
