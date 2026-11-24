// resolveGlobalSeaName
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 627
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function resolveGlobalSeaName(lat, lon) {
  if (lon >= 95 && lon <= 142 && lat >= -11 && lat <= 8) return "Perairan Nusantara / Segitiga Terumbu Karang";
  if ((lon >= 100 && lon <= 180) || (lon >= -180 && lon <= -70)) {
    if (lat > 23.5) return "Samudra Pasifik Utara";
    if (lat < -23.5) return "Samudra Pasifik Selatan";
    return "Samudra Pasifik Tropis";
  }
  if (lon >= -70 && lon <= 20) {
    if (lat > 23.5) return "Samudra Atlantik Utara";
    if (lat < -23.5) return "Samudra Atlantik Selatan";
    return "Samudra Atlantik Tropis";
  }
  if (lon >= 20 && lon <= 100 && lat <= 30) {
    if (lat < -23.5) return "Samudra Hindia Selatan";
    return "Samudra Hindia Tropis";
  }
  if (lat < -60) return "Samudra Antarktika (Southern Ocean)";
  if (lat > 66) return "Samudra Arktik";
  return "Perairan Internasional";
}
