// parseDump
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 50
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


function parseDump(a, pcount, gcount) {      // engine, preset, P_COUNT x v14, G_COUNT x v14 (selected track and globals)
  const p = [], g = [];
  for (let i = 0; i < pcount; i++) p.push(rv14(a, 2 + 2 * i));
  for (let i = 0; i < gcount; i++) g.push(rv14(a, 2 + 2 * pcount + 2 * i));
  return { eng: a[0], preset: a[1], p, g };
}
