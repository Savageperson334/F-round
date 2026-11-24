// fmtRA
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/inline_widget.js, line 1173
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmtRA(deg) {
  const h = deg/15, hi = Math.floor(h), mi = Math.floor((h-hi)*60), s = ((h-hi)*60-mi)*60;
  return hi+"h"+String(mi).padStart(2,"0")+"m"+s.toFixed(1).padStart(4,"0")+"s";
}
