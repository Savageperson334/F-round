// computeGlobalWeatherRain
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 734
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const GLOBAL_CYCLONES = [
  { id: "storm-94s", name: "Bibit Siklon Tropis 94S", region: "Samudra Hindia Selatan Jawa-Bali", lat: -12.4, lon: 108.5, rKm: 340, peakRain: 45, windKnots: 42, level: "SIAGA TINGGI" },
  { id: "storm-squall-natuna", name: "Vorteks & Squall Line Laut Natuna", region: "Laut Natuna Utara", lat: 4.2, lon: 108.2, rKm: 260, peakRain: 33, windKnots: 30, level: "WASPADA" },
  { id: "storm-wpac-low", name: "Taifun Tropis Yinxing (02W)", region: "Samudra Pasifik Barat / Laut Filipina", lat: 14.5, lon: 132.8, rKm: 380, peakRain: 48, windKnots: 56, level: "BERBAHAYA" },
  { id: "storm-andaman-low", name: "Depresi Tropis Teluk Benggala", region: "Samudra Hindia Utara / Laut Andaman", lat: 10.8, lon: 89.4, rKm: 280, peakRain: 29, windKnots: 32, level: "WASPADA" },
  { id: "storm-swio-bheki", name: "Siklon Tropis Bheki (03S)", region: "Samudra Hindia Barat Daya", lat: -16.8, lon: 62.4, rKm: 360, peakRain: 46, windKnots: 58, level: "BERBAHAYA" },
  { id: "storm-epac-kristy", name: "Badai Tropis Kristy (14E)", region: "Samudra Pasifik Timur", lat: 16.2, lon: -112.5, rKm: 340, peakRain: 39, windKnots: 48, level: "SIAGA TINGGI" },
  { id: "storm-natl-kirk", name: "Hurricane Kirk (AL12)", region: "Samudra Atlantik Utara Tengah", lat: 24.6, lon: -54.8, rKm: 420, peakRain: 52, windKnots: 64, level: "BERBAHAYA" },
  { id: "storm-spac-01f", name: "Depresi Tropis 01F", region: "Samudra Pasifik Selatan / Laut Koral", lat: -17.5, lon: 168.0, rKm: 300, peakRain: 31, windKnots: 34, level: "WASPADA" },
  { id: "storm-npac-kuroshio", name: "Siklon Ekstratropis Pasifik Utara", region: "Samudra Pasifik Utara / Kuroshio", lat: 37.5, lon: 158.0, rKm: 400, peakRain: 36, windKnots: 48, level: "SIAGA TINGGI" },
  { id: "storm-satl-sub", name: "Vorteks Subtropis Atlantik Selatan", region: "Samudra Atlantik Selatan", lat: -28.4, lon: -36.5, rKm: 320, peakRain: 28, windKnots: 34, level: "WASPADA" },
  { id: "storm-arabian-04a", name: "Siklon Tropis Laut Arab (04A)", region: "Samudra Hindia Barat Laut / Laut Arab", lat: 14.2, lon: 61.8, rKm: 330, peakRain: 38, windKnots: 44, level: "SIAGA TINGGI" },
  { id: "storm-npac-aleutian", name: "Siklon Ekstratropis Aleutian", region: "Samudra Pasifik Utara Tengah", lat: 48.5, lon: -164.0, rKm: 460, peakRain: 35, windKnots: 52, level: "SIAGA TINGGI" },
  { id: "storm-natl-iceland", name: "Vorteks Ekstratropis Atlantik Utara", region: "Samudra Atlantik Utara / Laut Labrador", lat: 55.2, lon: -32.4, rKm: 450, peakRain: 34, windKnots: 50, level: "SIAGA TINGGI" },
  { id: "storm-south-ocean", name: "Pusaran Badai Samudra Selatan", region: "Samudra Antarktika / Australia Selatan", lat: -51.6, lon: 138.0, rKm: 480, peakRain: 32, windKnots: 54, level: "BERBAHAYA" }
];


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


function wrapLonDelta(lon, centerLon) {
  let d = ((lon - centerLon + 180) % 360 + 360) % 360 - 180;
  return d;
}


function smoothstep(edge0, edge1, x) {
  const t = Math.max(0, Math.min(1, (x - edge0) / (edge1 - edge0)));
  return t * t * (3 - 2 * t);
}


function computeGlobalWeatherRain(lat, lon) {
  const itczLat = 4.0 * Math.sin((lon * Math.PI) / 90);
  const itczBand = Math.exp(-(((lat - itczLat) / 5.5) ** 2)) * (4.5 + 3.2 * Math.max(0, organicEddy(lat, lon, 3.1)));
  const stormTrack = Math.exp(-(((Math.abs(lat) - 42) / 8.0) ** 2)) * Math.max(0, organicEddy(lat, lon, 5.4)) * 6.5;
  let rain = itczBand + stormTrack;

  const cosLat = Math.max(0.25, Math.cos((lat * Math.PI) / 180));
  for (let i = 0; i < GLOBAL_CYCLONES.length; i++) {
    const s = GLOBAL_CYCLONES[i];
    const dLatDeg = lat - s.lat;
    if (Math.abs(dLatDeg) > 7.5) continue;
    const dLonDeg = wrapLonDelta(lon, s.lon);
    if (Math.abs(dLonDeg) > 9.0) continue;
    const dxKm = dLonDeg * cosLat * 111.32;
    const dyKm = dLatDeg * 111.32;
    const rKm = Math.hypot(dxKm, dyKm);
    if (rKm >= s.rKm * 1.15) continue;
    const dir = s.lat < 0 ? 1 : -1;
    const theta = Math.atan2(dyKm, dxKm);
    const spiralArm = 0.62 + 0.38 * Math.cos(2 * theta - dir * Math.pow(rKm / 65, 0.85) * 3.0);
    const radialEnv = Math.exp(-((rKm / (s.rKm * 0.56)) ** 1.55)) * smoothstep(0, 18, rKm);
    rain += s.peakRain * radialEnv * spiralArm;
  }
  return rain;
}
