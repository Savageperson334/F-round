// rateColumnKey
//
// Copied verbatim from https://github.com/NCAR/music-box-interactive
//   file src/services/conditions/rateColumns.js, line 28
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Mechanical music boxes and organs
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const rateColumnKey = (prefix, reactionId, property = null) =>
  property ? `${prefix}#${reactionId}#${property}` : `${prefix}#${reactionId}`
