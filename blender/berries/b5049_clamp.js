// clamp
//
// Copied verbatim from https://github.com/frepet/Robot-Arm-Controller
//   file src/model.js, line 1
//   licence (as GitHub reports it): Unlicense   see ../licenses/
//   catalogue shelf: Robots and tactile mechanisms
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function clamp(val, min, max) {
    return Math.min(Math.max(val, min), max);
}
