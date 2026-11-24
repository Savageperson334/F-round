# resolve_line_style
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file visualization/line_styles.py, line 7
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def resolve_line_style(app_state, style_key: str, fallback: dict) -> dict:
    """Resolve line style with app_state overrides."""
    style = {}
    try:
        style = app_state.line_styles.get(style_key, {}) or {}
    except Exception:
        style = {}

    resolved = dict(fallback)
    for key, value in style.items():
        if key == 'color':
            if value is not None and value != '':
                resolved['color'] = value
        elif value is not None:
            resolved[key] = value
    return resolved
