// degreesToCompass
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 29
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const COMPASS_16 = [
  "N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"
];


function degreesToCompass(deg) {
  const norm = ((deg % 360) + 360) % 360;
  const idx = Math.floor((norm + 11.25) / 22.5) % 16;
  return COMPASS_16[idx];
}
