# uniquifiy
#
# Copied verbatim from https://github.com/xdas-dev/xdas
#   file xdas/io/miniseed.py, line 186
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def uniquifiy(seq):
    """Return the unique elements of *seq* in order; unwrap to scalar if only one."""
    seen = set()
    seq = [x for x in seq if x not in seen and not seen.add(x)]
    if len(seq) == 1:
        return seq[0]
    else:
        return seq
