# array
#
# Copied verbatim from https://github.com/kpalaniuk/gnomad-firmware
#   file tools/gn_gen_content.py, line 182
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def array(name, data, comment):
    rows = [",".join(str(b) for b in data[i:i + 32]) for i in range(0, len(data), 32)]
    return f"/* {comment} */\nstatic const uint8_t {name}[{len(data)}u] = {{\n" + ",\n".join(rows) + "};\n"
