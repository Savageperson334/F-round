# arr
#
# Copied verbatim from https://github.com/GRiMMBIENT/grimm
#   file tools/gen_tables.py, line 23
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#   the same function also appears in: genkigenki/Speak37, isod89/clipper-fm1, isod89/clipper-pro, jbschooley/Virtual-FM-1, kpalaniuk/gnomad-firmware
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def arr(name, ctype, vals, per=12):
    out = [f"static const {ctype} {name}[{len(vals)}] = {{"]
    for i in range(0, len(vals), per):
        out.append("    " + ", ".join(str(v) for v in vals[i:i + per]) + ",")
    out.append("};")
    return out
