// bytesToHex
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file chirpstack/enLink - Chirpstack codec.js, line 393
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function bytesToHex(bytes) {
    let result = "";
    for (let i = 0; i < bytes.length; i += 1) {
        result += ('0' + (bytes[i]).toString(16).toUpperCase() + ' ').slice(-3);
    }
    return result.trim();
}
