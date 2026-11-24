# dim_conversion_y
#
# Copied verbatim from https://github.com/Jormono1/Lego-Pen-Plotter
#   file PC_scripts/ZZZ_Image_Drawing/Plotter_Pybricks_Generator.py, line 43
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

Y_Max = 3450


def dim_conversion_y (length):        # dim must be in mm
    ### conversion factor is established from distance drawn as measured with a ruler and the corresponding traveled angle ###
    ### in this case I know the total range of travel in X and Y, and I know how long ###
    ### the drawn line was which corresponds to the max angle ###
    max_length = 144.4625       # X max line measurement converted from inches to mm
    conversion_factor = Y_Max / max_length  # degrees/mm
    out = length * conversion_factor
    if out > Y_Max:
        print("coordinate value out of range, data will be missing from output file")
        return False
    else:
        return out
