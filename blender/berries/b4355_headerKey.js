// headerKey
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/conditions/table.js, line 27
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function headerKey(header) {
  const parts = String(header).split('.')
  const prefix = parts[0]
  if (prefix === 'ENV') return parts.length > 2 ? parts.slice(0, -1).join('.') : header
  if (prefix === 'SURF') return parts.length > 3 ? parts.slice(0, -1).join('.') : header
  return parts.slice(0, 2).join('.')
}
