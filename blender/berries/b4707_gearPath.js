// gearPath
//
// Copied verbatim from https://github.com/adamgilman/Orrery
//   file site/landing/build.mjs, line 64
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const f2 = (v) => v.toFixed(2);


function gearPath(teeth, r) {
  const add = r * 0.11, ded = r * 0.12, half = Math.PI / teeth;
  const pt = (rad, ang) => `${f2(rad * Math.cos(ang))} ${f2(rad * Math.sin(ang))}`;
  const pts = [];
  for (let i = 0; i < teeth; i++) {
    const a = i * 2 * half;
    pts.push(pt(r - ded, a - half * 0.55), pt(r - ded, a - half * 0.45), pt(r + add, a - half * 0.22), pt(r + add, a + half * 0.22), pt(r - ded, a + half * 0.45), pt(r - ded, a + half * 0.55));
  }
  return `M${pts.join(" L")} Z`;
}
