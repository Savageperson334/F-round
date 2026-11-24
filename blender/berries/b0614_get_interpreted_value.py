# get_interpreted_value
#
# Copied verbatim from https://github.com/POPCORNBOOM/EZHolodotNet
#   file Core/main.py, line 92
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Optical computing and holograms
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def get_interpreted_value(point, value_mat):
    relative_block = (int(point[0]), int(point[1]))
    inside_pos = (point[0] - relative_block[0], point[1] - relative_block[1])
    part_y = (inside_pos[1] - 0.5)
    part_x = (inside_pos[0] - 0.5)
    partial_y = abs(part_y)
    partial_x = abs(part_x)
    block_x = max(0, min(relative_block[0] + (1 if part_x > 0 else -1), len(value_mat[0]) - 1))
    block_y = max(0, min(relative_block[1] + (1 if part_y > 0 else -1), len(value_mat) - 1))
    print(f"Point: {point}, Relative Block: {relative_block}, Inside Pos: {inside_pos}, Partial X: {partial_x}, Partial Y: {partial_y}, Block X: {block_x}, Block Y: {block_y}")
    interpreted_value = (
        value_mat[relative_block[1]][relative_block[0]] * (1 - partial_x) * (1 - partial_y)
        + value_mat[relative_block[1]][block_x] * partial_x * (1 - partial_y)
        + value_mat[block_y][relative_block[0]] * (1 - partial_x) * partial_y
        + value_mat[block_y][block_x] * partial_x * partial_y
    )
    return interpreted_value
