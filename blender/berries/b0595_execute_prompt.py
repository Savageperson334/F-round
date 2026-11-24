# execute_prompt
#
# Copied verbatim from https://github.com/NDilanka/orrery
#   file engine/orrery_loop/prompts.py, line 32
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


def execute_prompt(
    criteria: list[str],
    task: str,
    gate_hint: str = "the gate command",
    progress_rel: str = ".loop/progress.md",
    recall: str = "",
) -> str:
    """Assemble the stable execute prompt (port of ``$prompt``, loop.ps1 ~600-617).

    STABLE-PREFIX-FIRST: stable system instructions, then the task spec name, then the frozen
    contract — all byte-identical across iterations (cache-eligible). ``gate_hint`` names the
    gate command the worker should run (the generic analogue of the PowerShell ``bun test``).

    ``recall`` is an OPTIONAL cross-run lessons block (:mod:`orrery_loop.memory`); when non-empty it is
    inserted into the STABLE prefix AFTER the frozen contract and BEFORE the procedure, so it
    stays cache-friendly (it changes only between runs, not between iterations). When empty
    (the default / NullMemoryStore) the prompt is byte-identical to before.
    """
    block = contract_block(criteria, task, progress_rel)
    recall_section = f"\n\n{recall.strip()}" if recall and recall.strip() else ""
    return f"""You are an autonomous fix-until-green worker. Follow these stable instructions
every turn; they do not change between iterations.

{block}{recall_section}

PROCEDURE:
Read {task} and {progress_rel} first.

Then run {gate_hint}, read the FIRST failing assertion, and make the SMALLEST
change to the implementation file named in {task} that fixes it. Never edit,
skip, or delete any locked test file, and do not break a test that already passes.
Re-run {gate_hint} to confirm no regression. Finally update {progress_rel}
with what you changed, what still fails, and the next step. If you are stuck,
write `BLOCKED: <reason>` on the first line of {progress_rel} and stop.
If you need a human/orchestrator decision to proceed, write
`QUESTION: <your one question>` on the first line of {progress_rel} and stop."""
