// hash01
//
// Copied verbatim from https://github.com/cepdnaclk/e19-3yp-beehive-monitoring-system
//   file code/backend/src/bridge/simulate.js, line 105
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Beehives and unusual agriculture
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function hash01(n) {
  const x = Math.sin(n * 127.1) * 43758.5453;
  return x - Math.floor(x);
}
