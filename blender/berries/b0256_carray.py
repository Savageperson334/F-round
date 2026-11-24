# carray
#
# Copied verbatim from https://github.com/GRiMMBIENT/grimm
#   file tools/gen_samples.py, line 22
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def carray(name, b):
    lines = [",".join(str(x) for x in b[i:i + 40]) for i in range(0, len(b), 40)]
    return f"static const uint8_t {name}[{len(b)}] = {{\n" + ",\n".join(lines) + "};\n"
