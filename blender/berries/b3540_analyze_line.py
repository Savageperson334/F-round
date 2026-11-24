# analyze_line
#
# Copied verbatim from https://github.com/rlseaman/neolyzer
#   file scripts/diagnostics/diagnose_missing.py, line 20
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Astronomical observation tools
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def analyze_line(line):
    """Analyze why a line might fail to parse"""
    issues = []

    stripped = line.rstrip('\n\r')
    if len(stripped) < 160:
        issues.append(f"Line too short: {len(stripped)} chars (need >= 160)")
        return issues

    try:
        H = line[8:13].strip()
        if not H:
            issues.append("Missing H magnitude (blank)")
        elif H:
            float(H)
    except ValueError:
        issues.append(f"Invalid H magnitude: '{line[8:13]}'")

    try:
        G = line[14:19].strip()
        if G:
            float(G)
    except ValueError:
        issues.append(f"Invalid G slope: '{line[14:19]}'")

    try:
        epoch = line[20:25].strip()
        if not epoch or len(epoch) < 5:
            issues.append(f"Invalid epoch: '{epoch}'")
    except:
        issues.append("Can't read epoch")

    for name, start, end in [
        # Offsets must match the canonical parser in src/mpc_loader.py
        # (parse_mpcorb_line) — do not edit independently
        ('mean anomaly', 26, 35),
        ('arg_peri', 37, 46),
        ('node', 48, 57),
        ('inclination', 59, 68),
        ('eccentricity', 70, 79),
        ('semi-major axis', 92, 103),
    ]:
        try:
            val = line[start:end].strip()
            if val:
                float(val)
        except ValueError:
            issues.append(f"Invalid {name}: '{line[start:end]}'")

    return issues
