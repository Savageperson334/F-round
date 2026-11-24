# build_js_runtimes
#
# Copied verbatim from https://github.com/phoxwupsh/turto
#   file src/ytdl/sidecar.py, line 69
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Mechanical music boxes and organs
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def build_js_runtimes(bun_arg: str) -> dict[str, dict[str, str | None]]:
    """Mirror the CLI default (``deno``) plus turto's configured bun runtime.

    The CLI flag ``--js-runtimes bun:<path>`` resolves to the YoutubeDL param
    ``{'deno': {'path': None}, 'bun': {'path': '<path>'}}``.
    """
    runtimes = {"deno": {"path": None}}
    if bun_arg:
        name, _, path = bun_arg.partition(":")
        runtimes[name.lower()] = {"path": path or None}
    return runtimes
