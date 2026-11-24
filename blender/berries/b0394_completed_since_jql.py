# completed_since_jql
#
# Copied verbatim from https://github.com/JonnyCarter/Delivery-Archaeology
#   file src/delivery_archaeology/jira.py, line 192
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def _quote_project_key(project: str) -> str:
    escaped = project.replace('"', '\\"')
    return f'"{escaped}"'


def completed_since_jql(projects: list[str], days: int) -> str:
    project_clause = ", ".join(_quote_project_key(project) for project in projects)
    return f'project in ({project_clause}) AND statusCategory = Done AND updated >= startOfDay("-{days}d") ORDER BY updated ASC'
