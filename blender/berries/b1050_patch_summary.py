# patch_summary
#
# Copied verbatim from https://github.com/amacias/octo-vave
#   file server.py, line 1685
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

ID_RE = re.compile(r"^[a-z0-9][a-z0-9\-]{0,31}$")

OFFICIAL_FORMAT = "official/dx7-voice+fx"

PATCH_SCHEMA = 2


def normalize_patch(d):
    """Schema v2 view of a stored patch, without changing the file.
    Returns (view, stored schema version)."""
    stored = d.get("schemaVersion")
    out = dict(d)
    if stored is None:  # v1: stock DX7 voice + FX; "firmware" was a loose string
        legacy = d.get("firmware")
        out["firmware"] = {"id": "official"}
        if isinstance(legacy, str) and legacy and legacy != "official":
            out["legacyFirmware"] = legacy[:32]
        out["format"] = OFFICIAL_FORMAT
        out["schemaVersion"] = PATCH_SCHEMA
        return out, 1
    fw = d.get("firmware")
    if not isinstance(fw, dict) or not isinstance(fw.get("id"), str):
        out["firmware"] = {"id": fw if isinstance(fw, str) and ID_RE.match(fw) else "unknown"}
    if not isinstance(d.get("format"), str):
        out["format"] = "unknown/unknown"
    return out, stored


def patch_summary(name, raw):
    """One row of GET /api/patches."""
    error = None
    if not isinstance(raw, dict):
        error, raw = "unreadable JSON", {}
    d, stored = normalize_patch(raw)
    tags = d.get("tags") if isinstance(d.get("tags"), list) else []
    return {
        "name": name, "favorite": bool(d.get("favorite")),
        "notes": d.get("notes", "") if isinstance(d.get("notes"), str) else "",
        "modified": d.get("modified", ""), "tags": [str(t) for t in tags],
        "program": d.get("program"),
        "hasVoice": bool(d.get("voice")), "hasFx": bool(d.get("fx")),
        "params": len(d["params"]) if isinstance(d.get("params"), dict) else 0,
        "cc": len(d["cc"]) if isinstance(d.get("cc"), list) else 0,
        "sysex": len(d["sysex"]) if isinstance(d.get("sysex"), list) else 0,
        "firmware": d["firmware"], "format": d["format"], "schemaVersion": stored,
        "legacyFirmware": d.get("legacyFirmware"), "error": error,
    }
