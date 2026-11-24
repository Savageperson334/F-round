# clock_of
#
# Copied verbatim from https://github.com/elpapimango/retroclawd
#   file machines/sega/scenarios/fitslots.py, line 22
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clock_of(h, h40):
    off = 780 if h40 else 774
    first = 0xE4 if h40 else 0xE9
    base = 18 if h40 else 15
    steps = 46 if h40 else 38
    if h >= first:
        return (h - first + base) * off // steps - off
    lo = 0xA5 if h40 else 0x85
    hi = 0xB6 if h40 else 0x93
    if lo <= h <= hi:
        return (h - lo) * off // steps - off
    return h * (16 if h40 else 20)
