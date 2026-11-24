// readU16
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file datacake/enLink - DataCake compact codec.js, line 172
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


function u16_1(bytes, index) {
    return U16((bytes[index + 1] << 8) | (bytes[index + 2]));
}


function readU16(data, i) { return u16_1(data, i); }
