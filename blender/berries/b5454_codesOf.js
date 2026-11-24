// codesOf
//
// Copied verbatim from https://github.com/ndschonegg/CaveCAD
//   file tools/make_test_cave.js, line 960
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Cave surveys and subterranean maps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function codesOf(findings) {
    var out = {};
    for (var i = 0; i < findings.length; i++) {
        out[findings[i].code] = (out[findings[i].code] || 0) + 1;
    }
    return out;
}
