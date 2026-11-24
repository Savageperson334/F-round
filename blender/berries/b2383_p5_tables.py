# p5_tables
#
# Copied verbatim from https://github.com/jbschooley/Virtual-FM-1
#   file engines/choralroot/upstream/tools/gen_tables.py, line 112
#   licence (as GitHub reports it): GPL-3.0   see ../licenses/
#   catalogue shelf: Small synthesizers and circuits
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import math

CTL = 32

FS = 44100


def arr(name, ctype, vals, per=12, ram=False):
    """a table in flash (XIP, through the cache); ram: in RAM (.data), for lookups every sample; ram a string: that
    macro decides (P5_TABLE: const, or TABLE_RAM in a build with CR_RAM_TABLES_P5)"""
    out = [f"static {ram + ' ' if isinstance(ram, str) else 'TABLE_RAM ' if ram else 'const '}{ctype} {name}[{len(vals)}] = {{"]
    for i in range(0, len(vals), per):
        out.append("    " + ", ".join(str(v) for v in vals[i:i + per]) + ",")
    out.append("};")
    return out


def p5_tables(fc):
    """PROPHET (eng_prophet_test.c, FELUCCA_PROPHET; docs/PROPHET.md): Melodee's tables for its Prophet-5 engine, as its
    tools/gen_tables.py makes them at commit 8a3074b (the last integer version; Modifications Copyright (C) 2026 Kerem
    Kilic (Ellic Studio), GPL-3.0-only): the same expressions, the same values (compared once with the tables of
    the remix that brought the engine here, docs/PROPHET.md "Where it comes from"). ChoralRoot's differences: only the 1x sample rate's coefficient table (Melodee also had P5_OVERSAMPLE 2's),
    and every table const, in flash as SINE is: Melodee put P5_EXP2_Q14, P5_TPT_G, P5_INV_DEN and P5_TANH_Q15 into a
    RAM section (.dsp_tables, 5.4 KB); here RAM is the tight region and the unit showed no gain from RAM for the
    effects' loops (docs/FX.md CR_FX_RAM). The four are P5_TABLE: const, and RAM in a device build with
    CR_RAM_TABLES_P5=1 (3y41: the unit did gain from RAM for this engine's code; the tables are measured apart). A build
    without the engine drops them (static const, unused)."""
    L = []
    L += [f"#define P5_KEYTRACK_HALF_Q7 {round(128 * 256 * 127 * math.log(2) / (2 * 192 * math.log(fc[-1] / fc[0])))}"]
    # LFO rate, raw 0..127. Measured on a Rev-4 factory demo (rates 74..97 -> 2.4..8.4 Hz,
    # within 2 %): ln Hz = -3.1005 + 0.05387 raw, bent at the ends to the documented .022 / 500 Hz.
    def p5_lfo_hz(v):
        x = -3.1005 + 0.05387 * v
        if v > 100:
            x += (math.log(500) - (-3.1005 + 0.05387 * 127)) * ((v - 100) / 27) ** 2
        if v < 20:
            x -= (-3.1005 - math.log(.022)) * ((20 - v) / 20) ** 2
        return math.exp(x)
    L += arr("P5_LFO_INC", "uint32_t", [int(p5_lfo_hz(v) / FS * 2**32) for v in range(128)], 8)
    # LFO amount response (initial + wheel + pressure), Q15. Rev-4 vibrato depth measured at
    # 18..55 fits 0.0519 * raw^1.737 cents; the full scale (235 cents) lives in the engine.
    L += arr("P5_AMOUNT_Q15", "uint16_t", [round(32767 * (v / 127) ** 1.737) for v in range(128)])
    # Envelopes, raw 0..127: t = 1 ms .. 10 s. Attack is a linear ramp of t; decay and release
    # are exponential with time constant t (Rev-4 decays were ~4.6x longer than a 99 % point);
    # the Rev 1/2 (SSM) filter envelope decays linearly, full scale in 3.6 t (fitted to "It's a Prophet 5").
    p5ms = [10000 ** (v / 127) for v in range(128)]
    L += arr("P5_ENV_ATK", "uint32_t", [max(1, int((1 << 24) * CTL / (m * FS / 1000))) for m in p5ms], 8)
    L += arr("P5_ENV_EXP", "uint16_t", [max(1, min(65535, int(65536 * (1 - math.exp(-CTL / (m / 1000 * FS))))))
                                        for m in p5ms])
    L += arr("P5_ENV_SSM", "uint32_t", [max(1, int((1 << 24) * CTL / (3.6 * m * FS / 1000))) for m in p5ms], 8)
    # 2^(i/256), Q14: exponential pitch (wheel and Poly-Mod) at audio rate
    L += arr("P5_EXP2_Q14", "uint16_t", [round(16384 * 2 ** (i / 256)) for i in range(257)], ram="P5_TABLE")
    # Four TPT poles at the sample rate (Melodee's P5_OVERSAMPLE 1 table).
    L += arr("P5_TPT_G", "uint16_t", [round(4096 * math.tan(math.pi * f / FS) / (1 + math.tan(math.pi * f / FS)))
                                      for f in fc], ram="P5_TABLE")
    L += arr("P5_INV_DEN", "uint16_t", [round((8192 * 4096) / (4096 + i * 32)) for i in range(257)], ram="P5_TABLE")
    # Nearest 32-unit lookup: <17 Q15 units of error, with the same tanh knee.
    # Distributed SSI saturation invokes this seven times per audio sample.
    L += arr("P5_TANH_Q15", "int16_t", [int(32767 * math.tanh(i / 2048 * 2)) for i in range(2049)], ram="P5_TABLE")
    return L
