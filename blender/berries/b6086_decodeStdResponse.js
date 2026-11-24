// decodeStdResponse
//
// Copied verbatim from https://github.com/synetica/enlink-decoder
//   file datacake/enLink - DataCake compact codec.js, line 769
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

var ENLINK_HEADER = 0xA5;

var ENLINK_ACK = 0x06;

var ENLINK_NACK = 0x15;

var ENLINK_SEND_SYS_INFO = 0x00;

var stdResponseCommandByType = {};


function bytesToHex(bytes) {
    var result = "";
    for (var i = 0; i < bytes.length; i += 1) {
        result += ('0' + (bytes[i]).toString(16).toUpperCase() + ' ').slice(-3);
    }
    return result.trim();
}


function decodeStdResponse(data) {
    var obj = {};
    if (data[0] != ENLINK_HEADER) {
        obj.reply = "Error: First byte is not 0xA5. Data: " + bytesToHex(data);
        return obj;
    }
    // Parse reply from device following a downlink command
    if (data[1] == ENLINK_ACK) {
        obj.reply = "ACK";
    } else if (data[1] == ENLINK_NACK) {
        obj.reply = "NACK";
    } else {
        obj.reply = "Error: Reply ACK/NACK failure. Data: " + bytesToHex(data);
        return obj;
    }

    if (data[2] == ENLINK_SEND_SYS_INFO) {
        // Only the ACK carries the version. A NACK with 0x00 is the reply to an unknown command
        if (data[1] == ENLINK_ACK && data.length >= 5) {
            obj.command = "Device Firmware Version: " + data[3] + "." + data[4];
        } else {
            obj.command = "Unknown command";
        }
    } else {
        var commandDescription = stdResponseCommandByType[data[2]];
        if (commandDescription) {
            obj.command = commandDescription;
        } else {
            obj.reply = "Unexpected Command byte. Data: " + bytesToHex(data);
        }
    }
    return obj;
}
