# continuous_valid_length
#
# Copied verbatim from https://github.com/qiaoguanren/TrafficGamer
#   file train_trafficgamer_waymo.py, line 103
#   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def continuous_valid_length(valid_mask):
    max_length = 0
    current_length = 0

    for is_valid in valid_mask:
        if is_valid:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0

    # 检查最后一段连续True的长度
    if current_length > max_length:
        max_length = current_length

    return max_length
