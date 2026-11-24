# exposure_needed
#
# Copied verbatim from https://github.com/topherchris420/nocturne
#   file vdl7/pilot.py, line 405
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from statistics import NormalDist
import math


def exposure_needed(rate: float, rate_ratio: float, alpha: float = 0.05, power: float = 0.8) -> float:
    """Segment-nights per arm to detect `rate_ratio` against a baseline
    `rate` (events per segment-night), two-sided, by the normal
    approximation to the log rate ratio."""
    if not (math.isfinite(rate) and rate > 0):
        raise ValueError(f"baseline rate must be a positive number of events per segment-night, got {rate:g}")
    if not (math.isfinite(rate_ratio) and rate_ratio > 0) or rate_ratio == 1:
        raise ValueError(f"rate ratio must be positive and not 1 (1 is no change to detect), got {rate_ratio:g}")
    if not (0 < alpha < 1 and 0 < power < 1):
        raise ValueError("alpha and power must be between 0 and 1")
    z = NormalDist().inv_cdf(1 - alpha / 2) + NormalDist().inv_cdf(power)
    return z * z * (1 / rate + 1 / (rate * rate_ratio)) / math.log(rate_ratio) ** 2
