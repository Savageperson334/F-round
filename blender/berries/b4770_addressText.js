// addressText
//
// Copied verbatim from https://github.com/amacias/octo-vave
//   file web/app.js, line 847
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function addressText(a) {
  if (!a) return "not sendable";
  if (a.cc != null) return `CC ${a.cc} · ch ${a.channel ?? "note"}`;
  if (Array.isArray(a.nrpn)) return `NRPN ${a.nrpn.join("/")} · ch ${a.channel ?? "note"}`;
  if (a.dx7 != null) return `DX7 param ${a.dx7}`;
  if (a.sysex) return a.sysex;
  return "?";
}
