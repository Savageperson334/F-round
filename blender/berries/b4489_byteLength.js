// byteLength
//
// Copied verbatim from https://github.com/Rickyslim/insects-detection-webui
//   file src/utils/index.js, line 120
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Moths insects and insect traps
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function byteLength(str) {
  // returns the byte length of an utf8 string
  let s = str.length
  for (var i = str.length - 1; i >= 0; i--) {
    const code = str.charCodeAt(i)
    if (code > 0x7f && code <= 0x7ff) s++
    else if (code > 0x7ff && code <= 0xffff) s += 2
    if (code >= 0xDC00 && code <= 0xDFFF) i--
  }
  return s
}
