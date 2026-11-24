// zscoreRobust
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/soundBaseline.js, line 49
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function zscoreRobust(value, medianVal, sigmaVal) {
  if (typeof value !== 'number' || typeof medianVal !== 'number' || typeof sigmaVal !== 'number' || sigmaVal === 0) return null;
  return (value - medianVal) / sigmaVal;
}
