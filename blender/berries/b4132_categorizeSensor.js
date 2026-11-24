// categorizeSensor
//
// Copied verbatim from https://github.com/Agerbi-Nouha/beehive-monitoring-app
//   file backend/src/utils/health.js, line 30
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


function asNumber(value) {
  const n = Number(value);
  return Number.isFinite(n) ? n : null;
}


function inRange(value, range) {
  return typeof value === 'number' && value >= range[0] && value <= range[1];
}


function categorizeSensor(sensor, value, thresholds) {
  const v = asNumber(value);
  if (v === null) return SENSOR_STATUS.OK;

  if (sensor === 'motion' || sensor === 'rain') return v === 1 ? SENSOR_STATUS.WARNING : SENSOR_STATUS.OK;
  if (sensor === 'flame') return v === 1 ? SENSOR_STATUS.DANGER : SENSOR_STATUS.OK;

  const th = thresholds?.[sensor];
  if (!th) return SENSOR_STATUS.OK;

  if (th.normal && inRange(v, th.normal)) return SENSOR_STATUS.OK;
  if (Array.isArray(th.warning)) {
    for (const rng of th.warning) {
      if (inRange(v, rng)) return SENSOR_STATUS.WARNING;
    }
  }
  return SENSOR_STATUS.DANGER;
}
