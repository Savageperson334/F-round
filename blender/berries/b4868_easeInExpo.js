// easeInExpo
//
// Copied verbatim from https://github.com/cikelino/ferrofluid
//   file src/app/utils.js, line 20
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//   the same function also appears in: robert-leitl/ferrofluid
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const easeInExpo = (x) => {
    return x === 0 ? 0 : Math.pow(2, 10 * x - 10);
}
