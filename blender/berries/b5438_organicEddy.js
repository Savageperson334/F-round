// organicEddy
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 443
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function organicEddy(lat, lon, seed = 0) {
  // Strictly integer longitude frequencies guarantee 100% seamless wrap at +-180 deg
  const x = (lon * Math.PI) / 180;
  const y = (lat * Math.PI) / 180;
  const wx = x + 0.22 * Math.sin(y * 6.0 + seed) * Math.cos(x * 4.0 - seed * 0.5);
  const wy = y + 0.22 * Math.cos(x * 5.0 - seed * 0.7) * Math.sin(y * 7.0 + seed);
  const n1 = Math.sin(wx * 4.0 + seed) * Math.cos(wy * 5.0 - seed * 0.4);
  const n2 = 0.55 * Math.sin(wx * 9.0 + 1.4 - seed * 0.8) * Math.sin(wy * 11.0 + 0.8);
  const n3 = 0.30 * Math.cos(wx * 16.0 - 0.9 + seed * 1.1) * Math.sin(wy * 17.0 + 1.9);
  return (n1 + n2 + n3) / 1.85;
}
