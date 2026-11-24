// clamp
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file frontend/modules/marine-map/web/index.js, line 457
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clamp = (value, low, high) => Math.min(high, Math.max(low, value));
