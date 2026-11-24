// pickDeclared
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/simulation/local/speciesProperties.js, line 72
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const pickDeclared = (source, keys) => {
  const picked = {}
  for (const key of keys) {
    if (source[key] !== undefined && source[key] !== null) {
      picked[key] = source[key]
    }
  }
  return picked
}
