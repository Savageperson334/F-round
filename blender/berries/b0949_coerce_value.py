# coerce_value
#
# Copied verbatim from https://github.com/akuhara/SEIS_FILO
#   notebook notebooks/joint_inv_ui.ipynb (its code cells joined in order; line 84 of those)
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def parse_bool(text: str) -> bool:
    value = text.strip().lower()
    return value in {"t", ".true.", "true", "1", "yes", "y"}


def coerce_value(kind: str, text: str):
    raw = text.strip()
    if kind == "bool":
        return parse_bool(raw)
    if kind == "int":
        return int(float(raw))
    if kind == "float":
        return float(raw)
    return raw
