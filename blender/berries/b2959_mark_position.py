# mark_position
#
# Copied verbatim from https://github.com/oscillr/LRRY
#   file lrry/tools/bench_record.py, line 281
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def mark_position(run_s, mark_after):
    """(BENCHR2) the START MARK: where in the recording the test begins, seconds from the file's start. The Mac notes how much sound the recording holds when it sends the
    `bench run` command (run_s) and puts the mark `mark_after` seconds later. Why later and not earlier: the unit does its per-test reset (the effect lines and phases
    are cleared, firmware/src/bench.c bench_reset_phases) in the first half of the run, so the reset's own noise comes AFTER the command, and the timeline's first
    note is held back by a silent lead-in (the runner's --lead). Both are delayed by the same unknown pipeline offset O (the unit's USB buffer, CoreAudio, sox's write
    buffer; 0 to about 0.1 s). The mark must fall after the reset noise (O + a few ms) and before the first note (O + lead): with O at most 0.1 s and the lead 0.6 s the
    middle, 0.35 s, is 0.25 s from both. The accuracy needed is therefore +-0.2 s, which the file size and the clock give."""
    return run_s + mark_after
