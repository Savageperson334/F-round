# po_field
#
# Copied verbatim from https://github.com/LaM3rzLG/FreeTVC
#   file tools/lang/po_check.py, line 118
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def po_quote(s):
    s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\t", "\\t").replace("\n", "\\n")
    return '"' + s + '"'


def po_field(keyword, s):
    pieces = re.findall(r"[^\n]*\n|[^\n]+$", s)
    if len(pieces) <= 1:
        return f"{keyword} {po_quote(s)}\n"
    return f'{keyword} ""\n' + "".join(po_quote(p) + "\n" for p in pieces)
