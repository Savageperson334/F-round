# interval_between
#
# Copied verbatim from https://github.com/MacNite/HiveHub
#   file server/counter_intervals.py, line 88
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Beehives and unusual agriculture
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def interval_between(prev_total, cur_total, restarted: bool):
    """Crossings between two totals: everything since the restart when the
    counter restarted (what happened before it, after the previous sample, is
    unrecoverable), the plain difference otherwise."""
    return cur_total if restarted else cur_total - prev_total
