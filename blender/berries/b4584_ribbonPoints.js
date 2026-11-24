// ribbonPoints
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/scenes/demo.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function ribbonPoints(t, mode = 0) {
  const pts = [];
  for (let i = 0; i <= 30; i++) { const x = -100 + i * 50; const y = mode === 0 ? 370 + Math.sin(i * .45 + t * 4) * 55 : 370 + Math.sin(i * .25 + t * 2) * (45 + i * 1.4); pts.push([x, y]); }
  return pts;
}
