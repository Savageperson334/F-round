// unproject
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file frontend/modules/marine-map/web/index.js, line 492
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const TILE_SIZE = 256;


function unproject(x, y, z) {
  const scale = TILE_SIZE * 2 ** z;
  const n = Math.PI - (2 * Math.PI * y) / scale;
  const lat = (180 / Math.PI) * Math.atan(Math.sinh(n));
  const lon = ((((x / scale) * 360) % 360) + 360) % 360 - 180;
  return [lat, lon];
}
