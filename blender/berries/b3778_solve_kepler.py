# solve_kepler
#
# Copied verbatim from https://github.com/tjyank/orrery-tui
#   file orrery/kepler.py, line 27
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math


def solve_kepler(m: float, e: float) -> float:
    """Eccentric anomaly E for mean anomaly M (radians), elliptic orbits."""
    m = math.remainder(m, math.tau)
    ecc = m + e * math.sin(m) if e < 0.8 else math.pi * (1 if m >= 0 else -1)
    for _ in range(50):
        f = ecc - e * math.sin(ecc) - m
        step = f / (1 - e * math.cos(ecc))
        ecc -= step
        if abs(step) < 1e-13:
            break
    return ecc
