# make_alias_name
#
# Copied verbatim from https://github.com/pysmo/pysmo
#   file utils/gen_literals.py, line 138
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def make_alias_name(
    enum_name: str, prefix: str | None, suffix: str | None, rename: dict[str, str]
) -> str:
    if enum_name in rename:
        return rename[enum_name]
    base = enum_name
    if prefix:
        base = f"{prefix}{base}"
    if suffix:
        base = f"{base}{suffix}"
    return base
