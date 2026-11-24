// asinh
//
// Copied verbatim from https://github.com/koansys/isat
//   file js/newtonnu.js, line 48
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function asinh(val) {
    return Math.log(val + Math.sqrt(val * val + 1));
}
