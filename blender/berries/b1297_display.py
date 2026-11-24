# display
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/pcode-disassembly/scripts/reconstruct/petspeed_listing.py, line 15
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def display(text):
    # Never emit terminal control bytes; the PRG is made from tokens, not display text.
    return ''.join(c if 32 <= ord(c) <= 126 else f'{{0x{ord(c):02X}}}' for c in text)
