# clock_of
#
# Copied verbatim from https://github.com/elpapimango/retroclawd
#   file machines/sega/scenarios/slotscan.py, line 17
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def clock_of(h, h40=True):
    off = 780 if h40 else 774
    if h >= (0xE4 if h40 else 0xE9):
        base = 18 if h40 else 15
        steps = 46 if h40 else 38
        first = 0xE4 if h40 else 0xE9
        return (h - first + base) * off // steps - off
    if h >= (0xA5 if h40 else 0x85) and h <= (0xB6 if h40 else 0x93):
        first = 0xA5 if h40 else 0x85
        steps = 46 if h40 else 38
        return (h - first) * off // steps - off
    return (h * (16 if h40 else 20))
