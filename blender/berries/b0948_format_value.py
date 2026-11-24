# format_value
#
# Copied verbatim from https://github.com/akuhara/SEIS_FILO
#   notebook notebooks/joint_inv_ui.ipynb (its code cells joined in order; line 74 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_value(kind: str, value):
    if kind == "bool":
        return "T" if bool(value) else "F"
    if kind == "int":
        return str(int(value))
    if kind == "float":
        return str(float(value))
    return str(value)
