# make_pages
#
# Copied verbatim from https://github.com/jesserobertson/earthchem-pyclient
#   file earthchem/pagination.py, line 10
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Geochemistry & materials
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

from itertools import count
from itertools import takewhile


def make_pages(max_items, items_per_page=50):
    """ Get a list of page bounds for submitting to the REST endpoint

        Parameters:
            max_items - the total number of items to get
            items_per_page - the size of each page (defaults to 50 which is 
                the Earthchem default)

        Returns:
            a list of tuples with (start_row, end_row) for each page
    """
    # Make a list of page bounds until we get bigger than the maximum number of items
    page_bounds = lambda n: (n * items_per_page, (n + 1) * items_per_page - 1)
    pages = list(takewhile(lambda x: x[0] < max_items, 
                           map(page_bounds, count())))

    # Replace last value with maximum row number
    pages[-1] = (pages[-1][0], max_items)
    return pages
