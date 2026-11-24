// optionValue
//
// Copied verbatim from https://github.com/hopechen067/MapStage
//   file mapstage/runtime/benchmark-vector-tuning.mjs, line 105
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Historic cartography
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function optionValue(argv, index, inlineValue, name) {
  if (inlineValue != null) return { value: inlineValue, nextIndex: index };
  if (index + 1 >= argv.length) throw new Error(name + ' requires a value');
  return { value: argv[index + 1], nextIndex: index + 1 };
}
