# stars_visible
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/skyglow.py, line 88
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

_STAR_COUNTS = [(1.0, 15), (2.0, 48), (3.0, 171), (4.0, 513), (5.0, 1602), (6.0, 4800), (6.5, 9100), (7.0, 14000)]


def stars_visible(limit_mag: float) -> int:
    """Stars above the horizon brighter than `limit_mag`: half the
    whole-sky count, log-interpolated."""
    pts = _STAR_COUNTS
    if limit_mag <= pts[0][0]:
        return int(round(pts[0][1] / 2 * 10 ** (0.45 * (limit_mag - pts[0][0]))))
    for (m0, n0), (m1, n1) in zip(pts, pts[1:]):
        if limit_mag <= m1:
            f = (limit_mag - m0) / (m1 - m0)
            return int(round(10 ** (math.log10(n0) + f * (math.log10(n1) - math.log10(n0))) / 2))
    return pts[-1][1] // 2
