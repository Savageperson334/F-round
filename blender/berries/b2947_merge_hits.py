# merge_hits
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/bench_analyze.py, line 234
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def merge_hits(hits, merge):
    if len(hits) == 0:
        return []
    groups, g0, last = [], int(hits[0]), int(hits[0])
    for h in hits[1:]:
        h = int(h)
        if h - last > merge:
            groups.append((g0, last))
            g0 = h
        last = h
    groups.append((g0, last))
    return groups
