// roundDecimalToFourDigits
//
// Copied verbatim from https://github.com/lilkraftwerk/lineboi3000
//   file src/utils/coordUtils.js, line 4
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Plotters & drawing machines
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const roundDecimalToFourDigits = (decimal) => {
    return +`${Math.round(`${decimal}e+4`)}e-4`;
};
