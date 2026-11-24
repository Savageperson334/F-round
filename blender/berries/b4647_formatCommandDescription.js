// formatCommandDescription
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/dev/help.js, line 53
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function formatCommandDescription(commandHelp, namespace, command) {
  const { args, description } = commandHelp;
  return `  ${namespace}.${command}${args ?? ""} - ${description}`;
}
