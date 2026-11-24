// print_value
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file web/js/drag-drop-composition.js, line 275
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function print_value(v) {
    if (!v || ['string', 'number', 'boolean'].indexOf(typeof v) !== -1)
        return v.toString();
    else
        return JSON.stringify(v);
}
