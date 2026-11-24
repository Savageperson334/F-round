# why_text
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/bench_run.py, line 592
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

TC_WHY = {"OK": "core 1 plays part 2",
          "NOANSWER": "core 1 did not answer at the start (the unit plays on one core)",
          "NOTARMED": "the start was not armed",
          "SKIPBOOT": "the boot guard skipped the start (the last start died within 30 s)",
          "NOTBUILT": "this build has no second core"}


def why_text(w):
    if w in TC_WHY:
        return TC_WHY[w]
    if w.startswith("FAIL-"):
        return f"core 1 was stopped during the session ({w[5:]}, a strike)"
    if w.startswith("PREV-"):
        return f"the last session ended in a strike ({w[5:]}): one core this power-on, the next power-on tries again"
    return w
