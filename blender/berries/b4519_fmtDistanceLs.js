// fmtDistanceLs
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/data-panel.js, line 16
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmtDistanceLs(ls) {
  if (typeof ls !== 'number') return '—';
  return `${ls.toFixed(ls < 100 ? 2 : 0)} ls`;
}
