// xWriteArgs
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 111
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const XSCOPE = 2;


const v14 = (v) => { const x = v + 8192; return [x & 127, x >> 7 & 127]; };


const xWriteArgs = (part, k, v) => [part, k, ...v14(v), XSCOPE];
