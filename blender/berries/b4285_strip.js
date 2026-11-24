// strip
//
// Copied verbatim from https://github.com/Mohammad-Mirasadollahi/Attack-Explorer
//   file scripts/fix-narrative-mod-fields.mjs, line 21
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Sensors and telemetry
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function strip(s) {
  return String(s || '')
    .replace(/—/g, '-')
    .replace(/\s+/g, ' ')
    .trim();
}
