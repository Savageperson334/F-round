# muFitting
#
# Copied verbatim from https://github.com/LiquidFun/Simple-Traffic-Simulation
#   file Datenauswertung/read_data.py, line 9
#   licence (as GitHub reports it): LGPL-3.0   see ../licenses/
#   catalogue shelf: Public transport and city motion
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def muFitting(median):
    LIMIT = 0
    WEIGHT = 0.8
    maxima = []
    cleanmax = []
    valid = range(0,len(median))
    for i in valid:
        diff = 0
        diff2 = 0
        if i+1 in valid and i-1 in valid and median[i] > median[i-1] and median[i] > median[i+1]:
            if i+1 in valid and i+2 in valid:
                if median[i+1]-median[i+2] > 0 and median[i]-median[i+1] < WEIGHT*(median[i+1]-median[i+2]):
                    diff = (median[i+1]-median[i+2]) - (median[i]-median[i+1])
            if i-1 in valid and i-2 in valid:
                if median[i-1]-median[i-2] > 0 and median[i]-median[i-1] < WEIGHT*(median[i-1]-median[i-2]):
                    diff2 = (median[i-1]-median[i-2]) - (median[i]-median[i-1])
            if diff > diff2:
                maxima.append(i + 0.5)
            elif diff < diff2:
                maxima.append(i - 0.5)
            else:
                maxima.append(i)
            cleanmax.append(i)
    #print(maxima)
    if LIMIT <= 0:
        return maxima

    limited = []
    for i in range(0,LIMIT):
         currmax = 0
         currj = 0
         for j in range(0,len(cleanmax)):
             x = median[cleanmax[j]]
             if x > currmax:
                 currmax = x
                 currj = j
         limited.append(maxima[currj])
         cleanmax[currj] = 0
    #print(limited)
    return limited
