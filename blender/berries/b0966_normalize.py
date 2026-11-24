# normalize
#
# Copied verbatim from https://github.com/alepersichetti/WyrmHex
#   file wyrmhex.py, line 2046
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Cave surveys and subterranean maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize(values):
    """Rescale {key: number} so the lowest is 0 and the highest is 1."""
    low, high = min(values.values()), max(values.values())
    spread = (high - low) or 1.0
    return {k: (v - low) / spread for k, v in values.items()}
