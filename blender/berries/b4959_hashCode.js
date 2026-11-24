// hashCode
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file web/js/drag-drop-composition.js, line 480
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hashCode(s) {
    let hash = 0, i, chr;
    if (s.length === 0) return hash;
    for (i = 0; i < s.length; i++) {
        chr = s.charCodeAt(i);
        hash = ((hash<<5)-hash)+chr;
        hash |= 0; // Convert to 32bit integer
    }
    return hash>>>0; // convert to unsigned
}
