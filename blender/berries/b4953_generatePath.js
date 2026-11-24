// generatePath
//
// Copied verbatim from https://github.com/dc-js/dc.graph.js
//   file src/utils.js, line 104
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const bez_cmds = {
    1: 'L',
    2: 'Q',
    3: 'C',
};


function generatePath(pts, bezDegree, close) {
    const cats = ['M', pts[0].x, ',', pts[0].y];
    let remain = bezDegree;
    let _hasNaN = false;
    for (let i = 1; i < pts.length; ++i) {
        if (isNaN(pts[i].x) || isNaN(pts[i].y))
            _hasNaN = true;
        cats.push(remain === bezDegree ? bez_cmds[bezDegree] : ' ', pts[i].x, ',', pts[i].y);
        if (--remain === 0)
            remain = bezDegree;
    }
    if (remain != bezDegree)
        console.log("warning: pts.length didn't match bezian degree", pts, bezDegree);
    if (close)
        cats.push('Z');
    return cats.join('');
}
