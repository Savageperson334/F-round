# make_pretty_size_str
#
# Copied verbatim from https://github.com/nion-software/nionswift
#   file nion/swift/model/Utility.py, line 809
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Scientific visualizations
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def make_pretty_size_str(total_bytes: int | float) -> str:
    """Format a number into a string with units Byte(s), KB, MB, GB, or TB formatted to two decimal places.

    See https://stackoverflow.com/a/31631711.
    """
    total_bytes = float(total_bytes)
    kilobyte = 1024.0
    if total_bytes < kilobyte:
        return f"{total_bytes} {'Bytes' if total_bytes != 1 else 'Byte'}"

    megabyte = 1048576.0  # 1024 ** 2
    if total_bytes < megabyte:
        return f"{total_bytes / kilobyte:.2f} KB"

    gigabyte = 1073741824.0  # 1024 ** 3
    if total_bytes < gigabyte:
        return f"{total_bytes / megabyte:.2f} MB"

    terabyte = 1099511627776.0  # 1024 ** 4
    if total_bytes < terabyte:
        return f"{total_bytes / gigabyte:.2f} GB"
    else:
        return f"{total_bytes / terabyte:.2f} TB"
