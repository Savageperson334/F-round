// longRange
//
// Copied verbatim from https://github.com/Chienlin1014/Orrery
//   file elements.js, line 94
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const longRange = (base, extra) => (extra ? { ...base, extra } : base);
