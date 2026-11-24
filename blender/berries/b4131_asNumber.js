// asNumber
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/health.js, line 25
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function asNumber(value) {
  const n = Number(value);
  return Number.isFinite(n) ? n : null;
}
