# runs
#
# Copied verbatim from https://github.com/KyleBastien/weather-balloon-logger
#   file scripts/generate_silkscreen_logo.py, line 35
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Weather balloon telemetry
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def runs(row: list[bool]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    start: int | None = None
    for index, value in enumerate(row + [False]):
        if value and start is None:
            start = index
        elif not value and start is not None:
            result.append((start, index))
            start = None
    return result
