// nodeObject
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/generate.js, line 13
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function nodeName(i) {
    // a-z, A-Z, aa-Zz, then quit
    if (i < 26)
        return String.fromCharCode(97+i);
    else if (i < 52)
        return String.fromCharCode(65+i-26);
    else if (i < 52*52)
        return nodeName(Math.floor(i/52))+nodeName(i%52);
    else throw new Error("no, that's too large");
}


function nodeObject(i, attrs) {
    attrs = attrs || {};
    return {
        id: i,
        name: nodeName(i),
        ...attrs,
    };
}
