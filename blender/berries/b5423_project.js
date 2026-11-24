// project
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file frontend/modules/marine-map/web/index.js, line 483
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TILE_SIZE = 256;


const clamp = (value, low, high) => Math.min(high, Math.max(low, value));


function project(lat, lon, z) {
  const scale = TILE_SIZE * 2 ** z;
  const clampedLat = clamp(lat, -85.05112878, 85.05112878);
  const sinLat = Math.sin((clampedLat * Math.PI) / 180);
  const x = ((lon + 180) / 360) * scale;
  const y = (0.5 - Math.log((1 + sinLat) / (1 - sinLat)) / (4 * Math.PI)) * scale;
  return [x, y];
}
