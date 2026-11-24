// GetCrnMetal
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file datacake/enLink - DataCake compact codec.js, line 454
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function GetCrnMetal(id_byte) {
    var id = (id_byte & 0x7F);
    var metalNames = ["Unknown", "Copper", "Silver", "Chromium"];
    return metalNames[id] || "Error";
}
