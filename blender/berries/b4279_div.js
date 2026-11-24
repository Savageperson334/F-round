// div
//
// Copied verbatim from https://github.com/MaxAlyokhin/audio-motion-interface
//   file client/src/js/helpers.js, line 24
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Sound sonification
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const div = (value, by) => (value - (value % by)) / by
