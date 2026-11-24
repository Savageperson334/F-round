# build_unicode
#
# Copied verbatim from https://github.com/NK8007/gofonix
#   file scripts/gen_fixtures.py, line 83
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

UNICODE_PARAGRAPHS = [
    "The note said, \u201cthis pipeline is well\u2013behaved\u201d \u2014 and the result was reproducible.",
    "A na\u00efve approach would ignore the caf\u00e9 sign\u2019s accents, but our tokenizer keeps every byte.",
    "The phrase is \u2018obvious\u2019 once the spans are visible; the r\u00e9sum\u00e9 of changes covered 2018\u20132024.",
    "The fa\u00e7ade of simplicity hides care: \u201cdon\u2019t\u201d and \u201cit\u2019s\u201d use a curly apostrophe here.",
    "From na\u00efvet\u00e9 to expertise \u2014 a long road \u2013 the system kept the contract opaque and stable.",
    "The motto was \u2018measure twice\u2019, followed by the practical reminder, \u201cthen measure again.\u201d",
]


def build_unicode(target_bytes: int) -> str:
    out = []
    size = 0
    i = 0
    para = []
    n = 0
    while size < target_bytes:
        s = UNICODE_PARAGRAPHS[i % len(UNICODE_PARAGRAPHS)]
        para.append(s)
        size += len(s.encode("utf-8")) + 1
        n += 1
        if n >= 3:
            out.append(" ".join(para) + "\n\n")
            para = []
            n = 0
        i += 1
    if para:
        out.append(" ".join(para) + "\n")
    return "".join(out)
