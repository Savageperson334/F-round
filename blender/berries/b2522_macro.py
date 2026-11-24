# macro
#
# Copied verbatim from https://github.com/kpalaniuk/gnomad-firmware
#   file tools/gn_gen_content.py, line 96
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def macro(v, centred):
    v = max(0, min(127, v))
    if centred:
        return v * 512 if v <= 64 else 32768 + (v - 64) * 32767 // 63
    return (v * 65535 + 63) // 127
