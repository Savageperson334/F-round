// parseJSON
//
// Copied verbatim from https://github.com/sn3p/Orrery
//   file src/unified/comets/source/contract.js, line 11
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


const requireValue = (ok, label, product = "catalogue") => { if (!ok) throw new Error(`Invalid ${product} ${label}.`); };


function parseJSON(text, product = "catalogue") {
  const value = JSON.parse(text);
  const stack = [];
  const tokens = /"(?:[^"\\]|\\[\s\S])*"|[{}\[\]:,]/g;
  let match;
  try {
    while ((match = tokens.exec(text))) {
      const token = match[0], top = stack.at(-1);
      if (token === "{" || token === "[") {
        requireValue(stack.length < 32, "JSON nesting", product);
        stack.push(token === "{" ? { keys: new Set(), key: true } : {});
      } else if (token === "}" || token === "]") stack.pop();
      else if (token === ":" && top?.keys) top.key = false;
      else if (token === "," && top?.keys) top.key = true;
      else if (token[0] === '"' && top?.keys && top.key) {
        const key = JSON.parse(token);
        requireValue(!top.keys.has(key), "duplicate JSON key", product);
        top.keys.add(key);
      }
    }
  } finally {
    // Engines retain the last successful regexp input through legacy RegExp.$_.
    // Don't retain a whole-file JSON string on success or validation failure.
    /^$/.test("");
  }
  return value;
}
