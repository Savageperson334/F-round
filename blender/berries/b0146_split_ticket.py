# split_ticket
#
# Copied verbatim from https://github.com/Dalageo/ml-titanic-shipwreck
#   notebook Exploring the World's Most Renowned Shipwreck 🚢.ipynb (its code cells joined in order; line 811 of those)
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Shipwrecks and maritime ghosts
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def split_ticket(ticket):
    parts = ticket.split()
    if len(parts) > 1:
        # Return the first part as the identifier and the last part as the ticket number
        return parts[0], parts[-1]
    else:
        # If there's only one part, return 'NaN' for the identifier
        return 'NaN', parts[0]
