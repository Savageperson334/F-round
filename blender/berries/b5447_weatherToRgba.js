// weatherToRgba
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 760
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


function weatherToRgba(rain) {
  if (rain < 0.6) return [0, 0, 0, 0];
  const u = Math.max(0, Math.min(1, rain / 44.0));
  const a = Math.round(24 + 140 * smoothstep(0.05, 0.88, u));
  if (u < 0.35) {
    const t = u / 0.35;
    return [Math.round(14 + (2 - 14) * t), Math.round(116 + (132 - 116) * t), Math.round(144 + (199 - 144) * t), a];
  } else if (u < 0.72) {
    const t = (u - 0.35) / 0.37;
    return [Math.round(2 + (56 - 2) * t), Math.round(132 + (189 - 132) * t), Math.round(199 + (248 - 199) * t), a];
  } else {
    const t = (u - 0.72) / 0.28;
    return [Math.round(56 + (224 - 56) * t), Math.round(189 + (242 - 189) * t), Math.round(248 + (254 - 248) * t), a];
  }
}
