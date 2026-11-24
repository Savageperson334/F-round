// fmtDec
//
// Copied verbatim from https://github.com/ovro-lwa/astrowidget
//   file js/inline_widget.js, line 1177
//   licence (as GitHub reports it): BSD-3-Clause   see ../licenses/
//   catalogue shelf: Astronomical observation tools
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function fmtDec(deg) {
  const sign = deg>=0?"+":"-", a = Math.abs(deg), d=Math.floor(a), m=Math.floor((a-d)*60), s=((a-d)*60-m)*60;
  return sign+d+"°"+String(m).padStart(2,"0")+"'"+s.toFixed(1).padStart(4,"0")+'"';
}
