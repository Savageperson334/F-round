// computeGlobalSst
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 574
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function wrapLonDelta(lon, centerLon) {
  let d = ((lon - centerLon + 180) % 360 + 360) % 360 - 180;
  return d;
}


function gauss2d(lat, lon, cLat, cLon, sLat, sLon) {
  const dLat = (lat - cLat) / sLat;
  const dLon = wrapLonDelta(lon, cLon) / sLon;
  const r2 = dLat * dLat + dLon * dLon;
  return r2 > 18 ? 0 : Math.exp(-r2);
}


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


function computeGlobalSst(lat, lon) {
  const latFactor = Math.cos((lat * Math.PI) / 155);
  let sst = 29.8 * Math.pow(Math.max(0, latFactor), 1.45) - 1.2;

  // Smooth wrapped 2D Gaussian ocean basins & currents (zero rectangular seams)
  sst += 1.35 * gauss2d(lat, lon, -2, 125, 13, 30);    // Indo-Pacific Warm Pool
  sst += 4.50 * gauss2d(lat, lon, 40, -50, 15, 22);    // Gulf Stream
  sst += 3.80 * gauss2d(lat, lon, 32, 142, 10, 16);    // Kuroshio Current
  sst -= 5.20 * gauss2d(lat, lon, -22, -78, 18, 9);    // Humboldt / Peru Cold Upwelling
  sst -= 4.00 * gauss2d(lat, lon, 35, -124, 12, 9);    // California Current
  sst -= 4.80 * gauss2d(lat, lon, -25, 14, 10, 6);     // Benguela Cold Upwelling

  sst += 1.65 * organicEddy(lat, lon, 0.0);
  return Math.max(-1.8, Math.min(32.5, Math.round(sst * 100) / 100));
}
