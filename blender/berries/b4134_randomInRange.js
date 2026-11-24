// randomInRange
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/simulator.js, line 14
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//   the same function also appears in: Akshatchaube01/TimeWarp, experimentalDataAesthetics/play-splom
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function randomInRange(min, max) {
  return Math.random() * (max - min) + min;
}
