# dim_conversion_x
#
# Copied verbatim from https://github.com/Jormono1/Lego-Pen-Plotter
#   file PC_scripts/ZZZ_Image_Drawing/Plotter_Pybricks_Generator.py, line 30
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Plotters & drawing machines
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

X_Max = 2304


def dim_conversion_x (length):        # dim must be in mm
    ### conversion factor is established from distance drawn as measured with a ruler and the corresponding traveled angle ###
    ### in this case I know the total range of travel in X and Y, and I know how long ###
    ### the drawn line was which corresponds to the max angle ###
    max_length = 144.4625       # X max line measurement converted from inches to mm
    conversion_factor = X_Max / max_length  # degrees/mm
    out = length * conversion_factor
    if out > X_Max:
        print("coordinate value out of range, data will be missing from output file")
        return False
    else:
        return out
