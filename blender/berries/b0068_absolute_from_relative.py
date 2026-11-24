# absolute_from_relative
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file data/metadata_profile/ratios.py, line 144
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

_PERCENT = 100.0


def absolute_from_relative(value: float, relative_percent: float) -> float:
    """按 B6.6 由相对不确定度（%）换算绝对不确定度。

    Args:
        value: 比值数值。
        relative_percent: 相对不确定度，百分数（档案示例 ``0.1`` 表示 0.1%）。

    Returns:
        绝对不确定度 ``value * relative_percent / 100``。
    """
    return value * relative_percent / _PERCENT
