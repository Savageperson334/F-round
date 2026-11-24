# parse_json_lenient
#
# Copied verbatim from https://github.com/ItIsMixian/Orrery
#   file scripts/docsite/_llm.py, line 443
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import json
import re

_BRACE = re.compile(r"\{[\s\S]*\}")

_FENCE = re.compile(r"^```(?:json)?\s*|\s*```$", re.M)


def parse_json_lenient(text: str) -> dict:
    """Best-effort JSON-object extraction from a model reply.

    Handles ```json fences and chatter around a single top-level object.
    Always returns a dict; on failure includes ``parse_error: True``.
    """
    if not text:
        return {"raw_text": "", "parse_error": True, "error": "empty response"}
    s = text.strip()
    if s.startswith("```"):
        s = _FENCE.sub("", s).strip()
    try:
        v = json.loads(s)
        return v if isinstance(v, dict) else {"value": v}
    except json.JSONDecodeError:
        pass
    m = _BRACE.search(s)
    if m:
        try:
            v = json.loads(m.group(0))
            return v if isinstance(v, dict) else {"value": v}
        except json.JSONDecodeError as e:
            return {"raw_text": text, "parse_error": True, "error": "brace parse: %s" % e}
    return {"raw_text": text, "parse_error": True, "error": "no JSON object found"}
