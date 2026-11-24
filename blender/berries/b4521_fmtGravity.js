// fmtGravity
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/data-panel.js, line 33
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmtGravity(g) {
  if (typeof g !== 'number') return '—';
  return `${g.toFixed(2)} G`;
}
