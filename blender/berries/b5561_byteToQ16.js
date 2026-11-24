// byteToQ16
//
// Copied verbatim from https://github.com/oscillr/LRRY
//   file lrry/web/editor/wavetable.js, line 31
//   licence (as GitHub reports it): GPL-3.0   see ../licenses/
//   catalogue shelf: Small synthesizers and circuits
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const AMP_LUT = [65536, 62757, 60097, 57549, 55109, 52773, 50535, 48393, 46341, 44376, 42495, 40693, 38968, 37316, 35734, 34219];


const byteToQ16 = (b) => (b ? AMP_LUT[(255 - b) & 15] >> ((255 - b) >> 4) : 0);
