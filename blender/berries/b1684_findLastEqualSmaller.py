# findLastEqualSmaller
#
# Copied verbatim from https://github.com/eeyrw/music-box-nv32
#   file BinarySearch.py, line 2
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def findLastEqualSmaller(arr, key):
    left = 0
    right = len(arr) - 1
    length = len(arr)

    # 这里必须是 <=
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= key:
            right = mid - 1
        else:
            left = mid + 1
    if left>=length:
        left=length-1
    return left
