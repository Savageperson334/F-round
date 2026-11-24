// parseXReply
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 112
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rv14 = (a, o = 0) => ((a[o] | a[o + 1] << 7) - 8192);


const parseXReply = (a) => ({ part: a[0], k: a[1], v: rv14(a, 2), scope: a[4] });
