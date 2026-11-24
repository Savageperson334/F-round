# normalize_class_label
#
# Copied verbatim from https://github.com/rudolffu/specbox
#   file specbox/qtmodule/qtmodule_enhanced.py, line 176
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_CLASS_LABEL_ALIASES = {
    "QSO(Default)": "QSO_DEFAULT",
    "QSO_DEFAULT": "QSO_DEFAULT",
    "QSO": "QSO",
    "QSO(narrow)": "QSO_NARROW",
    "QSO(Narrow)": "QSO_NARROW",
    "QSO_NARROW": "QSO_NARROW",
    "QSO(BAL)": "QSO_BAL",
    "QSO_BAL": "QSO_BAL",
    "QSO(FeLoBAL)": "QSO_FELOBAL",
    "QSO_FELOBAL": "QSO_FELOBAL",
    "LIKELY": "LIKELY_Q",
    "LIKELY_Q": "LIKELY_Q",
    "GALAXY": "GALAXY",
    "STAR": "STAR",
    "UNKNOWN": "UNKNOWN",
    "BAD": "BAD",
}


def normalize_class_label(value):
    if value is None:
        return ""
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return ""
    return _CLASS_LABEL_ALIASES.get(text, text)
