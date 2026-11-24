# draft
#
# Copied verbatim from https://github.com/BAHALLA/orrery
#   file core/orrery_core/studio/demo/writer.py, line 48
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

MAX_REQUEST_CHARS = 8192


def draft(request: str) -> str:
    """The deterministic draft for *request*."""
    title = "Release notes"
    bullets: list[str] = []
    for raw in request[:MAX_REQUEST_CHARS].splitlines():
        line = raw.strip().lstrip("-*• ").strip()
        if not line:
            continue
        if raw.strip().startswith("#"):
            title = line.lstrip("# ").strip() or title
            continue
        bullets.append(f"- {line}")
    if not bullets:
        bullets.append("- (nothing to report)")
    return f"# {title}\n\n" + "\n".join(bullets) + "\n"
