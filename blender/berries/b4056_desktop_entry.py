# desktop_entry
#
# Copied verbatim from https://github.com/ymatterlab/ycrystal
#   file src/ycrystal/desktop.py, line 141
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Molecular shapes and crystal lattices
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

PROJECT_MIME_TYPE = "application/x-ycrystal-project"


def desktop_entry(command: str) -> str:
    """Return the text of the ``.desktop`` launcher that runs ``command``.

    The command is quoted when it is a single path; files from the file manager are
    passed as ``%f``.
    """
    exec_line = f'"{command}"' if " -m " not in command else command
    return "\n".join(
        [
            "[Desktop Entry]",
            "Type=Application",
            "Version=1.5",
            "Name=Ycrystal",
            "GenericName=Crystal Structure Figures",
            "Comment=Prepare crystal-structure figures and render them with POV-Ray",
            f"Exec={exec_line} %f",
            "Icon=ycrystal",
            "Terminal=false",
            "Categories=Science;Physics;Chemistry;DataVisualization;",
            "Keywords=crystal;structure;POV-Ray;CIF;POSCAR;VASP;Quantum ESPRESSO;",
            f"MimeType={PROJECT_MIME_TYPE};",
            "StartupWMClass=ycrystal",
            "",
        ]
    )
