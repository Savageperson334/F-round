# scenario_family
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file archaeology/scenarios.py, line 76
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

VARIANT_MARK = "~"


def scenario_family(name: str) -> str:
    """The template a scenario trace belongs to: ``late-return~refine1`` is a variant of ``late-return``.

    Refine adds variants of a template under a suffixed name so the original is untouched. Analysis
    groups a variant with its template, so the values it adds count toward the template's sweeps.
    """
    return name.split(VARIANT_MARK, 1)[0]
