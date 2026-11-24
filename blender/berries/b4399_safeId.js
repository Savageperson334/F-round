// safeId
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/simulation/local/tracer.js, line 12
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const safeId = (id) => String(id).replace(/[^A-Za-z0-9_]/g, '_')
