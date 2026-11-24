# extract_text
#
# Copied verbatim from https://github.com/zrmzur24/lean-ctx-light
#   file scripts/analyze-sessions.py, line 99
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                for key in ('text', 'thinking'):
                    if key in block and isinstance(block[key], str):
                        parts.append(block[key])
        return '\n'.join(parts)
    return ''
