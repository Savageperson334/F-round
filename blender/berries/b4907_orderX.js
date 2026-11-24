// orderX
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/constraint_pattern.js, line 179
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function orderX(gap, ordering) {
    return {
        type: 'ordering',
        axis: 'x',
        gap: 60,
        ordering,
    };
}
