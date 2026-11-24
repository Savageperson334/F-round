# fmt_array
#
# Copied verbatim from https://github.com/romainguy/adrift
#   file tools/gen_dsp_tables.py, line 16
#   licence (as GitHub reports it): MPL-2.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fmt_array(vals: list[int], per_line: int = 8, hex_fmt: bool = False) -> str:
    lines = []
    for i in range(0, len(vals), per_line):
        chunk = vals[i : i + per_line]
        if hex_fmt:
            s = ", ".join(f"0x{v:08X}u" for v in chunk)
        else:
            s = ", ".join(str(v) for v in chunk)
        lines.append(f"    {s},")
    return "\n".join(lines)
