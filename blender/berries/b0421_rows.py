# rows
#
# Copied verbatim from https://github.com/KHAVld/ARTIHIVE
#   file tools/gen_dsp_tables.py, line 34
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def rows(name, values, typ):
    s = f"static const {typ} {name}[128] = {{\n"
    for i in range(0, 128, 8):
        s += "    " + ", ".join(f"{v}u" for v in values[i:i + 8]) + ",\n"
    return s + "};\n"
