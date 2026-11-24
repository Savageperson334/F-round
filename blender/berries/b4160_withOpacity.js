// withOpacity
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file app.js, line 108
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function withOpacity(hex, alpha) {
  const value = parseInt(hex.slice(1), 16);
  /* eslint-disable no-bitwise */
  return `rgba(${(value >> 16) & 255},${(value >> 8) & 255},${value & 255},${alpha})`;
  /* eslint-enable no-bitwise */
}
