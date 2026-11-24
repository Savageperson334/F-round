// between
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/shape.js, line 17
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const eps = 0.0000001;


function between(a, b, c) {
    return a-eps <= b && b <= c+eps;
}
