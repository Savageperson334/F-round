# format_number_to_human_readable
#
# Copied verbatim from https://github.com/earthspecies/avex
#   file scripts/icassp/extract_metrics_from_logs.py, line 19
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_number_to_human_readable(num_str: str) -> str:
    """Convert a number string to human-readable format (K, M, B).

    Args:
        num_str: Number as string (e.g., "90010417", "2.40M")

    Returns:
        Human-readable format (e.g., "90.01M", "2.40M")
    """
    if not num_str or num_str in ["", "nan", "NaN"]:
        return num_str

    # If already in human-readable format, return as is
    if any(suffix in num_str.upper() for suffix in ["K", "M", "B"]):
        return num_str

    try:
        num = float(num_str)

        if num >= 1_000_000_000:
            return f"{num / 1_000_000_000:.2f}B"
        elif num >= 1_000_000:
            return f"{num / 1_000_000:.2f}M"
        elif num >= 1_000:
            return f"{num / 1_000:.2f}K"
        else:
            return str(int(num))
    except (ValueError, TypeError):
        return num_str
