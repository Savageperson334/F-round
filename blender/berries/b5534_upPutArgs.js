// upPutArgs
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/proto.js, line 81
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const asc = (s) => [...s].map((c) => c.charCodeAt(0) & 127);


const cstr = (s) => [...asc(s), 0];


const v14 = (v) => { const x = v + 8192; return [x & 127, x >> 7 & 127]; };


const upPutArgs = (slot, eng, name, values, cat = 0, notes = null) =>
  [slot, eng, ...cstr(name), ...values.flatMap(v14), ...Array.from({ length: 16 }, (_, i) => notes?.[i] ?? [0, 0]).flat(), 0, ...new Array(16).fill(0), cat];
