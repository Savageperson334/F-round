// pointOnEllipse
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/shape.js, line 5
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function pointOnEllipse(A, B, dx, dy) {
    let tansq = Math.tan(Math.atan2(dy, dx));
    tansq = tansq*tansq; // why is this not just dy*dy/dx*dx ? ?
    const ret = {x: A*B/Math.sqrt(B*B+A*A*tansq), y: A*B/Math.sqrt(A*A+B*B/tansq)};
    if (dx < 0)
        ret.x = -ret.x;
    if (dy < 0)
        ret.y = -ret.y;
    return ret;
}
