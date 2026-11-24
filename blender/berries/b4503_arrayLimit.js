// arrayLimit
//
// Copied verbatim from https://github.com/SIOTLAB/BeehiveMonitoring
//   file web-app/backend/models/apiary.model.js, line 78
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function arrayLimit(val) {
  return val.length <= 10;
}
