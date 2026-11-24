# param_types
#
# Copied verbatim from https://github.com/kpalaniuk/gnomad-firmware
#   file tools/gn_size_fns.py, line 86
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re


def param_types(s):
    """an IR argument or parameter list -> its types ("%struct.track* %5, i32 0" and "%struct.track*, i32" alike)"""
    parts, depth, cur = [], 0, ""
    for ch in s:
        depth += ch in "([{<"
        depth -= ch in ")]}>"
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    out = []
    for a in parts:
        a = re.sub(r" (?:nonnull|noalias|readonly|readnone|nocapture|signext|zeroext|returned|byval|sret|inreg|"
                   r"dereferenceable(?:_or_null)?\(\d+\)|align \d+)\b", "", " " + a.strip())
        a = re.sub(r" (?:%[\w.]+|-?\d+|null|undef|true|false|@[\w.]+)$", "", a)
        out.append(a.strip())
    return tuple(out)
