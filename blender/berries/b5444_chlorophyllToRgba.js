// chlorophyllToRgba
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 681
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


function chlorophyllToRgba(chl) {
  const logVal = Math.log10(Math.max(0.03, chl) / 0.03) / Math.log10(2.2 / 0.03);
  const u = Math.max(0, Math.min(1, logVal));
  // Low-chlorophyll open ocean stays subtle & translucent; blooms glow vividly
  const a = Math.round(48 + 185 * smoothstep(0.18, 0.88, u));
  if (u < 0.28) {
    const t = u / 0.28;
    return [Math.round(56 + (52 - 56) * t), Math.round(10 + (82 - 10) * t), Math.round(88 + (139 - 88) * t), a];
  } else if (u < 0.56) {
    const t = (u - 0.28) / 0.28;
    return [Math.round(52 + (28 - 52) * t), Math.round(82 + (152 - 82) * t), Math.round(139 + (142 - 139) * t), a];
  } else if (u < 0.80) {
    const t = (u - 0.56) / 0.24;
    return [Math.round(28 + (94 - 28) * t), Math.round(152 + (206 - 152) * t), Math.round(142 + (96 - 142) * t), a];
  } else {
    const t = (u - 0.80) / 0.20;
    return [Math.round(94 + (250 - 94) * t), Math.round(206 + (232 - 206) * t), Math.round(96 + (42 - 96) * t), a];
  }
}
