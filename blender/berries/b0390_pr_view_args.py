# pr_view_args
#
# Copied verbatim from https://github.com/JonnyCarter/Delivery-Archaeology
#   file src/delivery_archaeology/github.py, line 204
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def pr_view_args(repo: str, number: int, fields: list[str]) -> list[str]:
    return [
        "pr",
        "view",
        str(number),
        "--repo",
        repo,
        "--json",
        ",".join(fields),
    ]
