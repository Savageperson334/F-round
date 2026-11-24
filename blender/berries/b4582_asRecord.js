// asRecord
//
// Copied verbatim from https://github.com/Vishnu-tppr/motionloom-studio
//   file engine/src/project-contract.js, line 98
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Generative typography and glyphs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function asRecord(value, label = 'project') {
  if (value && typeof value === 'object' && !Array.isArray(value)) {
    return /** @type {Record<string, unknown>} */ (value);
  }
  throw new Error(`${label} must be a JSON object`);
}
