// t_fix_v7
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file chirpstack/archive/enLink Zone codec.js, line 172
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function t_fix_v7(t) {
    var num = t & 0xFFFF;
    if (0x8000 & num)
        num = 655 + num;
    return num & 0xFFFF;
}
