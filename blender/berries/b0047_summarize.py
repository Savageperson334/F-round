# summarize
#
# Copied verbatim from https://github.com/Anko3o/Orrery
#   file orrery/orrery-export.py, line 202
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def summarize(body, limit=110):
    """正文首段，去掉 meaning 注释行和 wiki 括号，截断到 limit 字。"""
    lines = []
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", ">", "💭", "👣", "---")):
            continue
        lines.append(s)
        if len("".join(lines)) > limit * 2:
            break
    text = " ".join(lines)
    text = text.replace("[[", "").replace("]]", "")
    return text[:limit] + ("…" if len(text) > limit else "")
