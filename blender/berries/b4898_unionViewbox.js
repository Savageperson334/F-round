// unionViewbox
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/arrows.js, line 516
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function unionViewbox(vb1, vb2) {
    const left = Math.min(vb1[0], vb2[0]),
        bottom = Math.min(vb1[1], vb2[1]),
        right = Math.max(vb1[0]+vb1[2], vb2[0]+vb2[2]),
        top = Math.max(vb1[1]+vb1[3], vb2[1]+vb2[3]);
    return [left, bottom, right-left, top-bottom];
}
