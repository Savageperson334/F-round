# pick_copy
#
# Copied verbatim from https://github.com/N6RFM/HADESx-Decoder
#   file src/hadesx/voice.py, line 176
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Sensors and telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import collections


def pick_copy(copies, how='common'):
    """Choose one 40-byte frame out of all receptions of the same frame number.
    'common' = the most frequent identical copy (ties: the most recent of them), 'latest' = the newest, 'first'."""
    if how == 'latest':
        return copies[-1]
    if how == 'first':
        return copies[0]
    counts = collections.Counter(copies)
    best = max(counts.values())
    for c in reversed(copies):
        if counts[c] == best:
            return c
