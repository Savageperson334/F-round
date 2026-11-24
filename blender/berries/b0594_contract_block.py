# contract_block
#
# Copied verbatim from https://github.com/NDilanka/orrery
#   file engine/orrery_loop/prompts.py, line 14
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical clocks and orreries
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def contract_block(criteria: list[str], task: str, progress_rel: str = ".loop/progress.md") -> str:
    """The FROZEN acceptance-criteria block (port of ``$ContractBlock``, loop.ps1 ~594-599).

    When criteria were parsed, render them as a bullet list under a do-not-weaken header;
    otherwise point the worker at the task file's own AC section.
    """
    if criteria:
        bullets = "\n".join(f"- {c}" for c in criteria)
        return (
            "FROZEN ACCEPTANCE CRITERIA (do not weaken; the work is done only when ALL hold):\n"
            + bullets
        )
    return (
        "FROZEN ACCEPTANCE CRITERIA: see the '## Acceptance Criteria' / "
        f"'## Definition of done' section of {task}."
    )
