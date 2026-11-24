# paleoisochron_age_list
#
# Copied verbatim from https://github.com/Augtumn/IsoLeadToolkit
#   file core/overlay_state.py, line 213
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def paleoisochron_age_list(min_age: int, max_age: int, step: int) -> list[int]:
    """The ages the three controls describe, oldest first down to the youngest.

    The ages are derived from min/max/step, and the derivation lives here alone: the overlay container, the panel's
    controls and the dispatch layer all need it, and the panel used to compute its own copy - which is how changing
    min/max could leave the ages describing the old range.
    """
    minimum, maximum, stride = int(min_age), int(max_age), int(step)
    if stride <= 0:
        return []
    if maximum < minimum:
        minimum, maximum = maximum, minimum
    ages = list(range(maximum, minimum - 1, -stride))
    if not ages or ages[-1] != minimum:
        # Land on the youngest age even when the step does not divide the range.
        ages.append(minimum)
    return ages
