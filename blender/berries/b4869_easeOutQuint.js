// easeOutQuint
//
// Copied verbatim from https://github.com/cikelino/ferrofluid
//   file src/app/utils.js, line 24
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//   the same function also appears in: robert-leitl/ferrofluid
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const easeOutQuint = (x) => {
    return 1 - Math.pow(1 - x, 5);
}
