# adjust_point_units
#
# Copied verbatim from https://github.com/hvasbath/beat
#   file beat/utility.py, line 651
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

km = 1000.0

dimensiontypes = {
    "length",
    "width",
    "diameter",
    "a_half_axis",
    "b_half_axis",
    "a_half_axis_bottom",
    "b_half_axis_bottom",
}

locationtypes = {
    "east_shift",
    "north_shift",
    "depth",
    "distance",
    "delta_depth",
    "delta_east_shift_bottom",
    "delta_north_shift_bottom",
    "depth_bottom",
}

patch_anchor_points = {"center", "bottom_depth", "bottom_left"}

kmtypes = set.union(locationtypes, dimensiontypes, patch_anchor_points)

patypes = {"traction", "strike_traction", "dip_traction", "tensile_traction"}


def adjust_point_units(point):
    """
    Transform variables with [km] units to [m]

    Parameters
    ----------
    point : dict
        :func:`pymc.model.Point` of model parameter units as keys

    Returns
    -------
    mpoint : dict
        :func:`pymc.model.Point`
    """

    mpoint = {}
    for key, value in point.items():
        if key in kmtypes:
            mpoint[key] = value * km
        elif key in patypes:
            mpoint[key] = value * km * km
        else:
            mpoint[key] = value

    return mpoint
