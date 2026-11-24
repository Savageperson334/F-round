// bare
//
// Copied verbatim from https://github.com/adamgilman/Orrery
//   file tools/checkout-stages.mjs, line 6
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const bare = (c) => { const { group, ...rest } = c; return rest; };
