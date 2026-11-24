// clamp
//
// Copied verbatim from https://github.com/cikelino/ferrofluid
//   file src/app/utils.js, line 5
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//   the same function also appears in: robert-leitl/ferrofluid
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const clamp = (num, min, max) => Math.min(Math.max(num, min), max);
