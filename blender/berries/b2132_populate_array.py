# populate_array
#
# Copied verbatim from https://github.com/guaix-ucm/megara-tools
#   file megaratools/atan_model.py, line 18
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def populate_array(rows, columns):
    array_dic = {}
    for row in range(0, rows):
        array_dic[row] = []
        for col in range(0, columns):
            array_dic[row].append("None")  # initialize to 'None'
    return array_dic
