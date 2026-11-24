# compute_moving_average
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file stratigraphy/isotope_analysis.py, line 295
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import numpy as np


def compute_moving_average(values: np.ndarray, window: int = 5, mode: str = "center") -> np.ndarray:
    """
    计算移动平均

    参数:
        values: 输入数据
        window: 窗口大小 (必须是奇数)
        mode: 'center' 或 'right'

    返回:
        平滑后的数组
    """
    if window < 1:
        return np.asarray(values, dtype=float)

    if window % 2 == 0:
        window += 1  # 必须奇数

    if mode == "center":
        # 中心移动平均: 边缘按实际重叠窗口归一化。
        # 旧实现 np.convolve(mode="same") 在两端仍除以完整窗口,
        # 导致序列两端被系统性压低。
        smoothed = np.convolve(values, np.ones(window), mode="same")
        counts = np.convolve(np.ones_like(values), np.ones(window), mode="same")
        smoothed = smoothed / counts
    else:
        # 右对齐。
        # ``np.zeros_like`` 继承输入的 dtype, 整数序列的均值因此被向零截断:
        # [1..6] window=3 得到 [1, 1, 2, 3, 4, 5] 而不是 [1.0, 1.5, 2.0, ...]。
        # center 模式因为 np.convolve 会提升为 float 而是对的, 于是同一个
        # 输入在两个模式下给出不同结果。
        smoothed = np.zeros(len(values), dtype=float)
        for i in range(len(values)):
            start = max(0, i - window + 1)
            smoothed[i] = np.mean(values[start : i + 1])

    return smoothed
