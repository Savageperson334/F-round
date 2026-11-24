# summary
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file scripts/benchmark_render.py, line 286
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from statistics import median


def summary(values: list[float | None]) -> dict | None:
    numbers = [v for v in values if v is not None]
    if not numbers:
        return None
    return {"median": round(median(numbers), 4), "min": min(numbers), "max": max(numbers)}
