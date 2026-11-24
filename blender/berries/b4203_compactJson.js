// compactJson
//
// Copied verbatim from https://github.com/Flowm/satvis
//   file scripts/parity/generate.mjs, line 37
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Satellites and orbital systems
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------

const INLINE_JSON_LENGTH = 120;


function compactJson(value, indent = "") {
  const inline = JSON.stringify(value);
  if (value === null || typeof value !== "object" || inline.length <= INLINE_JSON_LENGTH || Object.values(value).every((item) => item === null || typeof item !== "object")) {
    return inline;
  }
  const inner = `${indent}  `;
  const items = Array.isArray(value)
    ? value.map((item) => `${inner}${compactJson(item, inner)}`)
    : Object.entries(value)
        .filter(([, item]) => item !== undefined)
        .map(([key, item]) => `${inner}${JSON.stringify(key)}: ${compactJson(item, inner)}`);
  const [open, close] = Array.isArray(value) ? ["[", "]"] : ["{", "}"];
  return items.length === 0 ? `${open}${close}` : `${open}\n${items.join(",\n")}\n${indent}${close}`;
}
