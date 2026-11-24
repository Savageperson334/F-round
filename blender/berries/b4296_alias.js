// alias
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/generate-scenario-registry.mjs, line 32
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function alias(prefix, id) {
  return prefix + id.replace(/[^A-Za-z0-9_]/g, '_');
}
