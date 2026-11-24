# powers_of_two
#
# Copied verbatim from https://github.com/mnky9800n/Python-course-materials-for-seismology-students
#   notebook example_notebooks/Introduction to Python.ipynb (its code cells joined in order; line 147 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def powers_of_two(n):
    """
    returns a list of powers of 2
    starting from 0 and progressing
    until n elements are generated.
    """
    results = []

    for i in range(n):
        results.append( 2**i )

    return results
