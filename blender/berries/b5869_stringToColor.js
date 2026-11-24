// stringToColor
//
// Copied verbatim from https://github.com/rewonc/pastalog
//   file src/lib.js, line 66
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


function hashCode(str) {
  let i;
  let chr;
  let len;
  let hash = 0;
  if (str.length === 0) return hash;
  for (i = 0, len = str.length; i < len; i++) {
    chr = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + chr;
    hash |= 0;
  }
  return hash;
}


function stringToColor(str) {
  return intToHex(hashCode(str));
}
