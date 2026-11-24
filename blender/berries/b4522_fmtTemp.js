// fmtTemp
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/data-panel.js, line 38
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmtTemp(kelvin) {
  if (typeof kelvin !== 'number') return '—';
  return `${kelvin.toFixed(0)} K`;
}
