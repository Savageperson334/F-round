# fix
#
# Copied verbatim from https://github.com/cognitivegears/ha-escpos-thermal-printer
#   file scripts/md_fix.py, line 37
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Thermal printers and obsolete output
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

FENCE = re.compile(r"^(\s*)(```|~~~)([^`~]*)$")

HEADING = re.compile(r"^(\s*)(#{1,6}) (.+)$")

LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+\.) ")


def is_continuation(line: str) -> bool:
    """A line that continues a previous list item (indented under it)."""
    # Conservative: anything that starts with 2+ spaces is treated as a
    # list continuation.
    return len(line) > 0 and line[0] in (" ", "\t")


def fix(text: str) -> str:
    lines = text.splitlines(keepends=False)
    in_fence = False
    fence_marker = None
    out: list[str] = []

    def prev_nonempty():
        for ln in reversed(out):
            if ln.strip():
                return ln
        return None

    def is_list(line: str) -> bool:
        m = LIST_ITEM.match(line)
        return m is not None

    def is_blank(line: str) -> bool:
        return line.strip() == ""

    for i, line in enumerate(lines):
        fm = FENCE.match(line)
        if fm and not in_fence:
            in_fence = True
            fence_marker = fm.group(2)
            indent, _, lang = fm.groups()
            # MD040: add 'text' lang if missing.
            if not lang.strip():
                line = f"{indent}{fence_marker}text"  # noqa: PLW2901
            # MD031: blank line before fence if previous line isn't blank.
            if out and not is_blank(out[-1]):
                # Don't insert a blank line if the previous line is a
                # list-item or heading that owns this code block; the
                # check below for "after fence" handles spacing.
                # Actually, MD031 expects a blank before the fence, so
                # always insert (unless prev is blank).
                out.append("")
            out.append(line)
            continue
        if in_fence:
            if line.strip().startswith(fence_marker or "```"):
                # closing fence
                in_fence = False
                fence_marker = None
                out.append(line)
                # MD031: blank line after closing fence if next isn't blank.
                next_line = lines[i + 1] if i + 1 < len(lines) else ""
                if next_line and not is_blank(next_line):
                    out.append("")
                continue
            # Inside fence — preserve verbatim.
            out.append(line)
            continue

        # Not in a fence.
        # MD022: blank line after a heading.
        hm = HEADING.match(line)
        if hm:
            if out and not is_blank(out[-1]):
                out.append("")
            out.append(line)
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if next_line and not is_blank(next_line):
                # Defer to next iteration to detect; insert blank now.
                # (We can't insert here without consuming next line, so
                # we'll handle by appending after.)
                out.append("")
                # And skip the auto-insert via a sentinel? Simpler: rely
                # on this insertion now; the next iteration will see the
                # blank we appended via `prev_nonempty` check.
                # But we mustn't double-insert. Just continue.
                continue
            continue

        # MD032: blank line before list start.
        if is_list(line):
            prev = out[-1] if out else ""
            if prev and not is_blank(prev) and not is_list(prev) and not is_continuation(prev):
                out.append("")
        out.append(line)

    return "\n".join(out) + ("\n" if text.endswith("\n") else "")
