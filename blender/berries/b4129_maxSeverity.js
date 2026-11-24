// maxSeverity
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/health.js, line 17
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SENSOR_STATUS = {
  OK: 'OK',
  WARNING: 'WARNING',
  DANGER: 'DANGER',
};

const SEVERITY_RANK = {
  [SENSOR_STATUS.OK]: 0,
  [SENSOR_STATUS.WARNING]: 1,
  [SENSOR_STATUS.DANGER]: 2,
};


function maxSeverity(a, b) {
  return SEVERITY_RANK[a] >= SEVERITY_RANK[b] ? a : b;
}
