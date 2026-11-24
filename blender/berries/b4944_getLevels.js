// getLevels
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/shape.js, line 616
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function interpolate(d, p) {
    const r = [];
    for (let i = 1; i < d.length; i++) {
        const d0 = d[i-1], d1 = d[i];
        r.push({x: d0.x+(d1.x-d0.x)*p, y: d0.y+(d1.y-d0.y)*p});
    }
    return r;
}


function getLevels(points, t_) {
    const x = [points];
    for (let i = 1; i < points.length; i++) {
        x.push(interpolate(x[x.length-1], t_));
    }
    return x;
}
