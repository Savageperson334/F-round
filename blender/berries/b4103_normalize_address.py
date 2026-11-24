# normalize_address
#
# Copied verbatim from https://github.com/yukiyuqichen/His-Geo
#   file his_geo/utils/normalization/normalization_ch_modern.py, line 25
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Historic cartography
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

minority_list = []

minority_postfix_list = []

postfix_list = ["特别行政区", "辖区", "地区", "自治区", "自治县", "自治州", "省", "市", "区", "县", "盟", "委员会"]


def normalize_address(str, structure_sign):
    if "自治" in str:
        # Special Cases
        if "内蒙古自治区" in str:
            str = str.replace("内蒙古自治区", "内蒙古")
        if "东乡族自治县" in str:
            str = str.replace("东乡族自治县", "东乡")
        if "龙胜各族自治县" in str:
            str = str.replace("龙胜各族自治县", "龙胜")
        if "河南蒙古族自治县" in str:
            str = str.replace("河南蒙古族自治县", "河南县")
        for postfix in minority_postfix_list:
            if postfix in str:
                str = str.replace(postfix, "")
        for minority in minority_list:
            if minority in str:
                str = str.replace(minority, "")
    if str == "市辖区":
        str == "市辖区"
    else:
        temp_signs = {"河南县":"[temp1]", "河北区":"[temp2]", "津市市":"[temp3]", 
                      "西市区":"[temp4]", "北市区":"[temp5]", "南市区":"[temp6]",
                      "新市区":"[temp7]", "东区":"[temp8]", "西区":"[temp9]",
                      "市区":"[temp10]"}
        for temp in temp_signs.keys():
            if temp in str: 
                str = str.replace(temp, temp_signs[temp])
        for postfix in postfix_list:
            # if postfix in str and len(str) <= 2:
            #     str = str.replace(postfix, postfix + structure_sign)
            # else:
            #     str = str.replace(postfix, structure_sign)
            str = str.replace(postfix, structure_sign)
        for temp in temp_signs.keys():
            if temp_signs[temp] in str:
                str = str.replace(temp_signs[temp], temp)


    str = re.sub("（.*）", "", str)
    return str
