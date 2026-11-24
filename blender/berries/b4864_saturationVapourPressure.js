// saturationVapourPressure
//
// Copied verbatim from https://github.com/cepdnaclk/e19-3yp-beehive-monitoring-system
//   file code/backend/src/bridge/simulate.js, line 141
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const saturationVapourPressure = (celsius) =>
  6.112 * Math.exp((17.67 * celsius) / (celsius + 243.5));
