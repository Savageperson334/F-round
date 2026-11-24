// generateOperations
//
// Copied verbatim from https://github.com/asyncapi-archived-repos/simulator
//   file src/parser/GenerateOperationsAndScenarios.js, line 42
//   licence (as GitHub reports it): Apache-2.0   see ../licenses/
//   catalogue shelf: Public transport and city motion
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function generateOperations (scenarioParsed) {
  const operations = {};

  for (const [name,value] of Object.entries(scenarioParsed)) {
    if (!name.match(RegExp(/^scenario-[\w\d]+$/))) {
      Object.assign(operations,{[name]: value});
    }
  }

  return operations;
}
