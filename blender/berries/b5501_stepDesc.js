// stepDesc
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/locks.js, line 60
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const stepMemo = new Map();


const stepDesc = (max) => { max = Math.min(64, Math.max(1, max)); if (!stepMemo.has(max)) stepMemo.set(max, { label: "STEP", fmt: 1, min: 1, max, def: 1, fk: -1, unit: "", names: null, order: null }); return stepMemo.get(max); };
