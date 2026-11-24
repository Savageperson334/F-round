// potentialToRgba
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 701
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ocean currents and fluid dynamics
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function smoothstep(edge0, edge1, x) {
  const t = Math.max(0, Math.min(1, (x - edge0) / (edge1 - edge0)));
  return t * t * (3 - 2 * t);
}


function potentialToRgba(pot) {
  const u = Math.max(0, Math.min(1, (pot - 22) / 68));
  // Quiet open water (<45%) stays subtle so hotspots (>=72%) pop unmistakably
  const a = Math.round(40 + 195 * smoothstep(0.12, 0.85, u));
  if (u < 0.36) {
    const t = u / 0.36;
    return [Math.round(12 + (20 - 12) * t), Math.round(85 + (178 - 85) * t), Math.round(110 + (162 - 110) * t), a];
  } else if (u < 0.68) {
    const t = (u - 0.36) / 0.32;
    return [Math.round(20 + (34 - 20) * t), Math.round(178 + (197 - 178) * t), Math.round(162 + (94 - 162) * t), a];
  } else {
    const t = (u - 0.68) / 0.32;
    return [Math.round(34 + (248 - 34) * t), Math.round(197 + (168 - 197) * t), Math.round(94 + (18 - 94) * t), a];
  }
}
