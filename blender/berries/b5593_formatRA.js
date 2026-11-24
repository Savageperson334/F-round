// formatRA
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 341
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatRA(raDeg) {
  // Normalize to [0, 360)
  let ra = ((raDeg % 360) + 360) % 360;
  const hours = ra / 15;
  const h = Math.floor(hours);
  const m = Math.floor((hours - h) * 60);
  const s = ((hours - h) * 60 - m) * 60;
  return `${h}h${String(m).padStart(2, "0")}m${s.toFixed(1).padStart(4, "0")}s`;
}
