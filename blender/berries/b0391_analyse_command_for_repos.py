# analyse_command_for_repos
#
# Copied verbatim from https://github.com/JonnyCarter/Delivery-Archaeology
#   file src/delivery_archaeology/inference.py, line 32
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def analyse_command_for_repos(projects: list[str], repos: list[str], days: int) -> str:
    lines = ["uv run delivery analyse \\"]
    lines.extend(f"  --jira-project {project} \\" for project in projects)
    lines.extend(f"  --repo {repo} \\" for repo in repos)
    lines.append(f"  --days {days}")
    return "\n".join(lines)
