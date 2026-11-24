# synthesise
#
# Copied verbatim from https://github.com/piersfinlayson/rom-bus-control-protocol
#   file reference/host/68k/amiga-boot/tools/mkchime.py, line 85
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Retro computing
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

ATTACK = 0.0012

NOTES = (
    (0.000, 293.665, 1.00),
    (0.130, 440.000, 0.90),
)

PARTIALS = (
    (1.000, 1.000, 1.00),
    (2.000, 0.400, 1.55),
    (3.000, 0.200, 2.10),
    (4.013, 0.100, 2.80),
    (5.432, 0.050, 3.60),
)

STRIKE = ((6.81, 0.10), (9.23, 0.07), (11.71, 0.05))

STRIKE_TAU = 0.010

TAU = 0.135

TWO_PI = 2.0 * math.pi


def synthesise(rate, count):
    """Return `count` floating point samples of the chime, unnormalised."""
    out = [0.0] * count
    for start, freq, level in NOTES:
        first = int(start * rate)
        for i in range(first, count):
            t = (i - first) / rate
            env = level * (1.0 - math.exp(-t / ATTACK))
            total = 0.0
            for ratio, amp, fade in PARTIALS:
                total += amp * math.exp(-t * fade / TAU) * math.sin(
                    TWO_PI * freq * ratio * t)
            knock = math.exp(-t / STRIKE_TAU)
            for ratio, amp in STRIKE:
                total += amp * knock * math.sin(TWO_PI * freq * ratio * t)
            out[i] += env * total
    return out
