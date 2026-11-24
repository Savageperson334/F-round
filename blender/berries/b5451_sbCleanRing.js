// sbCleanRing
//
// Copied verbatim from https://github.com/ndschonegg/CaveCAD
//   file scripts/CaveSurvey/ScatterBreakdown/ScatterBreakdown.js, line 61
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Cave surveys and subterranean maps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sbCleanRing(verts) {
    if (verts.length > 1) {
        var first = verts[0], last = verts[verts.length - 1];
        var dx = first.x - last.x, dy = first.y - last.y;
        if (Math.sqrt(dx * dx + dy * dy) < 1e-6) {
            return verts.slice(0, verts.length - 1);
        }
    }
    return verts;
}
