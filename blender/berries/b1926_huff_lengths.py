# huff_lengths
#
# Copied verbatim from https://github.com/genkigenki/Speak37
#   file tools/gen_aa_font.py, line 97
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware, oscillr/LRRY
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import heapq

HC_MAXLEN = 15


def huff_lengths(count):
    """symbol -> code length (Huffman), at most HC_MAXLEN"""
    heap = [(c, k, (s,)) for k, (s, c) in enumerate(sorted(count.items()))]
    heapq.heapify(heap)
    length = {s: 0 for s in count}
    if len(heap) == 1:
        return {s: 1 for s in count}
    k = len(heap)
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        for s in a[2] + b[2]:
            length[s] += 1
        k += 1
        heapq.heappush(heap, (a[0] + b[0], k, a[2] + b[2]))
    assert max(length.values()) <= HC_MAXLEN, "code too long: limit the lengths"
    return length
