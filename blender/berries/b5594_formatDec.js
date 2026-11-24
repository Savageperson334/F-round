// formatDec
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/projection.js, line 356
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatDec(decDeg) {
  const sign = decDeg >= 0 ? "+" : "-";
  const abs = Math.abs(decDeg);
  const d = Math.floor(abs);
  const m = Math.floor((abs - d) * 60);
  const s = ((abs - d) * 60 - m) * 60;
  return `${sign}${d}°${String(m).padStart(2, "0")}'${s.toFixed(1).padStart(4, "0")}"`;
}
