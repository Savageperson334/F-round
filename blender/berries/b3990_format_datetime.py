# format_datetime
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/coordinates/core.py, line 1786
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_datetime(x):
    """Format a datetime64-like *x* as an ISO string, truncating sub-millisecond digits."""
    string = str(x)
    if "." in string:
        datetime, digits = string.split(".")
        digits = digits[:3]
        return f"{datetime}.{digits}"
    else:
        return string
