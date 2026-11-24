# bond_relation_id
#
# Copied verbatim from https://github.com/Christanding/CrystalSketch
#   file src/crystalsketch/structures/connectivity.py, line 402
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def bond_relation_id(
    start_site_id: str,
    end_site_id: str,
    relative_offset: tuple[int, int, int],
) -> str:
    return (
        f"bond-relation:{start_site_id}--{end_site_id}@"
        f"{relative_offset[0]},{relative_offset[1]},{relative_offset[2]}"
    )
