# calculate_timings
#
# Copied verbatim from https://github.com/vr620/Adaptive_traffic_light_system
#   notebook final_complete_code.ipynb (its code cells joined in order; line 173 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calculate_timings(vehicle_count , Maximum_time):
    # time of green signal = t
    y = 3 * vehicle_count
    if vehicle_count < 5:
        t = 10
    else:
        if y > Maximum_time:
            t= Maximum_time
        else:
            t = y
    return t
