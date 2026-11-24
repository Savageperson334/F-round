# longest_matches
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/6502/c64-led-test/tools/pack_rom.py, line 29
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MAX_DIST = 4096

MAX_MATCH = 18

MIN_MATCH = 3


def longest_matches(data):
    """Each position's longest match and its distance back."""
    chains = {}
    best = [(0, 0)] * len(data)
    for i in range(len(data)):
        if i + MIN_MATCH <= len(data):
            key = data[i:i + MIN_MATCH]
            found_len, found_dist = 0, 0
            for j in reversed(chains.get(key, ())):
                dist = i - j
                if dist > MAX_DIST:
                    break
                n = MIN_MATCH
                limit = min(MAX_MATCH, len(data) - i)
                while n < limit and data[j + n] == data[i + n]:
                    n += 1
                if n > found_len:
                    found_len, found_dist = n, dist
                    if n == limit:
                        break
            best[i] = (found_len, found_dist)
            chains.setdefault(key, []).append(i)
    return best
