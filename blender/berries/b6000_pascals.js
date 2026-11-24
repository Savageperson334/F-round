// pascals
//
// Copied verbatim from https://github.com/stoatworks-labs/ferrofluid
//   file demo/plugin.js, line 1690
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Ferrofluids and magnetic materials
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const pascals = (pa) => {
  if (pa <= 0) return 'off';
  const exponent = Math.floor(Math.log10(pa));
  return `${(pa / 10 ** exponent).toFixed(2)}e${exponent} Pa`;
};
