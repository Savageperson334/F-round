// sortDeep
//
// Copied verbatim from https://github.com/MoneyPack/Orrery
//   file electron/fixtures/mcp-stdio-server.mjs, line 160
//   licence (as GitHub reports it): MIT   see ../licenses/
//   catalogue shelf: Astronomical clocks and orreries
//
// Everything below the line is that repository's code, unmodified. Imports, constants and
// helper functions it needs from the same file are included, also unmodified.
// ----------------------------------------------------------------------------


function sortDeep(value) {
  if (Array.isArray(value)) return value.map(sortDeep);
  if (value === null || typeof value !== "object") return value;
  const ordered = {};
  for (const key of Object.keys(value).sort()) ordered[key] = sortDeep(value[key]);
  return ordered;
}
