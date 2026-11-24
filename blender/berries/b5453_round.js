// round
//
// Copied verbatim from https://github.com/ndschonegg/CaveCAD
//   file tools/make_test_cave.js, line 135
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Cave surveys and subterranean maps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function round(v, places) {
    var f = Math.pow(10, places);
    return Math.round(v * f) / f;
}
