// sstToRgba
//
// Copied verbatim from https://github.com/muhammadfahas/lautscan
//   file web/_worker.js, line 653
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


function sstToRgba(sst) {
  let u;
  if (sst < 18.0) {
    u = Math.max(0, (sst + 2.0) / 20.0) * 0.42;
  } else if (sst < 26.0) {
    u = 0.42 + ((sst - 18.0) / 8.0) * 0.23;
  } else {
    u = 0.65 + Math.min(1, (sst - 26.0) / 5.2) * 0.35;
  }
  const a = Math.round(145 + 65 * smoothstep(0.15, 0.85, u));
  if (u < 0.25) {
    const t = u / 0.25;
    return [Math.round(13 + (106 - 13) * t), Math.round(8 + (0 - 8) * t), Math.round(135 + (168 - 135) * t), a];
  } else if (u < 0.50) {
    const t = (u - 0.25) / 0.25;
    return [Math.round(106 + (192 - 106) * t), Math.round(0 + (54 - 0) * t), Math.round(168 + (132 - 168) * t), a];
  } else if (u < 0.72) {
    const t = (u - 0.50) / 0.22;
    return [Math.round(192 + (232 - 192) * t), Math.round(54 + (108 - 54) * t), Math.round(132 + (90 - 132) * t), a];
  } else if (u < 0.88) {
    const t = (u - 0.72) / 0.16;
    return [Math.round(232 + (252 - 232) * t), Math.round(108 + (168 - 108) * t), Math.round(90 + (52 - 90) * t), a];
  } else {
    const t = (u - 0.88) / 0.12;
    return [Math.round(252 + (245 - 252) * t), Math.round(168 + (246 - 168) * t), Math.round(52 + (42 - 52) * t), a];
  }
}
