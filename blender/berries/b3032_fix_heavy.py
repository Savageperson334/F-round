# fix_heavy
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/patch_lint.py, line 233
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def fix_heavy(f, which):
    """the feature set with the cheap equivalents of the heavy features in `which` applied."""
    g = dict(f)
    for w in which:
        if w == "TWIN LADDER":
            g["tw"] = 1
        elif w == "COMB":
            g["tw"] = 0
            g["fbmod"] = 0
        elif w == "SUPER 4+ SAWS":
            if g["o1m"] == 5 and g["o1saw"] >= 4:
                g["o1saw"] = 3
            if g["o2on"] and g["o2m"] == 5 and g["o2saw"] >= 4:
                g["o2saw"] = 3
        elif w == "FILTER A 24 dB":
            g["sl"] = 1
        elif w == "OSC MODEL FM":
            if g["o1m"] == 6:
                g["o1m"] = 0
            if g["o2on"] and g["o2m"] == 6:
                g["o2m"] = 0
        elif w == "DIRT CRUSH":
            g["da"] = 1 if g["da"] == 5 else g["da"]
            g["db"] = 1 if g["db"] == 5 else g["db"]
        elif w == "TWIN SVF HP":
            g["tw"] = 1
    return g
