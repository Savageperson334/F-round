// normaliseSerial
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file datacake/enLink_DataCake_API_Decoder_MULTI_DEVICE.js, line 1002
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function normaliseSerial(value) {
    return String(value || "")
        .replace(/[^0-9a-zA-Z]/g, "")
        .toLowerCase();
}
