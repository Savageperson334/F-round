// motionDeleteArgs
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 118
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const motionDeleteArgs = (track, step, tid) => (tid >= 128 ? [track, 10, step, tid & 127, 1] : [track, 4, step, tid]);
