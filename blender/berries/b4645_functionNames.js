// functionNames
//
// Copied verbatim from https://github.com/WebOrigami/origami
//   file origami/src/dev/code.js, line 18
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Origami, folds and paper
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function functionNames(code) {
  if (!Array.isArray(code)) {
    return code;
  }
  let [head, ...tail] = code;
  if (typeof head === "function") {
    const text = head.toString();
    if (text.startsWith("«ops.")) {
      head = text;
    } else {
      head = head.name;
    }
  } else {
    head = functionNames(head);
  }
  return [head, ...tail.map(functionNames)];
}
