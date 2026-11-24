# uniquifiy
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/core/datacollection.py, line 933
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def uniquifiy(seq):
    """Return a deduplicated tuple of *seq* elements in their original order."""
    seen = set()
    return tuple(x for x in seq if x not in seen and not seen.add(x))
