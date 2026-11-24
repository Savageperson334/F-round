// diurnalTemperature
//
// Copied verbatim from https://github.com/cepdnaclk/e19-3yp-beehive-monitoring-system
//   file code/backend/src/bridge/simulate.js, line 130
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const SUNRISE = 6.0;


function diurnalTemperature(hour, tMin, tMax, peakHour) {
  if (hour >= SUNRISE && hour <= peakHour) {
    const frac = (hour - SUNRISE) / (peakHour - SUNRISE);
    return tMin + (tMax - tMin) * Math.sin((frac * Math.PI) / 2);
  }
  const sincePeak = (hour - peakHour + 24) % 24;
  const nightLength = 24 - peakHour + SUNRISE;
  return tMin + (tMax - tMin) * Math.exp((-2.6 * sincePeak) / nightLength);
}
