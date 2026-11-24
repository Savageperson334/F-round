# apply_units
#
# Copied verbatim from https://github.com/pyrocko/pyrocko
#   file src/plot/__init__.py, line 79
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

cm = 28.3465

inch = 72.

point = 1.

units_dict = {
    'point': point,
    'inch': inch,
    'cm': cm,
}


def apply_units(x, units):
    if isinstance(units, str):
        units = units_dict[units]

    if isinstance(x, (int, float)):
        return x / units
    else:
        if isinstance(x, tuple):
            return tuple(v / units for v in x)
        else:
            return list(v / units for v in x)
