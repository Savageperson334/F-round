# floor_breach
#
# Copied verbatim from https://github.com/NDilanka/orrery
#   file engine/orrery_loop/decide.py, line 100
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def floor_breach(pass_count: int, floor: int) -> bool:
    """Pure regression-floor decision: has ``pass_count`` dropped below ``floor``?

    The ONE place expressing "did the passing-test count drop" — BMAD's dev-gate, post-review,
    and post-smoke phase boundaries (:mod:`orrery_loop.bmad.driver`) each independently reimplemented
    this exact ``<`` check before this helper existed, one per boundary. Kept deliberately
    trivial: the point isn't the arithmetic, it's having ONE definition every call site shares,
    so a future refinement (e.g. a tolerance) changes in one place instead of three.
    """
    return pass_count < floor
