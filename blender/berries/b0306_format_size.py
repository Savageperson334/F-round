# format_size
#
# Copied verbatim from https://github.com/HubbleNetwork/hubble-device-sdk
#   file tools/ci/summarize_footprint.py, line 31
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Satellites and orbital systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def format_size(size_bytes):
    """Format size in bytes to human-readable format."""
    if size_bytes is None or size_bytes < 0:
        return 'N/A'
    for unit in ['B', 'KB', 'MB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} GB"
