# calculate_timings
#
# Copied verbatim from https://github.com/vr620/Adaptive_traffic_light_system
#   notebook main_varience_based.ipynb (its code cells joined in order; line 26 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Light pollution and night maps
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calculate_timings(vehicles , total_time):
    total_vehicle = 0
    for vehicle in vehicles:
        total_vehicle += vehicle
    a = vehicles[0]/total_vehicle
    b = vehicles[1]/total_vehicle
    c = vehicles[2]/total_vehicle
    d = vehicles[3]/total_vehicle


    t1 = round(total_time*a)
    t2 = round(total_time*b)
    t3 = round(total_time*c)
    t4 = round(total_time*d)


    return t1,t2,t3,t4
