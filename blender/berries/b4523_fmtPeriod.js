// fmtPeriod
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/data-panel.js, line 50
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmtPeriod(seconds) {
  if (typeof seconds !== 'number') return '—';
  const days = seconds / 86400;
  if (days < 2) return `${(seconds / 3600).toFixed(1)} h`;
  if (days < 1000) return `${days.toFixed(1)} d`;
  return `${(days / 365.25).toFixed(1)} yr`;
}
