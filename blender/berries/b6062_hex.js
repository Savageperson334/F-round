// hex
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file chirpstack/enLink - Chirpstack codec.js, line 411
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hex(data) {
    return ('0' + data.toString(16).toUpperCase()).slice(-2);
}
