# average
#
# Copied verbatim from https://github.com/zuzhaoye/cellular-automata-traffic-flow-framework
#   notebook structure_chn_with_output.ipynb (its code cells joined in order; line 431 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def average(data, steps_trace_back):
    step = len(data)
    start = step - steps_trace_back
    data_len = steps_trace_back + 1

    recent_average = sum(data[start:]) / data_len

    return recent_average
