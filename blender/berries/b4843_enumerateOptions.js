// enumerateOptions
//
// Copied verbatim from https://github.com/asyncapi-archived-repos/simulator
//   file src/bin/cli.js, line 15
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const enumerateOptions = (serverNames) => {
  let result = '';
  serverNames.forEach((value,i) => {
    result += `\n${i}: ${value}`;
  });
  return result;
};
