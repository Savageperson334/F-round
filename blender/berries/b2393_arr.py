# arr
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/melodee/upstream/tools/gen_tables.py, line 19
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def arr(name, ctype, vals, per=12, ram=False):
    """a table in flash (XIP, through the cache); ram: in RAM (.data), for lookups every sample"""
    out = [f"static {'TABLE_RAM ' if ram else 'const '}{ctype} {name}[{len(vals)}] = {{"]
    for i in range(0, len(vals), per):
        out.append("    " + ", ".join(str(v) for v in vals[i:i + per]) + ",")
    out.append("};")
    return out
