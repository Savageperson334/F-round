// U16
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file datacake/enLink - DataCake compact codec.js, line 120
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function U16(ival) {
    if (isNaN(ival) === false) {
        if (ival < 0)
            ival = ival + 65536;
    }
    return ival;
}
