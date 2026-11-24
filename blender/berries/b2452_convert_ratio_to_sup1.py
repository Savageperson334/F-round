# convert_ratio_to_sup1
#
# Copied verbatim from https://github.com/jlanversin/ONIX
#   file onix/nax/functions.py, line 1655
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def convert_ratio_to_sup1(ratio):

    indexes = []
    converted_ratio = ratio.copy()

    for i in range(len(ratio)):
        ratio_value = ratio[i]
        if ratio_value < 1:
            converted_ratio[i] = 1/ratio_value
        if i > 0:
            if ratio_value < 1 and ratio[i-1] >=1:
                indexes.append(i)
            elif ratio_value > 1 and ratio[i-1] <=1:
                indexes.append(i)


    return converted_ratio, indexes
