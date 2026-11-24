// cleanVoiceName
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/dx7import.js, line 23
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function cleanVoiceName(raw, n = 0) {
  let s = String(raw ?? "").replace(/[^\x20-\x7e]/g, " ").toUpperCase();
  s = s.replace(/\bDX\s*7\b[-:. ]*/g, " ").replace(/\s+/g, " ").trim().slice(0, 12).trim();
  return s || `FM VOICE ${String(n + 1).padStart(2, "0")}`;
}
