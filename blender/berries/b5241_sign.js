// sign
//
// Copied verbatim from https://github.com/koansys/isat
//   file js/isat.js, line 1145
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sign(val) {
    'use strict';
    if (val < 0) {
        return -1;
    }
    if (val > 0) {
        return 1;
    }
    return 0;
}
