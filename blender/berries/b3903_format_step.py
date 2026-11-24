# format_step
#
# Copied verbatim from https://github.com/waleedka/hiddenlayer
#   file hiddenlayer/history.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Graphs and networks
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_step(step, zero_prefix=False):
    """Return the step value in format suitable for display."""
    if isinstance(step, int):
        return "{:06}".format(step) if zero_prefix else "{}".format(step)
    elif isinstance(step, tuple):
        return "{:04}:{:06}".format(*step) if zero_prefix else "{}:{}".format(*step)
