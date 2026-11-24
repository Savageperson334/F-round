# itv2time
#
# Copied verbatim from https://github.com/HuberTRoy/MusicBox
#   file MusicPlayer/widgets/addition.py, line 13
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def deal_time(x):
    x = str(x)
    if len(x) == 1:
        x = '0' + x

    return x


def itv2time(iItv):
    iItv = int(iItv)

    # 地板除求小时整数。
    h = iItv//3600
    # 求余数。
    h_remainder = iItv % 3600

    # 地板除求分钟整数。
    m = h_remainder // 60
    # 求余数 为秒。
    s = h_remainder % 60

    return ":".join(map(deal_time,(m,s)))
