# normalize_bitmask
#
# Copied verbatim from https://github.com/syxscott/PaleoAST
#   file phylogenetics/tree_distance.py, line 212
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Fossil measurements and paleontology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def normalize_bitmask(bitmask: int, all_taxa_bitmask: int) -> int:
    """
    Return the canonical side of a split: the one *without* the first taxon.

    DendroPy's lsb0 convention -- the bit of the lowest-indexed taxon is forced
    to 0 by complementing within ``all_taxa_bitmask`` -- so that the same
    unrooted bipartition gets the same integer no matter how the tree is
    rotated or where it is rooted.

    Parameters:
        bitmask: Split (or leafset) to normalize.
        all_taxa_bitmask: Union of all taxon bits of the reference tree.

    Returns:
        Normalized bitmask; bits outside ``all_taxa_bitmask`` are dropped.
    """
    masked = bitmask & all_taxa_bitmask
    lowest = all_taxa_bitmask & -all_taxa_bitmask
    if lowest and masked & lowest:
        return masked ^ all_taxa_bitmask
    return masked
