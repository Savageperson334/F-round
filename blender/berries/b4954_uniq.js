// uniq
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/utils.js, line 137
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function uniq(a) {
    const ret = [];
    a.forEach((x, i) => {
        if (i === 0 || x !== a[i-1])
            ret.push(x);
    });
    return ret;
}
