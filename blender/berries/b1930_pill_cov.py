# pill_cov
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/gen_aa_keycaps.py, line 51
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pill_cov(w, h, r):
    """fill coverage 0..16 per pixel: 4 x 4 samples against the rounded rectangle"""
    cov = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            n = 0
            for sy in range(4):
                for sx in range(4):
                    px, py = x + (sx + 0.5) / 4, y + (sy + 0.5) / 4
                    cx = min(max(px, r), w - r)
                    cy = min(max(py, r), h - r)
                    n += (px - cx) ** 2 + (py - cy) ** 2 <= r * r
            cov[y][x] = n
    return cov
