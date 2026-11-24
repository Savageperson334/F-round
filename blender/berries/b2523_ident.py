# ident
#
# Copied verbatim from https://github.com/kpalaniuk/gnomad-firmware
#   file tools/gn_gen_content.py, line 115
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def ident(name):
    """a bank name as a C identifier: upper case, every other character '_'"""
    return "".join(c if c.isalnum() else "_" for c in name.upper())
