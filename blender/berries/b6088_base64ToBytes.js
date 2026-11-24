// base64ToBytes
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file datacake/enLink_DataCake_API_Decoder_MULTI_DEVICE.js, line 913
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function base64ToBytes(base64) {

    var chars =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    var input = String(base64 || "")
        .replace(/\r/g, "")
        .replace(/\n/g, "")
        .replace(/\s/g, "");

    var bytes = [];

    for (var i = 0; i < input.length; i += 4) {

        var ch1 = input.charAt(i);
        var ch2 = input.charAt(i + 1);
        var ch3 = input.charAt(i + 2);
        var ch4 = input.charAt(i + 3);

        var e1 = chars.indexOf(ch1);
        var e2 = chars.indexOf(ch2);

        var e3 =
            (!ch3 || ch3 === "=")
            ? 64
            : chars.indexOf(ch3);

        var e4 =
            (!ch4 || ch4 === "=")
            ? 64
            : chars.indexOf(ch4);

        if (e1 < 0 || e2 < 0) {
            break;
        }

        bytes.push(
            ((e1 << 2) | (e2 >> 4)) & 0xFF
        );

        if (e3 !== 64 && e3 >= 0) {
            bytes.push(
                (((e2 & 15) << 4) | (e3 >> 2)) & 0xFF
            );
        }

        if (e4 !== 64 && e4 >= 0) {
            bytes.push(
                (((e3 & 3) << 6) | e4) & 0xFF
            );
        }
    }

    return bytes;
}
