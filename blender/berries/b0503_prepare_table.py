# prepare_table
#
# Copied verbatim from https://github.com/MartinThoma/hwrt
#   file hwrt/partitions.py, line 16
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Handwriting and historical text
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def prepare_table(table):
    """
    Make the table 'symmetric'.

    The lower left part of the matrix is the reverse probability.
    """
    n = len(table)
    for i, row in enumerate(table):
        assert len(row) == n, f"len(row) = {len(row)} != {n} = n"
        for j, _ in enumerate(row):
            if i == j:
                table[i][i] = 0.0
            elif i > j:
                table[i][j] = 1 - table[j][i]
    return table
