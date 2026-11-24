// smoothNoise
//
// Copied verbatim from https://github.com/cepdnaclk/e19-3yp-beehive-monitoring-system
//   file code/backend/src/bridge/simulate.js, line 110
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


function smoothNoise(tMs, periodMs, salt = 0) {
  const p = tMs / periodMs + salt * 1000;
  const i = Math.floor(p);
  const f = p - i;
  const s = f * f * (3 - 2 * f); // smoothstep, so the joins are not visible
  return (hash01(i) * (1 - s) + hash01(i + 1) * s) * 2 - 1;
}
