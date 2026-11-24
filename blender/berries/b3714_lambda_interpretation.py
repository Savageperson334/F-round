# lambda_interpretation
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file phylogenetics/signal.py, line 617
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def lambda_interpretation(lambda_value: float) -> str:
    """
    解释 Pagel's λ 值的含义

    参数:
        lambda_value: λ 估计值

    返回:
        解释字符串
    """
    if lambda_value < 0:
        return "Invalid (λ < 0)，可能由于数值问题导致"
    elif lambda_value < 0.1:
        return "几乎无系统发育信号 (λ ≈ 0)，性状独立于系统发育"
    elif lambda_value < 0.5:
        return "弱系统发育信号 (0 < λ < 0.5)"
    elif lambda_value < 0.9:
        return "中等系统发育信号 (0.5 < λ < 1)"
    elif lambda_value <= 1.0:
        return "强系统发育信号 (λ ≈ 1)，符合 Brown 运动进化"
    else:
        return f"λ > 1 ({lambda_value:.4f})，可能存在强烈的系统发育依赖或模型误设"
