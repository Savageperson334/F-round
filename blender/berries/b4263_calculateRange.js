// calculateRange
//
// Copied verbatim from https://github.com/JamelSyh/braille-translator
//   file frontend/braille-translator/src/hooks/useTable.js, line 3
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Braille and tactile information
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const calculateRange = (data, rowsPerPage) => {
  const range = [];
  const num = Math.ceil(data.length / rowsPerPage);
  let i = 1;
  for (let i = 1; i <= num; i++) {
    range.push(i);
  }
  return range;
};
