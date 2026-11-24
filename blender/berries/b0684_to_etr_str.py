# to_etr_str
#
# Copied verbatim from https://github.com/ScopeFoundry/ScopeFoundry
#   file measurement.py, line 741
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def to_etr_str(secs):
    mins, mins_rem = divmod(secs, 60)
    if not mins:
        return f"{int(secs)}s"
    hours, hours_rem = divmod(secs, 3600)
    if not hours:
        return f"{mins + mins_rem/60:0.1f}min"
    days, days_rem = divmod(secs, 86400)
    if not days:
        return f"{hours + hours_rem/3600:0.1f}h"
    return f"{secs/86400:0.1f}d"
