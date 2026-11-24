// computeGlobalCurrentsAt
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 979
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function computeGlobalCurrentsAt(lat, lon) {
  const latRad = (lat * Math.PI) / 180;
  const lonRad = (lon * Math.PI) / 180;
  let u = 0, v = 0;

  if (lat >= -65 && lat <= -45) u += 0.45 * Math.sin(((lat + 55) / 10) * (Math.PI / 2));
  if ((lat >= -15 && lat <= -3) || (lat >= 10 && lat <= 20)) u -= 0.35;
  if (lat >= 2 && lat <= 8) u += 0.38;
  if (lon >= -82 && lon <= -40 && lat >= 25 && lat <= 52) {
    const factor = Math.exp(-(((lat - 38) / 12) ** 2) - (((lon + 65) / 18) ** 2));
    u += 0.55 * factor; v += 0.45 * factor;
  }
  if (lon >= 125 && lon <= 155 && lat >= 20 && lat <= 42) {
    const factor = Math.exp(-(((lat - 32) / 10) ** 2) - (((lon - 138) / 14) ** 2));
    u += 0.48 * factor; v += 0.40 * factor;
  }
  if (lon >= -85 && lon <= -72 && lat >= -42 && lat <= -8) v += 0.32;
  if (lon >= -130 && lon <= -116 && lat >= 24 && lat <= 44) v -= 0.28;
  if (lon >= 10 && lon <= 18 && lat >= -34 && lat <= -16) v += 0.30;

  u += 0.18 * Math.sin(latRad * 3.5 + lonRad * 2.0);
  v += 0.16 * Math.cos(lonRad * 3.0 + latRad * 1.5);

  const speed_ms = Math.round(Math.hypot(u, v) * 1000) / 1000;
  const speed_knots = Math.round(speed_ms * 1.94384 * 1000) / 1000;
  const dirDeg = Math.round(((Math.atan2(u, v) * (180 / Math.PI) + 360) % 360) * 10) / 10;

  return { u: Math.round(u * 1000) / 1000, v: Math.round(v * 1000) / 1000, speed_ms, speed_knots, direction_deg: dirDeg };
}
