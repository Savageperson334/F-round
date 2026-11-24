# wrap_comment
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/68k/amiga-boot/tools/mkimage.py, line 197
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import textwrap


def wrap_comment(paragraphs):
    """Wrap paragraphs into "; " comment lines, blank ones becoming ";"."""
    out = []
    for text in paragraphs:
        if not text:
            out.append(";")
            continue
        out += [f"; {line}" for line in
                textwrap.wrap(text, width=73, break_long_words=False)]
    return out
