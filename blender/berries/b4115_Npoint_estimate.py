# Npoint_estimate
#
# Copied verbatim from https://github.com/zaman13/Vector-Field-Topolgy-2D
#   file Codes/Python codes/Version 1.1/local_minima.py, line 186
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Peculiar interfaces, worlds, visual systems
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def Npoint_estimate(avgF_sort,th,order):
    # Estimate the number of critical points
    # For order == 0
    # Select the points with high local average values, meaning it was surrounded by zeros.     
    # As avF_sort is sorted, the [0] element is the maximum value. For points with local average th times
    # lower than avF, we disregard them.
    # For order == 1, the process is reversed (high local averages are discarded). The [0] element is the minimum value
    Npoints = 0
    for m in range(len(avgF_sort)):
        temp = avgF_sort[m]/avgF_sort[0]


        flg = (temp < th) if order == 0 else (temp > 1/th)

        print('m = %i, ratio = %1.3f, flag = %i \n' % (m,temp,flg))

        if flg == 1:
            break

        Npoints = Npoints + 1


    return Npoints
