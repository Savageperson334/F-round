# range_converter
#
# Copied verbatim from https://github.com/la-niche/nonos
#   file cli/src/nonos_cli/parsing.py, line 111
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def range_converter(extent, abscissa, ordinate):
    if len(extent) == 4:
        return (
            _ if (_ := extent[0]) is not None else abscissa.min(),
            _ if (_ := extent[1]) is not None else abscissa.max(),
            _ if (_ := extent[2]) is not None else ordinate.min(),
            _ if (_ := extent[3]) is not None else ordinate.max(),
        )
    elif len(extent) == 2:
        return (
            _ if (_ := extent[0]) is not None else abscissa.min(),
            _ if (_ := extent[1]) is not None else abscissa.max(),
        )
    else:
        raise TypeError(f"Expected extent to be of length 2 or 4, got {len(extent)=}")
