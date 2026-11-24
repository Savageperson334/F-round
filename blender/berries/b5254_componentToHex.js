// componentToHex
//
// Copied verbatim from https://github.com/lemmingapex/N-bodyGravitySimulation
//   file planets.js, line 505
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Physics and space without tidy answers
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function componentToHex(c) {
    var hex = c.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}
