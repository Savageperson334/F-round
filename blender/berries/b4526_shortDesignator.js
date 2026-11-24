// shortDesignator
//
// Copied verbatim from https://github.com/TerjeRu/orrery
//   file ui/src/naming.js, line 16
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function shortDesignator(bodyName, systemName) {
  if (!bodyName || !systemName) return bodyName;
  const prefix = `${systemName} `;
  return bodyName.startsWith(prefix) ? bodyName.slice(prefix.length) : bodyName;
}
