// rightPadDecimals2
//
// Copied verbatim from https://github.com/rewonc/pastalog
//   file src/lib.js, line 9
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Graphs and networks
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function round2(input) {
  return Math.round(input * 100) / 100;
}


function rightPadDecimals2(input) {
  const number = round2(input);
  const str = number.toString();
  const splits = str.split('.');
  if (splits[1] === undefined) {
    return `${str}.00`;
  }
  if (splits[1].length === 1) {
    return `${str}0`;
  }
  return str;
}
