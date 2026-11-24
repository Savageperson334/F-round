# integer_fac_to_seed
#
# Copied verbatim from https://github.com/c64cryptoboy/retro-archaeology-skills
#   file skills/c64-basic-v2-rnd-analysis/analysis/analyze_ti_seed_prefixes.py, line 40
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Archaeology & digital heritage
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------


def reverse_bytes32(value: int) -> int:
    return int.from_bytes(value.to_bytes(4, "big")[::-1], "big")


def integer_fac_to_seed(value: int) -> tuple[int, int]:
    """Return positive packed-seed exponent and unpacked mantissa for RND(-value)."""
    if value <= 0:
        raise ValueError("integer seed must be positive")
    top_bit = value.bit_length() - 1
    exponent = 0x81 + top_bit
    mantissa = value << (31 - top_bit)

    reversed_mantissa = reverse_bytes32(mantissa)
    shifts = 32 - reversed_mantissa.bit_length()
    wide = ((reversed_mantissa << 8) | exponent) << shifts
    output_mantissa = (wide >> 8) + (1 if wide & 0x80 else 0)
    output_exponent = 0x80 - shifts
    if output_mantissa == 1 << 32:
        output_mantissa = 0x80000000
        output_exponent += 1
    return output_exponent, output_mantissa
