// intToHex
//
// Copied verbatim from https://github.com/rewonc/pastalog
//   file src/lib.js, line 54
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function intToHex(i) {
  let hex = ((i >> 24) & 0xFF).toString(16).slice(-2) +
              ((i >> 16) & 0xFF).toString(16).slice(-2) +
              ((i >> 8) & 0xFF).toString(16).slice(-2) +
              (i & 0xFF).toString(16).slice(-2);
  hex = hex.slice(-6);
  while (hex.length < 6) {
    hex = `0${hex}`;
  }
  return `#${hex}`;
}
