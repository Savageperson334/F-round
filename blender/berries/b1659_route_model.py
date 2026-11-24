# route_model
#
# Copied verbatim from https://github.com/ductone/orrery
#   file research/modelbench/fetch.py, line 792
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

BUDGET_RE = re.compile(r"^\d+(\.\d+)?k$")

CLAUDE_FAMS = "opus|sonnet|haiku|fable|mythos"

DATE8 = re.compile(r"-(20\d\d)-?(\d\d)-?(\d\d)(?=$|-)")

DOT_FAMILIES = re.compile(
    r"^(claude-(?:%s)|gpt|grok|gemini|glm|kimi-k|minimax-m|mimo-v|muse-spark|qwen|deepseek-v|mistral-(?:large|medium|small))-?(\d+)-(\d)(?=$|-)" % CLAUDE_FAMS
)

EFFORT_WORDS = {
    "none": "none", "minimal": "minimal", "low": "low",
    "medium": "medium", "med": "medium", "high": "high", "xhigh": "xhigh",
    "x-high": "xhigh", "extra-high": "xhigh", "extrahigh": "xhigh",
    "max": "max", "maximum": "max",
    "non-reasoning": "none", "nonreasoning": "none", "no-thinking": "none",
    "nothinking": "none", "non-thinking": "none", "instant": "none",
    "thinking": None, "reasoning": None, "unknown": None, "enabled": None,
    "default": None, "effort": None,
}

MONTH_DATE_RE = re.compile(r"-(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*-20\d\d(?=$|-)")

UNSPEC = "unspecified"

LEVEL_THINKING_RE = re.compile(r"^(minimal|low|medium|high|xhigh|max)thinking$")


def _strip_vendor(s):
    s = s.strip()
    if s.startswith("http"):
        s = s.rstrip("/").rsplit("/", 1)[-1]
    if "/" in s:
        s = s.rsplit("/", 1)[-1]
    return s


def combine_levels(levels):
    lv = [x for x in levels if x]
    if not lv:
        return UNSPEC
    if len(set(lv)) == 1:
        return lv[0]
    return UNSPEC


def effort_word(w):
    """Normalize one effort word. Returns (is_effort, level_or_None)."""
    w = w.strip().lower().replace(" ", "-").replace("_", "-")
    if w in EFFORT_WORDS:
        return True, EFFORT_WORDS[w]
    if BUDGET_RE.match(w):
        return True, None
    m = LEVEL_THINKING_RE.match(w)
    if m:
        return True, m.group(1)
    return False, None


def parse_name(raw, source=None):
    """Split a raw model string into (normalized_name, effort, effort_raw, harness).

    normalized_name is the generic slug before alias lookup. effort is a level
    from EFFORTS or 'unspecified'; effort_raw is the exact fragment(s) that
    carried effort information, or None.
    """
    s = _strip_vendor(raw)
    frags, levels = [], []
    harness = None
    date_suffix = None
    extra_words = []

    # Parenthesized groups: "(High)", "(codex-harness)", "(0813)", "(thinking-minimal)"
    for g in re.findall(r"\(([^)]*)\)", s):
        gl = g.strip().lower()
        if "harness" in gl:
            harness = re.sub(r"[-\s]*harness", "", gl).strip() or gl
        elif re.fullmatch(r"\d{4}", gl):
            date_suffix = gl
        else:
            words = re.split(r"[\s\-_,]+", gl)
            words = [w for w in words if w]
            # "Extra High" -> xhigh
            joined = "-".join(words)
            ok, lvl = effort_word(joined)
            if ok:
                frags.append(g)
                levels.append(lvl)
            elif words and all(effort_word(w)[0] or w == "extra" for w in words):
                frags.append(g)
                ws = joined.replace("extra-high", "xhigh")
                levels.append(combine_levels([effort_word(w)[1] for w in ws.split("-")]))
            else:
                extra_words.append(gl.replace(" ", "-"))
    s = re.sub(r"\([^)]*\)", " ", s)

    # Epoch-style "<slug>_<effort>" suffix.
    if "_" in s:
        base, suf = s.rsplit("_", 1)
        sl = suf.strip().lower()
        m = re.fullmatch(r"pro(none|minimal|low|medium|high|xhigh|max|unknown)", sl)
        if m:
            s = base + "-pro"
            frags.append(suf)
            levels.append(EFFORT_WORDS[m.group(1)])
        else:
            ok, lvl = effort_word(sl)
            if ok:
                s = base
                frags.append(suf)
                levels.append(lvl)

    s = s.strip().lower()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    for k in ("extra-high", "x-high", "non-reasoning", "no-thinking", "non-thinking"):
        if re.search(r"(^|-)%s($|-)" % k, s):
            frags.append(k)
            levels.append(EFFORT_WORDS[k])
            s = re.sub(r"(^|-)%s(?=$|-)" % k, "", s)

    # Dates: YYYYMMDD / YYYY-MM-DD. DeepSeek uses MMDD to distinguish
    # checkpoints (v4-flash-0731, v4-pro-0813), so keep MMDD there.
    def _date(m):
        if s.startswith("deepseek"):
            return "-" + m.group(2) + m.group(3)
        return ""
    s = DATE8.sub(_date, s)
    s = MONTH_DATE_RE.sub("", s)  # Epoch display names: "Gemini 2.5 Pro (Jun 2025)"
    s = re.sub(r"(?<=\d)p(?=\d)", ".", s)  # fireworks/ramp style 5p3 -> 5.3
    s = re.sub(r"^qwen-(\d)", r"qwen\1", s)

    toks = [t for t in s.split("-") if t]
    # Effort markers are only taken from the trailing run of effort/budget/
    # MMDD tokens ("...-high-32k", "...-high-0813"), so size words inside a
    # name ("phi-3-medium-4k-instruct") survive.
    j = len(toks)
    while j - 1 > 0 and (effort_word(toks[j - 1])[0] or re.fullmatch(r"\d{4}", toks[j - 1])
                         or toks[j - 1] in ("preview", "exp")):
        j -= 1
    # OpenRouter slugs use level words as model names ("fugu-max"); only the
    # o-series carry a level suffix ("o4-mini-high"). Thinking markers still strip.
    keep_levels = source == "openrouter" and not re.match(r"^o\d", toks[0] if toks else "")
    kept = []
    eff_idx = set()
    for i, t in enumerate(toks):
        ok, lvl = effort_word(t)
        is_budget = BUDGET_RE.match(t) is not None
        if i == 0 or i < j or not ok or (keep_levels and lvl is not None):
            kept.append(t)
            continue
        if is_budget:
            # only a thinking budget when next to another effort marker
            nb = (i - 1 in eff_idx) or (i + 1 < len(toks) and effort_word(toks[i + 1])[0] and not BUDGET_RE.match(toks[i + 1]))
            if not nb:
                kept.append(t)
                continue
        if t == "max" and kept and re.match(r"^qwen[\d.]*$", kept[-1]):
            kept.append(t)  # "qwen3.8-max" / "qwen-max" are model names
            continue
        if t == "medium" and re.match(r"^(mistral|magistral|devstral|phi)", "-".join(kept)):
            kept.append(t)  # "mistral-medium", "phi-3-medium"
            continue
        eff_idx.add(i)
        frags.append(t)
        levels.append(lvl)
    if source == "livebench" and kept and kept[-1] == "base":
        kept.pop()
        frags.append("base")
        levels.append("none")  # LiveBench '-base' = thinking disabled
    s = "-".join(kept)

    # Version separators: 5p5 -> 5.5, claude-opus-5-5 -> claude-opus-5.5
    s = re.sub(r"(?<=\d)p(?=\d)", ".", s)
    s = re.sub(r"^qwen-(\d)", r"qwen\1", s)
    for _ in range(2):
        s = DOT_FAMILIES.sub(lambda m: "%s-%s.%s" % (m.group(1), m.group(2), m.group(3)) if not m.group(1).endswith(("kimi-k", "minimax-m", "mimo-v", "deepseek-v")) and not m.group(1).startswith("qwen") else "%s%s.%s" % (m.group(1), m.group(2), m.group(3)), s)
    s = re.sub(r"^qwen-(\d)", r"qwen\1", s)
    # claude-3.5-sonnet / claude-4-opus -> claude-sonnet-3.5 / claude-opus-4
    s = re.sub(r"^claude-(\d+)(?:[.-](\d))?-(%s)(?=$|-)" % CLAUDE_FAMS,
               lambda m: "claude-%s-%s%s" % (m.group(3), m.group(1), "." + m.group(2) if m.group(2) else ""), s)
    if extra_words:
        s = s + "-" + "-".join(extra_words)
    if date_suffix:
        s = s + "-" + date_suffix
    s = re.sub(r"-+", "-", s).strip("-")

    effort = combine_levels(levels) if frags else UNSPEC
    effort_raw = " ".join(frags) if frags else None
    return s, effort, effort_raw, harness


def route_model(route):
    wire = route.split("/", 1)[1] if "/" in route else route
    name, _, _, _ = parse_name(wire)
    return name
