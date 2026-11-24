# arr
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/gen_tables.py, line 20
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

HOT_TABLES = ['SINE', 'PITCH_OCT', 'TIME_MS_X10', 'ENV_LIN', 'ENV_EXP', 'LFO_INC', 'TANH_Q15']


def arr(name, ctype, vals, per=12):
    out = [f"static const {ctype} {name}[{len(vals)}]{' HOT_RAM' if name in HOT_TABLES else ''} = {{"]
    for i in range(0, len(vals), per):
        out.append("    " + ", ".join(str(v) for v in vals[i:i + per]) + ",")
    out.append("};")
    return out
