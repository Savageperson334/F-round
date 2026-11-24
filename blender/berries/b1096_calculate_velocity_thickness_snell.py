# calculate_velocity_thickness_snell
#
# Copied verbatim from https://github.com/aradfarahani/Seismology
#   notebook AUT/Dr. Mahdavi/ES Project 2_13-8-1403.ipynb (its code cells joined in order; line 32 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Earthquakes and seismic tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def calculate_velocity_thickness_snell(travel_times, dx):
    velocities = []
    thicknesses = []
    for i in range(len(travel_times) - 1):
        dt = travel_times[i+1] - travel_times[i]
        velocity = dx / dt
        thickness = (travel_times[i+1] + travel_times[i]) / 2 * velocity
        velocities.append(velocity)
        thicknesses.append(thickness)
    return velocities, thicknesses
