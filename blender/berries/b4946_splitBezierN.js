// splitBezierN
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/shape.js, line 659
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function splitBezier(p, t) {
    const x1 = p[0].x,
        y1 = p[0].y,
        x2 = p[1].x,
        y2 = p[1].y,
        x3 = p[2].x,
        y3 = p[2].y,
        x4 = p[3].x,
        y4 = p[3].y,
        x12 = (x2-x1)*t+x1,
        y12 = (y2-y1)*t+y1,
        x23 = (x3-x2)*t+x2,
        y23 = (y3-y2)*t+y2,
        x34 = (x4-x3)*t+x3,
        y34 = (y4-y3)*t+y3,
        x123 = (x23-x12)*t+x12,
        y123 = (y23-y12)*t+y12,
        x234 = (x34-x23)*t+x23,
        y234 = (y34-y23)*t+y23,
        x1234 = (x234-x123)*t+x123,
        y1234 = (y234-y123)*t+y123;

    return [
        [{x: x1, y: y1}, {x: x12, y: y12}, {x: x123, y: y123}, {x: x1234, y: y1234}],
        [{x: x1234, y: y1234}, {x: x234, y: y234}, {x: x34, y: y34}, {x: x4, y: y4}],
    ];
}


function splitBezierN(p, n) {
    const ret = [];
    while (n > 1) {
        const parts = splitBezier(p, 1/n);
        ret.push(parts[0][0], parts[0][1], parts[0][2]);
        p = parts[1];
        --n;
    }
    ret.push.apply(ret, p);
    return ret;
}
