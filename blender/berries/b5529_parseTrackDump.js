// parseTrackDump
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 46
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


function parseTrackDump(a, pcount) {         // track, engine, preset, P_COUNT x v14
  const p = []; for (let i = 0; i < pcount; i++) p.push(rv14(a, 3 + 2 * i));
  return { track: a[0], eng: a[1], preset: a[2], p };
}
