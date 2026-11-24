# path_template
#
# Copied verbatim from https://github.com/AkshayTallikar/software-archaeology
#   file archaeology/infer/catalog.py, line 46
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re

_DIGITS = re.compile(r"[0-9]+")

_HAS_DIGIT = re.compile(r"[0-9]")

_OPAQUE_ID = re.compile(r"(?:[A-Za-z]{1,4}[-_])?[0-9a-fA-F]{6,}")

_PREFIXED = re.compile(r"[A-Za-z]{1,4}[-_][0-9a-fA-F]{6,}")

_SEPARATED_DIGITS = re.compile(r"[0-9]+(?:-[0-9]+)*-(?:[0-9]+|[Xx])")

_UUID = re.compile(r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}")


def _is_opaque_id(segment: str) -> bool:
    """True for a segment that looks generated or catalogue-like.

    That is a UUID, a digit-bearing hex token, or a hyphen-separated run of at
    least six digits (an ISBN written as ``978-0-00-000001-9``).
    """
    if _UUID.fullmatch(segment):
        return True
    if _SEPARATED_DIGITS.fullmatch(segment) and sum(c.isdigit() for c in segment) >= 6:
        return True
    if _OPAQUE_ID.fullmatch(segment) is None:
        return False
    # A bare hex word (deadbeef, facade) is literal unless it has a digit; a
    # prefixed token (L-acdffe, m_beadfeed) is generated either way.
    return _HAS_DIGIT.search(segment) is not None or _PREFIXED.fullmatch(segment) is not None


def path_template(path: str) -> str:
    """Replace every all-digit or opaque identifier path segment with ``{id}``."""
    return "/".join(
        "{id}" if _DIGITS.fullmatch(seg) or _is_opaque_id(seg) else seg
        for seg in path.split("/")
    )
