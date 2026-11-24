# pr_list_args
#
# Copied verbatim from https://github.com/JonnyCarter/Delivery-Archaeology
#   file src/delivery_archaeology/github.py, line 187
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

PR_LIST_FIELDS = [
    "number",
    "url",
    "title",
    "author",
    "createdAt",
    "updatedAt",
    "closedAt",
    "mergedAt",
    "state",
    "reviewDecision",
    "headRefName",
    "baseRefName",
    "labels",
]


def pr_list_args(repo: str, since: str) -> list[str]:
    return [
        "pr",
        "list",
        "--repo",
        repo,
        "--state",
        "all",
        "--limit",
        "1000",
        "--search",
        f"updated:>={since}",
        "--json",
        ",".join(PR_LIST_FIELDS),
    ]
